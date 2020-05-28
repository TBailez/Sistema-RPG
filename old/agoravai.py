import matplotlib.pyplot as plt
from random import randint
import numpy as np

plt.ion()

'''
#Let's generate some random X, Y data X = [ [frst group],[second group] ...]
X = [ [randint(0,50) for i in range(0,5)] for i in range(0,24)]
Y = [ [randint(0,50) for i in range(0,5)] for i in range(0,24)]
print('x:',X)
print('y:',Y)
labels = range(1,len(X)+1)
'''
fig = plt.figure()
ax = fig.add_subplot(111)
X=[[1],[2],[3]]
Y=[[4],[5],[6]]
xl=[]
yl=[]
for a,b in zip(X,Y):
    xl.append(a[0])
    yl.append(b[0])
xl.sort(reverse=True)
yl.sort(reverse=True)
if xl[0]-xl[-1]<yl[0]-yl[-1]: dm=yl[0]-yl[-1]
else: dm=xl[0]-xl[-1]
ax.set_xlim(xl[-1]-2,xl[-1]+2+dm)
ax.set_ylim(yl[-1]-2,yl[-1]+2+dm)
labels=['jplup','tom','von karma']
for x,y,lab in zip(X,Y,labels):
    ax.scatter(x,y,label=lab)
plt.legend()
plt.show()
sair=False
while True:
    while True:
        m=input('Digite qual personagem deve mudar de lugar:')
        if m in labels: break
        elif m=='b':
            sair=True
            break
        else: print('Esse nome não existe')
    if sair: break
    xy=input('Digite x y:')
    xys=xy.split(sep=' ')
    inn=labels.index(m)
    X[inn][0]=float(xys[0])
    Y[inn][0]=float(xys[1])
    print('X:',X)
    print('Y:',Y)
    ax.clear()
    for x,y,lab in zip(X,Y,labels):
        ax.scatter(x,y,label=lab)
    ax.legend()
    ax.set_xlim(xl[-1]-2,xl[-1]+2+dm)
    ax.set_ylim(yl[-1]-2,yl[-1]+2+dm)
    fig.canvas.draw()
    fig.canvas.flush_events()