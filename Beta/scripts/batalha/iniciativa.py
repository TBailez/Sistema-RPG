import json
from .combates.melee import melee
from .combates.magical import magical
from .combatentes import createcombatentes
from ..funcoes.useit import useitem
from ..funcoes.lvlup import lvlup

def batalha():
    createcombatentes()
    with open('Beta/data/combatentes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/nomes.json') as jo:
        jogadores=json.load(jo)

    with open('Beta/data/inventario/armas.json') as h:
        armas=json.load(h)

    with open('Beta/data/inventario/armadura.json') as p:
        armadura=json.load(p)
    
    with open('Beta/data/inventario/escudos.json') as q:
        escudos=json.load(q)
    for pessoa in nomes:
        print('Nome: ',pessoa,'seus itens:')
        print(nomes.get(pessoa).get('inventario').get('itens'))
        print(nomes.get(pessoa).get('inventario').get('gold'))
    n=[]
    v=[]
    i=[]
    a=[]
    q=[]
    auxq=[]
    v2=[]
    a2=[]
    for z in nomes:
        ldva=nomes.get(z).get('inventario').get('arma')
        dva=ldva[0]
        ldvam=nomes.get(z).get('inventario').get('armadura')
        dvam=ldvam[0]
        ldve=nomes.get(z).get('inventario').get('escudo')
        dve=ldve[0]
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
        if int(u2)<1: q.append(1)
        else: q.append(int(u2))
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
    end=False
    lenn=len(n)
    while x=='s' or x=='sim':
        na=[]
        while u2<lenn:
            while u<lenn:
                if end: break
                if v[u2]==v2[u] and not n[u] in na:
                    na.append(n[u])
                    #print('\n')
                    for nm in n:
                        if nomes.get(nm).get('hp')>0:# and nm not n[u]:
                            print(' ',nm,'/',nomes.get(nm).get('hp'),'of',nomes.get(nm).get('chp')*15,'de vida')
                    #print('\n')
                    print('Vez de',n[u],'(',q[u],'ações )')
                    action=0
                    #print('\nu:',u)
                    #print('\nu2:',u2)
                    #print('\ni:',i)
                    #print('\nq:',q)
                    #print('\na:',a)
                    #print('\na2:',a2)
                    #print('\nv:',v)
                    #print('\nv2:',v2)
                    #print('\nauxq:',auxq)
                    while action<q[u]:
                        print('Qual a sua ação',action+1,'?')
                        TdC=input()
                        if TdC=='me':
                            nomedef=melee(n[u],n)
                            with open('Beta/data/combatentes.json') as jp:
                                nomesm=json.load(jp)
                            nomes=nomesm.copy()
                            nomes[nomedef]['hp']=nomes.get(nomedef).get('hp')
                            action+=1
                        elif TdC=='ma':
                            nomedef=magical(n[u],n)
                            with open('Beta/data/combatentes.json') as pj:
                                nomesm=json.load(pj)
                            nomes=nomesm.copy()
                            nomes[nomedef]['hp']=nomes.get(nomedef).get('hp')
                            action+=1
                        elif TdC=='use':
                            nomedef=n[u]
                            sair=useitem(0,n[u],2)
                            with open('Beta/data/combatentes.json') as fu:
                                nomesm=json.load(fu)
                            nomes=nomesm.copy()
                            if not sair: action+=1
                        elif TdC=='jump' or TdC=='j':
                            nomedef=n[u]
                            print("Pulou o turno")
                            action+=1
                        elif TdC=='end':
                            nomedef=n[u]
                            end=True
                            break
                        else: print('Não existe essa opção')
                        if nomes.get(nomedef).get('hp')<=0:
                            u-=1
                            print(nomedef,'morreu')
                            combatentesleft-=1
                            inde=n.index(nomedef)
                            if inde<u2: u2-=1
                            n.pop(inde)
                            for vi in v: 
                                if vi==v2[inde]:
                                    v.remove(vi)
                                    break
                            for vi in q:
                                if vi==q[inde]:
                                    qsort=q.copy()
                                    qsort.sort(reverse=True)
                                    if qsort[0]==auxq[0]: pass
                                    else: vi+=(auxq[0]-qsort[0])
                                    auxq.remove(vi)
                                    break
                            v2.pop(inde)
                            i.pop(inde)
                            a.pop(inde)
                            a2.pop(inde)
                            q.pop(inde)
                            lenn=len(n)
                    break
                else: u+=1
            u=0
            u2+=1
            if end: break
        u2=0
        while u<lenn:
            a[u]=i[u]*aux
            q[u]=int(a[u])-int(a2[u])
            a2[u]=a[u]
            if q[u]>=1: auxq[u]=q[u] 
            else: auxq[u]=1
            u+=1
        u=0
        auxq.sort()
        while u<lenn:
            q[u]-=(auxq[0]-1)
            u+=1
        aux+=1
        u=0
        for per in n:
            cmana=nomes.get(per).get('cmana')
            mana=nomes.get(per).get('mana')
            if nomes.get(per).get('cmana')>0:
                if cmana+mana>cmana*15: nomes[per]['mana']=cmana*15
                else: nomes[per]['mana']+=cmana
        while True:
            if end: x='n'
            else: x=input('Deseja continuar o combate?')
            if x=='loot' or x=='lootar' or x=='l' or x=='s' or x=='sim' or x=='n' or x=='nao': break
            else: print('Essa opção não existe')
    xptotal=0
    if x=='loot' or x=='lootar' or x=='l':
        print('Jogadores: ',jogadores)
        while True:
            print('Quem vai lootar?')
            lutador=input()
            if lutador in jogadores:
                lut={
                    'gold':0,
                    'arma': None,
                    'armadura': None,
                    'escudo': None,
                    'itens': None,
                }
                new_inventario={}
                for monstro in nomes:
                    if not monstro in jogadores and nomes.get(monstro).get('hp')<1:
                        print('Monstro:',monstro,' / Seu inventario:',nomes.get(monstro).get('inventario'))
                while True:
                    print('Deseja lootar todos os monstros(all) ou 1 especifico(u)?')
                    qual=input()
                    if qual=='all' or qual=='u': break
                    elif qual=='exit': break
                    else: print('Não existe essa opção')
                if qual=='u':
                    while True:
                        with open('Beta/data/combatentes.json') as f:
                            nomes=json.load(f)
                        print('Deseja lootar qual monstro?')
                        mon=input()
                        if not mon in jogadores and nomes.get(mon).get('hp')<1:
                            while True:
                                while True:
                                    print('Inventario de',mon,':',nomes.get(mon).get('inventario'))
                                    print('Deseja lootar tudo(all or a), só o gold(gold or g), todos os itens(i) ou digitar quais itens(d)?')
                                    x=input()
                                    if x=='all' or x=='a':
                                        lut['gold']+=nomes.get(mon).get('inventario').get('gold')
                                        lut['itens'].extend(nomes.get(mon).get('inventario').get('itens'))
                                        lut['arma'].extend(nomes.get(mon).get('inventario').get('arma'))
                                        lut['armadura'].extend(nomes.get(mon).get('inventario').get('armadura'))
                                        lut['escudo'].extend(nomes.get(mon).get('inventario').get('escudo'))
                                        new_inventario={}
                                        break
                                    elif x=='i':
                                        lut['itens'].extend(nomes.get(mon).get('inventario').get('itens'))
                                        new_inventario=nomes.get(mon).get('inventario')
                                        new_inventario.pop('itens',None)
                                        break
                                    elif x=='gold' or x=='g':
                                        lut['gold']+=nomes.get(mon).get('inventario').get('gold')
                                        new_inventario=nomes.get(mon).get('inventario')
                                        new_inventario.pop('gold',None)
                                        break
                                    elif x=='d':
                                        while True:
                                            while True:
                                                print('Qual item deseja lootar?')
                                                qual2=input()
                                                new_inventario=nomes.get(mon).get('inventario')
                                                if qual2 in nomes.get(mon).get('inventario').get('arma'):
                                                    variavel='arma'
                                                    break
                                                elif qual2 in nomes.get(mon).get('inventario').get('armadura'):
                                                    variavel='armadura'
                                                    break
                                                elif qual2 in nomes.get(mon).get('inventario').get('escudo'):
                                                    variavel='escudo'
                                                    break
                                                elif qual2 in nomes.get(mon).get('inventario').get('itens'):
                                                    variavel='itens'
                                                    break
                                                else: print('Esse monstro não tem esse item')
                                            lut[variavel].extend(nomes.get(mon).get('inventario').get(variavel).get(qual2))
                                            new_inventario[variavel].pop(qual2,None)
                                            nomes[mon]['inventario']=new_inventario
                                            with open('Beta/data/combatentes.json','w') as f:
                                                json.dump(nomes,f)
                                            print('Deseja lootar outro item desse monstro?')
                                            con=input()
                                            if con=='s': pass 
                                            else: break
                                        break
                                    else: print('Não existe essa opção')
                                print('Deseja lootar esse monstro novamente?')
                                ask=input()
                                if ask=='s': pass
                                else: break
                            for coisa in nomes.get(lutador).get('inventario'):
                                print('lut:',lut)
                                if lut.get(coisa)==None: pass
                                else:
                                    if isinstance((nomes.get(lutador).get('inventario').get(coisa)),list): nomes[lutador]['inventario'][coisa].extend(lut.get(coisa))
                                    else: nomes[lutador]['inventario'][coisa]+=(lut.get(coisa))
                            nomes[mon]['inventario']=new_inventario
                            with open('Beta/data/combatentes.json','w') as f:
                                json.dump(nomes,f)
                        elif mon=='exit': break
                        else: print('Não existe esse monstro')
                if qual=='all' or qual=='a':
                    for mon in nomes:
                        if not mon in jogadores and nomes.get(mon).get('hp')<1:
                            lut['gold']+=nomes.get(mon).get('inventario').get('gold')
                            lut['itens']+=nomes.get(mon).get('inventario').get('itens')
                            lut['arma']+=nomes.get(mon).get('inventario').get('arma')
                            lut['armadura']+=nomes.get(mon).get('inventario').get('armadura')
                            lut['escudo']+=nomes.get(mon).get('inventario').get('escudo')
                            new_inventario={}
                            for coisa in nomes.get(lutador).get('inventario'):
                                if isinstance(nomes.get(lutador).get('inventario').get(coisa),list): nomes[lutador]['inventario'][coisa].extend(lut.get(coisa))
                                else: nomes[lutador]['inventario'][coisa]+=lut.get(coisa)
                            nomes[mon]['inventario']=new_inventario
                            with open('Beta/data/combatentes.json','w') as f:
                                json.dump(nomes,f)
                        elif mon=='exit': break
                        else: print('Não existe esse monstro')
            elif lutador=='exit': break
            else: print('Esse nome não existe')
    for monstro in n:
        if not monstro in jogadores and nomes.get(monstro).get('hp')<1:
            xptotal+=nomes.get(monstro).get('dropxp')
    for per in n:
        if per in jogadores:
            lvlup(xptotal,per,2)
    nomes={}
    with open('Beta/data/combatentes.json','w') as f:
        json.dump(nomes,f)
    return(n)  
