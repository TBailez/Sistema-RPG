import matplotlib.pyplot as plt
import random
import numpy as np
import cmath
from curve2 import curve


aux=0
X=[]
Y=[]
while aux<3:
    print('Digite x',aux+1,':')
    X.append(float(input()))
    print('Digite y',aux+1,':')
    Y.append(float(input()))
    aux+=1
C=curve(X,Y)
plt.plot(C[0],C[1])
plt.scatter(X,Y)
plt.scatter(C[2],C[3])
plt.show()



'''
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

auxiliar=0
xrand=[1,2,3]
yrand=[1,2,1]

#while auxiliar<3:
#    xrand.append(random.randint(-30,30))
#    yrand.append(random.randint(-30,30))
#    auxiliar+=1


a=0
newx=[]
newy=[]
while a<360:
    R=R2D2(xrand,yrand,a)
    newx=R[0]
    newy=R[1]
    aux=1
    for x,y in zip(newx,newy):
        if aux==1: n=str('a'+str(a))
        if aux==2: n=str('b'+str(a))
        if aux==3: n=str('c'+str(a))
        #plt.text(x,y,n)
        aux+=1
    plt.plot(newx,newy)
    a+=3
#plt.scatter([-30,-30,30,30],[-30,30,-30,30])
plt.show()
'''





'''
X=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
a1=random.randint(-3,3)
a2=random.randint(-3,3)
b1=random.randint(-3,3)
b2=random.randint(-3,3)
Y1=[]
Y2=[]
Y3=[]
for x in X:
    Y1.append((x*a1)+b1)
    Y2.append((x*a2)+b2)
    Y3.append((x*((a1+a2)/2))+((b1+b2)/2))
print('X:',X)
print('Y1:',Y1)
print('Y2:',Y2)
print('Y3:',Y3)
plt.plot(X,Y1)
plt.plot(X,Y2)
plt.plot(X,Y3)
plt.show()
'''

'''

auxiliar=0
xrand=[0,1,1.5]
yrand=[-1.9,-2.4,-0.325]

#while auxiliar<3:
#    xrand.append(random.randint(-30,30))
#    yrand.append(random.randint(-30,30))
#    auxiliar+=1

a=3.1
b=-3.6
c=-1.9

aux=0
while aux<2:
    if aux==0:
        p=xrand[0]
        p2=yrand[0]
    if aux==1:
        p=xrand[2]
        p2=yrand[2]
    a2=(2*a*p)+b
    b2=-((p*a2)-p2)
    xdx1=p-1
    xdx2=p+1
    ydx1=(xdx1*a2)+b2
    ydx2=(xdx2*a2)+b2
    plt.plot([xdx1,xdx2],[ydx1,ydx2])
    aux+=1
X=np.linspace(xrand[0],xrand[-1])
Y=[]
for x in X: Y.append(((a)*(x**2))+(b*x)+c)
plt.plot(X,Y)
plt.scatter(xrand,yrand)
plt.show()
'''
