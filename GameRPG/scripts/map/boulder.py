import random
import numpy as np
import matplotlib.pyplot as plt
import cmath

def lin(x,y,xt,yt,c):
    if c==1:
        x1=x
        x2=xt
        y1=y
        y2=yt
    else:
        x1=int(input('x1:'))
        x2=int(input('x2:'))
        y1=int(input('y1:'))
        y2=int(input('y2:'))
    a=(y2-y1)/(x2-x1)
    b=y1-(x1*a)
    if not c==1: print('Deu certo, a=',a,'b=',b)
    else: return [a,b]

def convert(lx,ab):
    newx=[]
    for x in lx: newx.append(x*ab[0]+ab[1])
    return newx

def prob(x): return (2.7182**(-3.125*((x/1.2)**2)))

def R2D2(d,a):
    a=np.radians(a)
    e=np.exp((complex(0,1))*a)
    p=complex(d,0)*e
    return [p.real,p.imag]

def RoundProx(xs,ys,co):
    newx=[]
    newy=[]
    for x,y in zip(xs,ys):
        d=((x**2)+(y**2))**(1/2)
        i=xs.index(x)
        if i==(len(xs)): ip==0
        else: ip=i+1
        d2=((xs[ip]**2)+(ys[ip]**2))**(1/2)
        d3=((xs[i-1]**2)+(ys[i-1]**2))**(1/2)
        d4=d-((d2+d3)/2)
        sin=y/d
        cos=x/d
        newx.append(cos*(d-(d4*co)))
        newy.append(sin*(d-(d4*co)))
    return [newx,newy]

def pedra(centro,tamanho,qual=2):
    nump=random.randint(16,28)
    ds=np.linspace(2,8)
    newx=convert(ds,lin(ds[0],-1,ds[-1],1,1))
    p=[]
    for xis in newx: p.append(prob(xis))
    distances=random.choices((ds),weights=(p),k=nump)
    tits=360/nump
    si=0
    x=[]
    y=[]
    for a in distances:
        xy=R2D2(a,si)
        x.append(xy[0])
        y.append(xy[1])
        si+=tits
    x.append(distances[0])
    y.append(0)
    D=distances
    D.sort()
    md=D[0]
    if qual==1: newlist=[x,y]
    if qual==2: newlist=RoundProx(x,y,0.2)
    if qual==3: newlist=RoundProx(x,y,0.6)
    if qual==4:
        times=random.randint(3,8)
        aux=0
        newwlist=RoundProx(x,y,0.35)
        while aux<times:
            newlist=RoundProx(newwlist[0],newwlist[1],0.35)
            aux+=1
    X=[]
    Y=[]
    xs=[]
    ys=[]
    multi=(tamanho/md)*0.85
    for j,p in zip(newlist[0],newlist[1]):
        xs.append(j*multi)
        ys.append(p*multi)
    D=((xs[0]**2)+(ys[0])**2)**(1/2)
    for u,l in zip(xs,ys):
        d=(((u**2)+(l**2))**(1/2))
        if d>D: D=d
    for x,y in zip(xs,ys):
        X.append(x+centro[0])
        Y.append(y+centro[1])
    return [X,Y,D,centro]