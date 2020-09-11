import random
import numpy as np

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

def prob(x): return (2.7182**(-3.125*((x/1.2)**2)))*10

def xys(d,an):
    numt=0
    while an>90:
        numt+=1
        an-=90
    s=np.sin(np.radians(an))
    c=np.cos(np.radians(an))
    x3=c*d
    y3=s*d
    if numt==1: return [-y3,x3]
    if numt==2: return [-x3,-y3]
    if numt==3: return [y3,-x3]
    if numt==0: return [x3,y3]

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

def pedra(centro,mint,maxt,qual=2,minp=6,maxp=30):
    nump=random.randint(minp,maxp)
    ds=np.linspace(mint,maxt)
    newx=convert(ds,lin(ds[0],-1,ds[-1],1,1))
    p=[]
    for xis in newx: p.append(prob(xis))
    distances=random.choices((ds),weights=(p),k=nump)
    D=distances
    D.sort()
    md=D[0]
    tits=360/nump
    si=0
    x=[]
    y=[]
    for a in distances:
        xy=xys(a,si)
        x.append(xy[0])
        y.append(xy[1])
        si+=tits
    x.append(distances[0])
    y.append(0)
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
    for x,y in zip(newlist[0],newlist[1]):
        X.append(x+centro[0])
        Y.append(y+centro[1])
    return [X,Y,md,centro]