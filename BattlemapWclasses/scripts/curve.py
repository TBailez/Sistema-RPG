import numpy as np
import cmath
import matplotlib.pyplot as plt
import random
from bezier import quazier

def guess(x1,x2,x3,b):
    if np.cosh(b*x2)==np.cosh(b*x1): b+=0.0001
    return (np.cosh(b*x3)-np.cosh(b*x1))/(np.cosh(b*x2)-np.cosh(b*x1))
    # calcula u baseado no guess de b

def R2D2(x,y,a):
    a=np.radians(a)
    e=np.exp((complex(0,1))*a)
    newp=complex(x,y)*e
    return [newp.real,newp.imag]
    #Complex 2D Rotation (roda um ponto(counterclockwise) em relação a origem com un angulo(a) dado)
    # Rotation 2 D Rotation = R2D2

def testgo(x1,x2,x3,u,f0):
    if abs(x2)>abs(x1): X2=True
    else: X2=False
    if abs(x3)>abs(x2) and abs(x3)>abs(x1):
        if X2:
            if u>=1 and u>=f0: go=True
            else: go=False
        else:
            if u<=0 and u<=f0: go=True
            else: go=False
    else:
        if X2:
            if abs(x3)>abs(x1):
                if u>0 and u<=1:
                    if u<f0: go=True
                    else: go=False
                else: go=False
            else:
                if u<0 and u>f0: go=True
                else: go=False
        else:
            if abs(x3)>abs(x2):
                if u<1 and u>=0:
                    if u>f0: go=True
                    else: go=False
                else: go=False
            else:
                if u>1 and u<f0: go=True
                else: go=False
    return go
    # testa se com os valores x1,x2,x3,u,f0 isso é possivel: f0=u
    #    f(b)=(cosh(x3*b)-cosh(x1*b))/(cosh(x2*b)-cosh(x1*b))
    #    f(0)=f0

def coshka(xs,ys):
    x1=xs[0]
    x2=xs[1]
    x3=xs[2]
    y1=ys[0]
    y2=ys[1]
    y3=ys[2]
    if y2==y1: y2+=0.00001
    u=(y3-y1)/(y2-y1)
    f0=(guess(x1,x2,x3,0))
    go=testgo(x1,x2,x3,u,f0)
    if go:
        gb=0
        g=guess(x1,x2,x3,gb)
        tmax=100
        times=0
        up=True
        dup=0.005
        ant=g
        d=1
        while (abs(g-u)<0.005) or (times<tmax) or (d<0.001):
            if times>tmax: break
            if up:
                gb=dup*2
                dup=gb
                g=guess(x1,x2,x3,gb)
                if abs(g-u)>abs(ant-u):
                    up=False
                    gb=gb/2
                    d=dup/4
                ant=g
            else:
                t1=abs(guess(x1,x2,x3,(gb+d))-u)
                t2=abs(guess(x1,x2,x3,(gb-d))-u)
                t3=abs(guess(x1,x2,x3,gb)-u)
                if t1<t2 and t1<t3: gb+=d
                elif t2<t1 and t2<t3: gb-=d
                elif t3<t1 and t3<t2: pass
                else: break
                g=guess(x1,x2,x3,gb)
                d=d/2
            times+=1
        a=((y2-y1)/(np.cosh(gb*x2)-np.cosh(gb*x1)))
        c=y1-(a*(np.cosh(gb*x1)))
        return [a,gb,c]
    else: return False
    #returns a,b,c pra função a*cosh(b*x)+c=y baseado dos xs e ys passados

def cosh(xs,ys):
    abc=coshka(xs,ys)
    if isinstance(abc,bool): return False
    else:
        a=abc[0]
        b=abc[1]
        c=abc[2]
        X=np.linspace(xs[0],xs[-1])
        y=[]
        for x in X: y.append(a*(np.cosh(b*x))+c)
        # retorna x e y passdo pela curva do cosh
        for j,p in zip(X,y):
            if (abs(xs[1]-j)<1) and (abs(ys[1]-p)<1):
                good=True
                break
            else: good=False
        if good: return [X,y,a,b]
        else: return False

def abcs(xs,ys):
    x1=xs[0]
    x2=xs[1]
    x3=xs[2]
    y1=ys[0]
    y2=ys[1]
    y3=ys[2]
    tit=x2+x1
    if x2==x1: x2+=0.00001
    t=(y2-y1)/(x2-x1)
    VeSeEZero=((x3**2)-(x3*tit)-(x1**2)+(x1*tit))
    if VeSeEZero==0: VeSeEZero=0.00001
    a=(y3-(t*x3)-y1+(x1*t))/VeSeEZero
    b=(y2-y1-(a*((x2**2)-(x1**2))))/(x2-x1)
    c=y1-(a*(x1**2))-(b*x1)
    # returns a,b,c da função quadratica normal
    return [a,b,c]

def qua(xs,ys,Normal=True):
    if (xs[1]>xs[0] and xs[1]>xs[-1]) or (xs[1]<xs[0] and xs[1]<xs[-1]):
        Y=np.linspace(ys[0],ys[-1])
        abc=(abcs(ys,xs))
        QX=Y
    else:
        X=np.linspace(xs[0],xs[-1])
        abc=(abcs(xs,ys))
        QX=X
    y=[]
    a=abc[0]
    b=abc[1]
    c=abc[2]
    for x in QX: y.append((a*(x**2))+(b*x)+c)
    # retorna x e y passdo pela curva quadratica
    if ((xs[1]>xs[0] and xs[1]>xs[-1]) or (xs[1]<xs[0] and xs[1]<xs[-1])) and Normal:
        for j,p in zip(y,QX):
            if (abs(xs[1]-j)<1) and (abs(ys[1]-p)<1):
                good=True
                break
            else: good=False
        if good: return [y,QX,a,b]
        else: return False
    else:
        for j,p in zip(QX,y):
            if (abs(xs[1]-j)<1) and (abs(ys[1]-p)<1):
                good=True
                break
            else: good=False
        if good: return [QX,y,a,b]
        else: return False

def gettit(X,Y,er,teste):
    tit=0
    tits=[]
    titf=False
    while True:
        while tit<360:
            newx=[]
            newy=[]
            for x,y in zip(X,Y):
                r2d2=R2D2(x,y,tit)
                newx.append(r2d2[0])
                newy.append(r2d2[1])
            abc=abcs(newx,newy)
            d0=(-abc[1])/(2*abc[0])
            if teste: tits.append(tit)
            if abs(newx[1]-d0)<er:
                titf=tit
                tit+=er
                #break
            else: tit+=er
        if (isinstance(titf,bool)) or (er>=2): er=er*1.5
        else: break
    newx=[]
    newy=[]
    if teste:
        xs=[]
        ys=[]
        for tt in tits:
            newx=[]
            newy=[]
            for x,y in zip(X,Y):
                r2d2=R2D2(x,y,tt)
                newx.append(r2d2[0])
                newy.append(r2d2[1])
            xs.append(newx)
            ys.append(newy)
        print('foi')
        for x,y in zip(xs,ys): plt.plot(x,y)
        plt.show()
        # plota todas as listas de x,y cada um rotacionado com a(angulo anterior + er) até o titf
    else:
        for x,y in zip(X,Y):
            r2d2=R2D2(x,y,titf)
            newx.append(r2d2[0])
            newy.append(r2d2[1])
        # returns x,y rotacionados com um angulo t(de tal forma q a derivada da função, que foi criada a partir desses pontos, é igual a 0 no x do meio), e o angulo t
        return [newx,newy,titf]

def rq(xs,ys,er,teste,func,true):
    # xs = 3 x dos pontos
    # ys = 3 y dos pontos
    # er = o quanto o angulo cresce a cada iteration
    # teste = if true: plota uns testes ai / se n n
    # func = qual função será usada(ax^2 + bx + c    ou    a*cosh(bx)+c )
    # true = if True: usa o método de checar distancia(mt lento) / se False usa o metodo de achar dx/x de f(x)=0
    #         (Só pra função ax^2+bx+c)
    de1=distance([xs[0],xs[1]],[ys[0],ys[1]])
    de2=distance([xs[1],xs[2]],[ys[1],ys[2]])
    if de1<de2: derro=de1/3
    else: derro=de2/3
    if (func=='qua') and (not true):
        xys=gettit(xs,ys,er,teste)
        if not teste:
            x=xys[0]
            y=xys[1]
            New=qua(x,y)
            if isinstance(New,bool): return False
            else:
                new=[New[0],New[1]]
                X=[]
                Y=[]
                for a,b in zip(new[0],new[1]):
                    n=R2D2(a,b,xys[-1]*(-1))
                    X.append(n[0])
                    Y.append(n[1])
                return [X,Y,New[2],New[3]]
    else:
        angle=0
        dmin=9999999
        B=False
        while angle<360:
            rx=[]
            ry=[]
            for x,y in zip(xs,ys):
                r=R2D2(x,y,angle)
                rx.append(r[0])
                ry.append(r[1])
            if func=='qua': Newc=qua(rx,ry)
            elif func=='cosh': Newc=cosh(rx,ry)
            else:
                print('Deu tudo errado no rq / digita a função certa')
                return False
            if isinstance(Newc,bool): newc=False
            else: newc=[Newc[0],Newc[1]]
            if not isinstance(newc,bool):
                d=distance(newc[0],newc[1])
                if d<dmin:
                    for j,p in zip(newc[0],newc[1]):
                        if (abs(rx[1]-j)<derro) and (abs(ry[1]-p)<derro):
                            good=True
                            break
                        else: good=False
                    if good:
                        if (abs(newc[0][0]-rx[0])<0.05) and (abs(newc[0][-1]-rx[-1])<0.05):
                            if (abs(newc[1][0]-ry[0])<0.05) and (abs(newc[1][-1]-ry[-1])<0.05):
                                dmin=d
                                an=angle
                                B=newc
                                AB=[Newc[2],Newc[3]]
            angle+=er
        X=[]
        Y=[]
        if isinstance(B,bool): return B
        else: 
            for x,y in zip(B[0],B[1]):
                R=R2D2(x,y,-an)
                X.append(R[0])
                Y.append(R[1])
            return [X,Y,AB[0],AB[1]]
    # retorna xs e ys passados pela função dada no melhor angulo possivel 

def distance(xs,ys):
    xa=xs[0]
    ya=ys[0]
    d=0
    for x,y in zip(xs,ys):
        a=x-xa
        b=y-ya
        d+=(((a**2)+(b**2))**(1/2))
        xa=x
        ya=y
    return d
    # retorna o comprimento da curva
    
def curves(px,py,auto,r,sa):
    X=[]
    Y=[]
    if auto:
        X=px
        Y=py
    else:
        aux=0
        while aux<3:
            print('Digite x',aux+1,':')
            X.append(float(input()))
            print('Digite y',aux+1,':')
            Y.append(float(input()))
            aux+=1
    return best(X,Y,r,sa)

def best(xs,ys,r,showall):
    # r = 'all': retorna todas as curvas num dicionario   /   'b': retorna a melhor curva   /   qualquer outra coisa: Não retorna nada e mostra os graficos
    # showall = if True: plota todas as curvas de um lado e a melhor do outro / se n plota só a melhor curva
    b={}
    Qr=rq(xs,ys,0.05,False,'qua',False)
    if isinstance(Qr,bool):
        dmin=99999999
        dminn='nenhum'
    else:
        b['Qr']={'values':[Qr[0],Qr[1]],'d':0,'a,b':[Qr[2],Qr[3]]}
        dmin=distance(Qr[0],Qr[1])
        dminn='Q'
    Q=qua(xs,ys)
    if isinstance(Q,bool): pass
    else: b['Q']={'values':[Q[0],Q[1]],'d':0,'a,b':[Q[2],Q[3]]}
    C=cosh(xs,ys)
    if isinstance(C,bool): pass
    else: b['C']={'values':[C[0],C[1]],'d':0,'a,b':[C[2],C[3]]}
    Qrt=rq(xs,ys,1,False,'qua',True)
    if isinstance(Qrt,bool): pass
    else: b['Qrt']={'values':[Qrt[0],Qrt[1]],'d':0,'a,b':[Qrt[2],Qrt[3]]}
    Cr=rq(xs,ys,1,False,'cosh',True)
    if isinstance(Cr,bool): pass
    else: b['Cr']={'values':[Cr[0],Cr[1]],'d':0,'a,b':[Cr[2],Cr[3]]}
    for c in b:
        v=b[c].get('values')
        d=distance(v[0],v[1])
        if d<=dmin:
            if (abs(xs[0]-v[0][0])<0.05) and (abs(xs[2]-v[0][-1])<0.05):
                if (abs(ys[0]-v[1][0])<0.05) and (abs(ys[2]-v[1][-1])<0.05):
                    dmin=d
                    B=v
                    Bab=b[c].get('a,b')
                    dminn=str(c)
    bel=quazier(xs,ys,False,True)
    b['bel']={'values':bel,'d':0,'a,b':'none'}
    if r=='b': return B
    elif r=='all': return [b,dminn]
    elif r=='bdx': return [B,Bab,dminn]
    else:
        if showall:
            fig=plt.figure()
            ax1=fig.add_subplot(121)
            ax2=fig.add_subplot(122)
            for c in b:
                v=b[c].get('values')
                ax1.plot(v[0],v[1],label=str(c))
                if c==dminn:
                    v=b[c].get('values')
                    ax2.plot(v[0],v[1])
            ax1.scatter(xs,ys)
            ax2.scatter(xs,ys)
            ax1.legend()
            ax1.set_title('all')
            ax2.set_title(str('best: '+str(dminn)))
            plt.show()
        else:
            for c in b:
                if c==dminn:
                    v=b[c].get('values')
                    plt.plot(v[0],v[1])
            plt.scatter(xs,ys)
            plt.show()

def pontos_aleatorios():
    xrand=[]
    yrand=[]
    auxiliar=0
    while auxiliar<3:
        xrand.append(random.randint(-30,30))
        yrand.append(random.randint(-30,30))
        auxiliar+=1
    print('\n\n\nXs:',xrand)
    print('Ys:',yrand)
    return [curves(xrand,yrand,True,'all',False),[xrand,yrand]]

'''
fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
while True:
    plt.ion()
    dick=pontos_aleatorios()
    b=dick[0][0]
    dminn=dick[0][1]
    xs=dick[1][0]
    ys=dick[1][1]
    for c in b:
        v=b[c].get('values')
        ax1.plot(v[0],v[1],label=str(c))
        if c==dminn:
            v=b[c].get('values')
            Abs=b[c].get('a,b')
            ax2.plot(v[0],v[1])
    ax1.scatter(xs,ys)
    ax1.scatter([-30,-30,30,30],[-30,30,-30,30])
    ax2.scatter([-30,-30,30,30],[-30,30,-30,30])
    ax2.scatter(xs,ys)
    ax1.legend()
    ax1.set_title('all')
    ax2.set_title(str('best: '+str(dminn)))
    #ax2.text(-30,30,str(abcs))
    plt.show()
    x=input()
    ax1.clear()
    ax2.clear()
    if x=='s': break
'''

#curves(1,1,False,'nada',True)
#'''


# não funfa com os pontos:
#  p1=(-6,22)
#  p2=(-1,23)
#  p3=(15,-18)
# não sei pq