import json
from .combates.melee import melee
from .combates.magical import magical
from .combatentes import createcombatentes
from ..funcoes.useit import useitem

def batalha():
    createcombatentes()
    with open('Beta/data/combatentes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/inventario/armas.json') as h:
        armas=json.load(h)

    with open('Beta/data/inventario/armadura.json') as p:
        armadura=json.load(p)
    
    with open('Beta/data/inventario/escudos.json') as q:
        escudos=json.load(q)

    n=[]
    v=[]
    i=[]
    a=[]
    q=[]
    auxq=[]
    v2=[]
    a2=[]
    for z in nomes:
        dva=nomes.get(z).get('inventario').get('arma')
        dvam=nomes.get(z).get('inventario').get('armadura')
        dve=nomes.get(z).get('inventario').get('escudo')
        if dva in armas: dvat=armas.get(dva).get('int_VEL')
        else: dvat=0
        if dvam in armadura: dvamt=armadura.get(dvam).get('int_VEL')
        else: dvamt=0
        if dve in escudos: dvet=escudos.get(dve).get('int_VEL')
        else: dvet=0
        debuff_vel=dvat+dvamt+dvet
        n.append(z)
        u=nomes.get(z).get('velocidade')+debuff_vel
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
    nomedef=z
    print('Combatentes:',n)
    na='0'
    combatentesleft=len(n)
    while x=='s':
        while u2<(len(n)):
            while u<(len(n)):
                if combatentesleft==1:
                    truebreak=True
                    break
                if v[u2]==v2[u] and not n[u]==na:
                    truebreak=False
                    while True:
                        if truebreak:
                            na=n[u]
                            break
                        sair=False
                        while True:
                            print('vez de',n[u])
                            TdC=input('Qual a sua ação?\n')
                            if TdC=='me':
                                nomedef=melee(n[u],q[u],n)
                                with open('Beta/data/combatentes.json') as j:
                                    nomesm=json.load(j)
                                nomes[nomedef]['hp']=nomesm.get(nomedef).get('hp')
                                truebreak=True
                                break
                            elif TdC=='ma':
                                nomedef=magical(n[u],q[u],n)
                                with open('Beta/data/combatentes.json') as j:
                                    nomesm=json.load(j)
                                nomes[nomedef]['hp']=nomesm.get(nomedef).get('hp')
                                truebreak=True
                                break
                            elif TdC=='use':
                                sair=useitem(0,n[u],2)
                                with open('Beta/data/combatentes.json') as f:
                                    nomes=json.load(f)
                                if not sair:
                                    truebreak=True
                                    break
                            else: print('Não existe essa opção')
                    if nomes.get(nomedef).get('hp')<=0:
                        combatentesleft-=1
                        inde=n.index(nomedef)
                        i[inde]=0
                        v2[inde]=-100
                else: u+=1
            u=0
            u2+=1
        u2=0
        while u<(len(n)):
            a[u]=i[u]*aux
            q[u]=int(a[u])-int(a2[u])
            a2[u]=a[u]
            if q[u]>=1: auxq[u]=q[u] 
            else: auxq[u]=1
            u+=1
        u=0
        auxq.sort()
        while u<(len(n)):
            q[u]-=(auxq[0]-1)
            u+=1
        aux+=1
        u=0
        x=input('Deseja continuar o combate?')
    nomes={}
    with open('Beta/data/combatentes.json','w') as f:
        json.dump(nomes,f)
    return(n)
