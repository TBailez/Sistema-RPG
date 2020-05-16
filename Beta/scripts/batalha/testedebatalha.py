import json
from .combates.melee import melee
from .combates.magical import magical

def batalha():
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)
    
    n=[]
    v=[]
    i=[]
    a=[]
    q=[]
    auxq=[]
    v2=[]
    a2=[]
    print('Npc list:')
    for npc in npcs:
        print('  ',npc)
    while True:
        NPC=input('Quais npcs estaram no combate?(para não adicionar mais npcs digite exit)\n')
        if NPC in npcs: 
            n.append(NPC)
            u=(npcs.get(NPC).get('velocidade'))
            u2=(2.71828**((0.0423*u+0.0423)))
            v.append(u)
            v2.append(u)
            i.append(u2)
            a.append(u2)
            q.append(int(u2))
            a2.append(int(u2))
            auxq.append(int(u2))
        elif NPC.lower()=='exit': break
        else: print('Não existe esse npc')
    u=0
    u2=0
    for z in nomes: 
        n.append(z)
        u=nomes.get(z).get('velocidade')
        u2=(2.71828**((0.0423*u+0.0423)))
        v.append(u)
        v2.append(u)
        i.append(u2)
        a.append(u2)
        q.append(int(u2))
        a2.append(int(u2))
        auxq.append(int(u2))
    u=0
    u2=0
    v.sort(reverse=True)
    x='s'
    aux=2
    print('Combatentes:',n)
    na='0'
    while x=='s':
        while u2<(len(n)):
            while u<(len(n)):
                if v[u2]==v2[u] and not n[u]==na:
                    while True:
                        #ve oq q faz com isso aqui
                        print('vez de',n[u],'atacar')
                        TdC=input('Qual o tipo de combate?\n')
                        if TdC=='me':
                            nomedef=melee(n[u],q[u],n)
                            if nomedef in nomes:
                                with open('Beta/data/nomes.json') as j:
                                    nomesm=json.load(j)
                                nomes[nomedef]['hp']=nomesm.get(nomedef).get('hp')
                            else: 
                                with open('Beta/data/npcs.json') as h:
                                    npcsm=json.load(h)
                                npcs[nomedef]['hp']=npcsm.get(nomedef).get('hp')
                            break
                        elif TdC=='ma':
                            nomedef=magical(n[u],q[u],n)
                            if nomedef in nomes:
                                with open('Beta/data/nomes.json') as j:
                                    nomesm=json.load(j)
                                nomes[nomedef]['hp']=nomesm.get(nomedef).get('hp')
                            else: 
                                with open('Beta/data/npcs.json') as h:
                                    npcsm=json.load(h)
                                npcs[nomedef]['hp']=npcsm.get(nomedef).get('hp')
                            break
                        else: print('Não existe essa opção')
                    na=n[u]
                    break
                else: u+=1
            u=0
            u2+=1
        u2=0
        while u<(len(n)):
            a[u]=i[u]*aux
            q[u]=int(a[u])-int(a2[u])
            a2[u]=a[u]
            auxq[u]=q[u]
            u+=1
        u=0
        auxq.sort()
        while u<(len(n)):
            q[u]-=(auxq[0]-1)
            u+=1
        aux+=1
        u=0
        x=input('Deseja continuar o combate?')
    return(n)