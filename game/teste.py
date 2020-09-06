import matplotlib.pyplot as plt
import numpy as np


v1=[1,1]
v2=[1,0]
a=np.arccos(((v1[0]*v2[0])+(v1[1]*v2[1]))/((((v1[0]**2)+(v1[1]**2))**(1/2))*(((v2[0]**2)+(v2[1]**2))**(1/2))))
print('a:',np.degrees(a))

'''
fig=plt.figure()
ax=fig.add_subplot(111)
c=[5,6]
p=[7,10]
t=3
ax.add_artist(plt.Circle(tuple(c),t,fill=False))
if c[0]==p[0]:
    if p[1]>c[1]: P=[c[0],c[1]+t]
    else: P=[c[0],c[1]-t]
else:
    a=(c[1]-p[1])/(c[0]-p[0])
    b=c[1]-(a*c[0])
    x1=(t/((1+(a**2))**(1/2)))+c[0]
    x2=-(t/((1+(a**2))**(1/2)))+c[0]
    p1=[x1,((x1*a)+b)]
    p2=[x2,((x2*a)+b)]
    if (p[0]-c[1])>0:
        if p1[0]>p2[0]: P=p1
        else: P=p2
    else:
        if p1[0]<p2[0]: P=p1
        else: P=p2

ax.plot([c[0],p[0]],[c[1],p[1]])
ax.scatter(P[0],P[1])
plt.show()
'''