import numpy as np
import matplotlib.pyplot as plt

def quazier(xs,ys,s,au):
    # xs = os xs dos pontos
    # ys = os ys dos pontos
    # s = if True: plota a curva / se n n
    # au = if True: usa os xs e ys dados / se n vc tem q digitar cada ponto
    if au:
        p1=np.array([xs[0],ys[0]])
        p2=np.array([xs[1],ys[1]])
        p3=np.array([xs[2],ys[2]])
        if len(xs)==4: p4=np.array([xs[3],ys[3]])
    else:
        aux=0
        X=[]
        Y=[]
        while aux<4:
            print('Digite x',aux+1,':')
            if aux==3:
                print('Se não quiser outro ponto digite n')
                X4=input()
            else: X4=float(input())
            if X4=='n': break
            else: X.append(float(X4))
            print('Digite y',aux+1,':')
            Y.append(float(input()))
            aux+=1
        p1=np.array([X[0],Y[0]])
        p2=np.array([X[1],Y[1]])
        p3=np.array([X[2],Y[2]])
        if len(X)==4: p4=np.array([X[3],Y[3]])
        xs=X
        ys=Y
    Q1=[]
    Q2=[]
    x=[]
    y=[]
    t=0
    while t<1.01:
        l1=(((1-t)*p1)+(t*p2))
        l2=(((1-t)*p2)+(t*p3))
        q1=(((1-t)*l1)+(t*l2))
        if len(xs)==3:
            x.append(q1[0])
            y.append(q1[1])
        else:
            l3=(((1-t)*p3)+(t*p4))
            q2=(((1-t)*l2)+(t*l3))
            Q=(((1-t)*q1)+(t*q2))
            Q1.append(Q[0])
            Q2.append(Q[1])
        t+=0.01
    if s:
        if len(xs)==4: plt.plot(Q1,Q2)
        else: plt.plot(x,y)
        plt.scatter(xs,ys)
        plt.show()
    if len(xs)==4: return [Q1,Q2]
    else: return [x,y]
    # returns uma bezier curve baseada em 3 ou 4 pontos

# se quiser rodar só esse script tira a # da linha 63
#quazier(1,1,True,False)