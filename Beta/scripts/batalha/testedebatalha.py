import json
from .combates.melee import melee
from .combates.magical import magical

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def batalha():
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
                    while True:
                        TdC=input('Qual o tipo de combate?')
                        if TdC=='me':
                            melee(n[u],q[u],n)
                            break
                        elif TdC=='ma':
                            magical(n[u],q[u],n)
                            break
                        else: print('Não existe essa opção')
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
    