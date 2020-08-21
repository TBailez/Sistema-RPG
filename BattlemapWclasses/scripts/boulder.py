import matplotlib.pyplot as plt
import random
import numpy as np

def lin(x,y,xt,yt,c):
    # retorna uma lista com A e B de uma função linear q converte um intervalo de x em outro
    # exp: eu quero q de x=2 a x=5 vire x=-1 a x=1 para botar em outro função depois
    # a função faz essa conta: e ve quais são os valores de a e b pra isso funfar
    #          2*A+B=-1
    #          5*A+B=1
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
    #converte todos os x da lista lx em novos x de acordo com uma função linear q usa A e B
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

def demo():
    plt.ion()
    fig=plt.figure()
    ax1=fig.add_subplot(221)
    ax2=fig.add_subplot(222)
    ax3=fig.add_subplot(223)
    ax4=fig.add_subplot(224)
    while True:
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
            xy=xys(a,si)
            x.append(xy[0])
            y.append(xy[1])
            si+=tits
        x.append(distances[0])
        y.append(0)
        ax1.fill(x,y,'gray')
        ax1.set_title('Circle-Based')
        newlist=RoundProx(x,y,0.2)
        ax2.fill(newlist[0],newlist[1],'gray')
        ax2.set_title('CB rounded(20%)')
        newlist=RoundProx(x,y,0.6)
        ax3.fill(newlist[0],newlist[1],'gray')
        ax3.set_title('CB rounded(80%)')
        times=7
        aux=0
        while aux<2:
            if aux==0: newlist=RoundProx(x,y,0.2)
            else: newwlist=RoundProx(newlist[0],newlist[1],0.35)
            aux+=1
        ax4.fill(newwlist[0],newwlist[1],'gray')
        string=str('CB '+str(times)+'-rounded(35%)')
        ax4.set_title(string)
        plt.draw()
        g=input()
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax3.clear()
        ax4.clear()
        if g=='stop': break

demo()