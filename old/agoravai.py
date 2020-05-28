import matplotlib.pyplot as plt
plt.ion()
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
        elif m=='exit':
            sair=True
            break
        else: print('Esse nome não existe')
    if sair: break
    while True:
        while True:
            xy=input('Digite x y:')
            xys=xy.split(sep=' ')
            if len(xys)==2:
                try: newx=float(xys[0])
                except ValueError:
                    print('X digitado não é um numero')
                    sair=False
                else:
                    try: newy=float(xys[1])
                    except ValueError:
                        print('Y digitado não é um numero')
                        sair=False
                    else: sair=True
            else: print('Digite: x-espaço-y')
            if sair: break
        aux=0
        while aux<len(X):
            if X[aux][0]==float(xys[0]) and Y[aux][0]==float(xys[1]):
                print('Erro, já existe um personagem nesse lugar')
                sair=False
                break
            sair=True
            aux+=1
        if sair: break
    inn=labels.index(m)
    X[inn][0]=float(xys[0])
    Y[inn][0]=float(xys[1])
    ax.clear()
    for x,y,lab in zip(X,Y,labels):
        ax.scatter(x,y,label=lab)
    ax.legend()
    ax.set_xlim(xl[-1]-2,xl[-1]+2+dm)
    ax.set_ylim(yl[-1]-2,yl[-1]+2+dm)
    fig.canvas.draw()
    fig.canvas.flush_events()
    sair=False

print('Teste')
input()