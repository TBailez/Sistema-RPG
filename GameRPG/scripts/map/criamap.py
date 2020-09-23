from scripts.map.boulder import pedra
import random
from data.classes import Pedra
from data.classes import Arvore

def criapedras(tamanho,quantidade,initial_position,overlap=True):
    aux=0
    ini=initial_position
    l=[]
    x=random.randint(-100,tamanho[0])
    y=random.randint(-100,tamanho[1])
    p=pedra([x,y],random.randint(15,35),random.randint(2,4))
    l.append([p[0],p[1],p[2],p[3]])
    while aux<quantidade:
        while True:
            x=random.randint(-100,tamanho[0]+100)
            y=random.randint(-100,tamanho[1]+100)
            teste=False
            if (x<ini[0]) or (x>ini[1]):
                if (y<ini[2]) or (y>ini[3]):
                    teste=True
            if teste: break
        p=pedra([x,y],random.randint(15,35),random.randint(2,4))
        if overlap: foi=True
        else:
            foi=False
            for P in l:
                if ((l.index(P))==(len(l)-1)): pass
                else: pass
                xt=abs(P[3][0]-p[3][0])
                yt=abs(P[3][1]-p[3][1])
                D=(((xt**2)+(yt**2))**(1/2))
                if D>(P[2]+p[2]): foi=True
                else:
                    foi=False
                    break
        if foi:
            l.append([p[0],p[1],p[2],p[3]])
            aux+=1
    newl=[]
    for p in l:
        lista=[]
        for x,y in zip(p[0],p[1]): lista.append([x,y])
        newl.append(Pedra(p[3],lista,p[2]))
    return newl

def convert(lx,p):
    a=2/(p[1]-p[0])
    b=((-1)-(p[0]*a))
    newx=[]
    for x in lx: newx.append(x*a+b)
    return newx

def criaarvores(tamanho,quantidade,initial_position):
    ini=initial_position
    a=15
    pop=[]
    while a<=40:
        pop.append(a)
        a+=0.5
    newx=convert(pop,[pop[0],pop[-1]])
    chan=[]
    for j in newx:
        chan.append((2.7182**(-3.125*((j/1.2)**2))))
    ar=random.choices(pop,weights=chan,k=quantidade)
    arv=[]
    for A in ar:
        while True:
            x=random.randint(-100,tamanho[0]+100)
            y=random.randint(-100,tamanho[1]+100)
            teste=False
            if (x<ini[0]) or (x>ini[1]):
                if (y<ini[2]) or (y>ini[3]):
                    teste=True
            if teste: break
        arv.append(Arvore([x,y],A))
    return arv

def mapa(tamanho,tipo,initial_position,overlap=True):
    if tipo=='floresta 1':
        ps=criapedras(tamanho,random.randint(3,10),initial_position,overlap)
        ars=criaarvores(tamanho,random.randint(25,40),initial_position)
        return {'pedras':ps,'arvores':ars}