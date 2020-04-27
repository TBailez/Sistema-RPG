n=[]
v=[]
i=[]
a=[]
q=[]
v2=[]
q2=[]
j=0
u=0
u2=0
aux=1
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
    a.insert(j,(2.71828**((0.0423*v1)+0.0423)))
    j=j+1
v.sort(reverse=True)
x=int(input("Numero de rodadas: "))
while x>0:
    while u<qj:
        a[u]=a[u]+(i[u]-q[u])
        u=u+1
    u=0
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
        if aux==1:
            q2.insert(u,int(a[u]))
        else:
            q2[u]=int(a[u])
        u=u+1
    aux=aux-1
    u=0
    q2.sort()
    while u<qj:
        q[u]=q[u]-((q2[0])-1)
        u=u+1
    u=0
    x=x-1
    print("\n")
