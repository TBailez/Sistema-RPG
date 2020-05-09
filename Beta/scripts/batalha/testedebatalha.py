import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def batalha():
    non={}
    n=[]
    v=[]
    i=[]
    a=[]
    q=[]
    v2=[]
    q2=[]
    auxi=1
    print('Npc list:')
    for npc in npcs:
        print('  ',npc)
    while True:
        NPC=input('Quais npcs estaram no combate?(para não adicionar mais npcs digite exit)')
        if NPC in npcs: 
            n.append(NPC)
            u=(npcs.get(NPC).get('velocidade'))
            u2=(2.71828**((0.0423*u+0.0423)))
            v.append(u)
            v2.append(u)
            i.append(u2)
            a.append(u2)
            q.append(int(u2))
        elif NPC.lower()=='exit': break
        else: print('Não existe esse npc')
    u=0
    u2=0
    for z in nomes: 
        n.append(z)
        print(nomes)
        u=nomes.get(z).get('velocidade')
        u2=(2.71828**((0.0423*u+0.0423)))
        v.append(u)
        v2.append(u)
        i.append(u2)
        a.append(u2)
        q.append(int(u2))
    u=0
    u2=0
    v.sort(reverse=True)
    x=1
    print('Combatentes:',n)
    while x>0:
        while u<(len(n)):
            a[u]+=(i[u]-q[u])
            u+=1
        u=0
        while u2<(len(n)):
            while u<(len(n)):
                if v[u2]==v2[u]:
                    print("Vez de",n[u],"atacar",q[u],"vez(es)")
                    quanti=0
                    while quanti<q[u]:
                        while True:
                            nomedef=input('Qual o nome do defensor?\n')
                            if nomedef in n: break
                            else: print('burro esse nome n existe')
                        d1=int(input("dado atk:"))
                        d2=int(input("dado def:"))
                        dd=(d1-d2)
                        if n[u] in nomes: non=nomes.copy()
                        else: non=npcs.copy()
                        f=int(non.get(n[u]).get('forca'))
                        f=int(non.get(n[u]).get('forca'))
                        ba=int(non.get(n[u]).get('inventario').get('arma'))
                        qva=dd+int(non.get(n[u]).get('velocidade'))
                        if nomedef in nomes: non=nomes.copy()
                        else: non=npcs.copy()
                        f2=int(non.get(nomedef).get('forca'))
                        ba2=int(non.get(nomedef).get('inventario').get('arma'))
                        qa=f+ba+dd
                        qd=int(non.get(nomedef).get('resistencia'))+int(non.get(nomedef).get('inventario').get('armadura'))
                        dano=qa-qd
                        desvio=qva-int(non.get(nomedef).get('velocidade'))
                        pa=qa-(f2+ba2)
                        if d1==20: dano=dano*2
                        if d2==20: int(dano=dano/2)
                        print("Se tentar bloquear:\n Dano =",dano,'\nSe tentar desviar:')
                        if desvio<=0:
                            print(" Desvio")
                        else:
                            print(" Dano=",int(dano*1.5),"(x1,5)")
                        print('Se tentar parrear:')
                        if pa<0 and desvio<0:
                            if (pa+desvio)<=(-5): print(' Parry perfeito')
                            else: print(' Parry inperfeito')
                        else:
                            print(' Dano=',dano+int(non.get(nomedef).get('inventario').get('armadura')))
                        quanti=quanti+1
                    break
                else: u+=1
            u=0
            u2+=1
        u2=0
        while u<(len(n)):
            q[u]=int(a[u])
            if auxi==1:
                q2.insert(u,int(a[u]))
            else:
                q2[u]=int(a[u])
            u+=1
        auxi=auxi-1
        u=0
        q2.sort()
        while u<(len(n)):
            q[u]=q[u]-((q2[0])-1)
            u=u+1
        u=0
        x=int(input('Quer continuar o combate?(1=s)'))
    