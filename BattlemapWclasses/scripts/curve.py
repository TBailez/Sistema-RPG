import numpy as np
import cmath
import matplotlib.pyplot as plt
from findlin import lin

def guess(x1,x2,x3,b):
    if np.cosh(b*x2)==np.cosh(b*x1): b+=0.001
    return (np.cosh(b*x3)-np.cosh(b*x1))/(np.cosh(b*x2)-np.cosh(b*x1))
# calcula u baseado no guess de b

def findtit(a,b,c,d):
    u=((a*c)+(b*d))/((((c**2)+(d**2))**(1/2))*(((a**2)+(b**2))**(1/2)))
    t=np.arccos(u)
    # retorna o angulo entre 2 vetores
    return t

def R2D2(x,y,a):
    a=np.radians(a)
    e=np.exp((complex(0,1))*a)
    newp=complex(x,y)*e
    return [newp.real,newp.imag]
    #Complex 2D Rotation (roda um ponto(counterclockwise) em relação a origem com un angulo dado)
    # Rotation 2 D Rotation = R2D2

def coshka(xs,ys):
    x1=xs[0]
    x2=xs[1]
    x3=xs[2]
    y1=ys[0]
    y2=ys[1]
    y3=ys[2]
    u=(y3-y1)/(y2-y1)
    f0=(guess(x1,x2,x3,0))
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
    #returns a,b,c pra função cosh

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
        return [X,y]

def abcs(xs,ys):
    x1=xs[0]
    x2=xs[1]
    x3=xs[2]
    y1=ys[0]
    y2=ys[1]
    y3=ys[2]
    tit=x2+x1
    t=(y2-y1)/(x2-x1)
    a=(y3-(t*x3)-y1+(x1*t))/((x3**2)-(x3*tit)-(x1**2)+(x1*tit))
    b=(y2-y1-(a*((x2**2)-(x1**2))))/(x2-x1)
    c=y1-(a*(x1**2))-(b*x1)
    # returns a,b,c da função quadratica normal
    return [a,b,c]

def qua(xs,ys):
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
    if (xs[1]>xs[0] and xs[1]>xs[-1]) or (xs[1]<xs[0] and xs[1]<xs[-1]): return [y,QX]
    else: return [QX,y]

def gettit(X,Y,er,teste):
    tit=0
    tits=[]
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
        # returns uma lista com todas as listas de x,y cada um rotacionado com a(angulo anterior + er) até o titf
        return [xs,ys]
    else:
        for x,y in zip(X,Y):
            r2d2=R2D2(x,y,titf)
            newx.append(r2d2[0])
            newy.append(r2d2[1])
        # returns x,y rotacionados com um angulo t(de tal forma q a derivada da função, que foi criada a partir desses pontos, é igual a 0 no x do meio), e o angulo t
        return [newx,newy,titf]

def rq(xs,ys,er,teste,func):
    if func=='qua':
        xys=gettit(xs,ys,er,teste)
        if teste:
            for a,b in zip(xys[0],xys[1]):
                tp=qua(a,b)
                plt.plot(tp[0],tp[1])
            plt.show()
        else:
            x=xys[0]
            y=xys[1]
            new=qua(x,y)
            X=[]
            Y=[]
            for a,b in zip(new[0],new[1]):
                n=R2D2(a,b,xys[-1]*(-1))
                X.append(n[0])
                Y.append(n[1])
            return [X,Y]
    elif func=='cosh':
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
            newc=cosh(rx,ry)
            if not isinstance(newc,bool):
                d=distance(newc[0],newc[1])
                if d<dmin:
                    if (abs(newc[0][0]-rx[0])<0.05) and (abs(newc[0][-1]-rx[-1])<0.05):
                        if (abs(newc[1][0]-ry[0])<0.05) and (abs(newc[1][-1]-ry[-1])<0.05):
                            dmin=d
                            an=angle
                            B=newc
            angle+=er
        X=[]
        Y=[]
        if isinstance(B,bool): return B
        else: 
            for x,y in zip(B[0],B[1]):
                R=R2D2(x,y,-an)
                X.append(R[0])
                Y.append(R[1])
            return [X,Y]
    else: print('deu tudo errado')

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
    

def curve(px,py,co):
    X=[]
    Y=[]
    if co==1:
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
    best(X,Y,True,False)

def best(xs,ys,showall,r):
    b={}
    Q=qua(xs,ys)
    b['Q']={'values':Q,'d':0}
    dmin=distance(Q[0],Q[1])
    dminn='Q'
    C=cosh(xs,ys)
    if isinstance(C,bool): pass
    else: b['C']={'values':C,'d':0}
    #B=rquad(xs,ys)
    #b['B']={'values':B,'d':0}
    Qr=rq(xs,ys,0.01,False,'qua')
    b['Qr']={'values':Qr,'d':0}
    Qrc=rq(xs,ys,1,False,'cosh')
    if isinstance(Qrc,bool): pass
    else: b['Qrc']={'values':Qrc,'d':0}
    for c in b:
        v=b[c].get('values')
        d=distance(v[0],v[1])
        if d<=dmin:
            if (abs(xs[0]-v[0][0])<0.05) and (abs(xs[2]-v[0][-1])<0.05):
                if (abs(ys[0]-v[1][0])<0.05) and (abs(ys[2]-v[1][-1])<0.05):
                    dmin=d
                    B=v
                    dminn=str(c)
    if r: return B
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

    
curve(1,1,0)


        




