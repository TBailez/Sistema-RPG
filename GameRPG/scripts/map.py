from scripts.boulder import pedra
import random

def mapa(tamanho,tipo):
    if tipo=='floresta 1':
        aux=0
        l=[]
        x=random.randint(0,tamanho[0])
        y=random.randint(0,tamanho[1])
        p=pedra([x,y],30,70,random.randint(1,4))
        l.append([p[0],p[1]])
        teste=0
        while (aux<10) and (teste<50):
            x=random.randint(0,tamanho[0])
            y=random.randint(0,tamanho[1])
            p=pedra([x,y],30,70,random.randint(1,4))
            foi=True#False
            for P in l:
                if ((l.index(P))==(len(l)-1)): pass
                else: pass
                '''
                xt=abs(P[3][0]-p[3][0])
                yt=abs(P[3][1]-p[3][1])
                D=(((xt**2)+(yt**2))**(1/2))
                if D>(P[2]+p[2]): foi=True
                else:
                    foi=False
                    break
                '''
            if foi:
                l.append([p[0],p[1]])
                aux+=1
            teste+=1
    return l

