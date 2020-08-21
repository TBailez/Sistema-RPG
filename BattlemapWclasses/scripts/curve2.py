import numpy as np
import cmath
import matplotlib.pyplot as plt
import random
from bezier import quazier

def guess(x1,x2,x3,b):
    if np.cosh(b*x2)==np.cosh(b*x1): b+=0.0001
    return (np.cosh(b*x3)-np.cosh(b*x1))/(np.cosh(b*x2)-np.cosh(b*x1))
    # calcula u baseado no guess de b

def R2D2(X,Y,a):
    newx=[]
    newy=[]
    a=np.radians(a)
    e=np.exp((complex(0,1))*a)
    for x,y in zip(X,Y):
        newp=complex(x,y)*e
        newx.append(newp.real)
        newy.append(newp.imag)
    return [newx,newy]
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
    if ((xs[1]>xs[0] and xs[1]>xs[-1]) or (xs[1]<xs[0] and xs[1]<xs[-1])):
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

def getSS(xs,ys,a,b,f):
    sx=[]
    sy=[]
    for x,y in zip(xs,ys):
        if f=='qua': a2=(2*a*x)+b
        else: a2=a*(b*(np.sinh(b*x)))
        b2=((2*a2*x)-y)*(-1)
        newx=x-0.01
        sx.append(newx)
        sy.append(((newx*2)*a2)+b2)
    return [sx,sy]


def Rcurve(xs,ys,func):
    # xs = 3 x dos pontos
    # ys = 3 y dos pontos
    # func = qual função será usada (ax^2+bx+c ou a*cosh(bx)+c)
    de1=distance([xs[0],xs[1]],[ys[0],ys[1]])
    de2=distance([xs[1],xs[2]],[ys[1],ys[2]])
    if de1<de2: derro=de1/3
    else: derro=de2/3
    angle=0
    dmin=9999999
    B=False
    while angle<360:
        rp=R2D2(xs,ys,angle)
        rx=rp[0]
        ry=rp[1]
        if func=='qua': newc=qua(rx,ry)
        if func=='cosh': newc=cosh(rx,ry)
        if isinstance(newc,bool): pass
        else:
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
                            sxy=getSS(rx,ry,newc[2],newc[3],func)
        angle+=1
    if isinstance(B,bool): return B
    else:
        R=R2D2(B[0],B[1],-an)
        Rs=R2D2(sxy[0],sxy[1],-an)
        return [R[0],R[1],Rs[0],Rs[1],dmin]
    # retorna xs e ys passados pela função dada no melhor angulo possivel 

def curve(xs,ys):
    Qr=Rcurve(xs,ys,'qua')
    Cr=Rcurve(xs,ys,'cosh')
    if isinstance(Qr,bool):
        print('Cr')
        return Cr
    if isinstance(Cr,bool):
        print('Qr')
        return Qr
    if Qr[-1]<Cr[-1]:
        print('Qr')
        return Qr
    else:
        print('Cr')
        return Cr