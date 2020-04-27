n=[]
v=[]
i=[]
a=[]
q=[]
v2=[]
j=0
ma=25
me=1
u=0
u2=0
a=(2/(ma-me))
b=((-ma-me)/(ma-me))
qj=int(input("Quantos combatentes: "))
while j<qj:
    print("Nome do combatente ",j+1,": ")
    nx=str(input(""))
    v1=int(input("Sua velocidade: "))
    n.insert(j,nx)
    v.insert(j,v1)
    i.insert(j,(2.71828**((0.0423*v1)+0.0423)))
    q.insert(j,(int(i[j])))
    v2.insert(j,v[j])
    j=j+1
a=i
print("v: ",v,"v2: ",v2)
#i.sort(reverse=True)
v.sort(reverse=True)
#print("i: ",i,"q: ",q,"a: ",a)
print("v: ",v,"v2: ",v2)
x=int(input("Numero de rodadas: "))
while x>0:
    while u<qj:
        a[u]=a[u]+(i[u]-q[u])
        u=u+1
    u=0
    #print("a: ",a)
    while u2<qj:
        while u<qj:
            if v[u2]==v2[u]:
                print(" ",n[u]," x",q[u])
            u=u+1
        u=0
        u2=u2+1
    u2=0
    while u<qj:
        q[u]=int(a[u])
        u=u+1
    u=0
    x=x-1
    print("\n")
