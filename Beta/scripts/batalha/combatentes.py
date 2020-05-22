import json
import random

def createcombatentes():
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    combatentes1={}
    sair=False
    truebreak=False
    print('Npc list:')
    for npc in npcs: 
        print('  ',npc)
    while True:
        if truebreak: break
        while True:
            # da pra escrever só o nome do npc ou só o nome,quantidade
            Npc=input('Quais npcs estaram no combate?[nome do npc,balanceador(manual/balanceador/custom),quantidade desse npc](para não adicionar mais npcs digite exit)\n')
            comx=Npc.split(sep=',')
            if comx[0] in npcs:
                sair=False
                while True:
                    if len(comx)==1:
                        balance=input('Qual balanceador será usado?(Digite o nivel de cada npc(digite sim), ser balanceado[digite b(mesmo nivel dos jogadores +ou- 1)], custom(digite ou)\n')
                        times=int(input('Quantos desse npc estarão no combate?\n'))
                    elif len(comx)==2:
                        Npc=comx[0]
                        try: times=int(float(comx[1]))
                        except ValueError: true=False
                        else: true=True
                        if true: times=int(comx[1])
                        else:
                            print('Numero de npcs dado não é um numero')
                            sair=True
                            break
                        balance=input('Qual balanceador será usado?(Digite o nivel de cada npc(digite s), ser balanceado[digite b(mesmo nivel dos jogadores +ou- 1)], custom(digite ou)\n')
                    elif len(comx)==3:
                        Npc=comx[0]
                        balance=comx[1]
                        try: times=int(float(comx[2]))
                        except ValueError: true=False
                        else: true=True
                        if true: times=int(comx[2])
                        else:
                            print('Numero de npcs dado não é um numero')
                            sair=True
                            break
                    else: print('Digitou coisas demais')
                    if balance=='b' or balance=='s' or balance=='ou': break
                    else:
                        print('Não existe essa opção de balanceador')
                        if len(comx)==3:
                            sair=True
                            break
                if sair: break
                if balance.lower()=='b':
                    div=0
                    lvl=0
                    for no in nomes:
                        div+=1
                        lvl+=nomes.get(no).get('lvl')
                    lvl=int(lvl/div)
                    var=1
                elif balance.lower()=='ou':
                    while True:
                        lvls=input('Digite qual nivel você deseja que esses npcs tenham, espaço, + ou - x niveis(exp:3 1 --> nivel 3 +- 1 nivel)')
                        lvlns=lvls.split(sep=' ')
                        if len(lvlns)==2:
                            try: lvl=int(float(lvlns[0]))
                            except ValueError: print('Nivel dado não é um numero')
                            else:
                                lvl=int(comx[0])
                                try: var=int(float(lvlns[0]))
                                except ValueError: print('Variancia dada não é um numero')
                                else:
                                    var=int(comx[0])
                                    break
                        else: print('Digitou errado')
                else:
                    lvl=1
                    var=0
                tlvl=lvl
                it=npcs.get(Npc).get('inventario').get('itens')
                while times>0:
                    if balance.lower()=='sim' or balance.lower()=='s':
                        print('Qual o nivel de',Npc,times,)
                        lvl=int(input())
                        varn=0
                    else: varn=random.randint(-var,var)
                    tlvl=lvl+varn
                    if tlvl<1: tlvl=1
                    if times==1: name=Npc 
                    else: name=Npc+' '+str(times)
                    inventariom=(npcs.get(Npc).get('inventario'))
                    gold=random.randint(0,int((npcs.get(Npc).get('inventario').get('gold'))*lvl))
                    items=[]
                    for i in it:
                        x=random.randint(0,5)
                        while x>0:
                            items.append(i)
                            x-=1
                    inventariom['gold']=gold
                    inventariom['itens']=items
                    if lvl>1: multiplicador=0.5
                    else: multiplicador=1
                    multi=0.3*lvl
                    if multi<1: multi=1
                    dados={
                        'forca': int((npcs.get(Npc).get('forca'))*multiplicador*lvl),
                        'velocidade' : int((npcs.get(Npc).get('velocidade'))*multiplicador*lvl),
                        'resistencia' : int((npcs.get(Npc).get('resistencia'))*multiplicador*lvl),
                        'chp': int((npcs.get(Npc).get('chp'))*multiplicador*lvl),
                        'hp': int((npcs.get(Npc).get('chp'))*multiplicador*lvl)*15,
                        'cmana': int((npcs.get(Npc).get('cmana'))*multiplicador*lvl),
                        'mana': int((npcs.get(Npc).get('cmana'))*multiplicador*lvl)*15,
                        'inteligencia' : int((npcs.get(Npc).get('inteligencia'))*multiplicador*lvl),
                        'intransigencia' : int((npcs.get(Npc).get('intransigencia'))*multiplicador*lvl),
                        'raca': (npcs.get(Npc).get('raca')),
                        'classe': (npcs.get(Npc).get('classe')),
                        'inventario': inventariom,
                        'lvl': tlvl,
                        'dropxp': int((npcs.get(Npc).get('dropxp'))*multi)
                    }
                    combatentes1[name]=dados
                    combatentes1[name]['inventario']=inventariom
                    times-=1
            elif comx[0].lower()=='exit':
                truebreak=True
                break
            else: print('Esse npc não existe')
    for n in nomes:
        combatentes1.update({n:nomes.get(n)})
    with open('Beta/data/combatentes.json','w') as j:
        json.dump(combatentes1,j)
