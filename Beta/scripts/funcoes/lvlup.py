import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def lvlup(x,n,y):
    quebrar=False
    while y==0:
        name=input('Qual nome do personagem que você deseja dar lvl up?')
        if name in nomes:
            non=nomes.copy()
            break
        elif name in npcs:
            non=npcs.copy()
            break
        else: print('Esse nome não existe')
    if y==1: name=n
    while True:
        if y==0: opcao=input('Deseja adicionar nivel ou xp?')
        else: opcao='x'
        if opcao.lower()=='n' or opcao.lower()=='nivel':
            while True:
                print('Nivel atual:',non.get(name).get('lvl'))
                op=input('Deseja adicionar ou retirar niveis?')
                if op.lower()=='adicionar' or op.lower()=='a':
                    while True:
                        niv=int(input('Dejesa adicionar quantos niveis?'))
                        nlvl=non.get(name).get('lvl')+niv
                        if nlvl>20: print('Adicionou niveis demais')
                        else:
                            quebrar=True
                            break
                elif op.lower()=='remover' or op.lower()=='r':
                    niv=int(input('Dejesa remover quantos niveis?'))
                    nlvl=non.get(name).get('lvl')-niv
                    if nlvl <1: nlvl=1
                    break
                else: print('Não existe essa opção')
                if quebrar: break
            if nlvl==20: xp=294850
            if nlvl==19: xp=225850
            if nlvl==18: xp=183850
            if nlvl==17: xp=148850
            if nlvl==16: xp=121350
            if nlvl==15: xp=101350
            if nlvl==14: xp=84100
            if nlvl==13: xp=69100
            if nlvl==12: xp=55600
            if nlvl==11: xp=44400
            if nlvl==10: xp=33900
            if nlvl==9: xp=24300
            if nlvl==8: xp=16800
            if nlvl==7: xp=10550
            if nlvl==6: xp=5550
            if nlvl==5: xp=3050
            if nlvl==4: xp=1300
            if nlvl==3: xp=250
            if nlvl==2: xp=50
            if nlvl==1: xp=0
            non[name]['lvl']=nlvl
            non[name]['xp']=xp
            break
        elif opcao.lower()=='x' or opcao.lower()=='xp':
            while True:
                if y==0:
                    print('Xp atual:',non.get(name).get('xp'))
                    op=input('Deseja adicionar ou retirar xp?')
                else: op='a'
                if op.lower()=='adicionar' or op.lower()=='a':
                    if y==0: xpi=int(input('Dejesa adicionar quanto de xp?'))
                    else: xpi=x
                    nxp=non.get(name).get('xp')+xpi
                    break
                elif op.lower()=='remover' or op.lower()=='r':
                    xpi=int(input('Dejesa remover quanto de xp?'))
                    nxp=non.get(name).get('xp')-xpi
                    if nxp<0: nxp=0
                    break
                else: print('Não existe essa opção')
            if xp>=294850: lvl=20
            elif xp>=225850: lvl=19
            elif xp>=183850: lvl=18
            elif xp>=148850: lvl=17
            elif xp>=121350: lvl=16
            elif xp>=101350: lvl=15
            elif xp>=84100: lvl=14
            elif xp>=69100: lvl=13
            elif xp>=55600: lvl=12
            elif xp>=44400: lvl=11
            elif xp>=33900: lvl=10
            elif xp>=24300: lvl=9
            elif xp>=16800: lvl=8
            elif xp>=10550: lvl=7
            elif xp>=5550: lvl=6
            elif xp>=3050: lvl=5
            elif xp>=1300: lvl=4
            elif xp>=300: lvl=3
            elif xp>=50: lvl=2
            else: lvl=1
            non[name]['lvl']=lvl
            non[name]['xp']=xp
            break
        else: print('Não existe essa opção')
    if name in npcs:
        npcs.update({name:non.get(name)})
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
        if y==0: print('Salvo')
    if name in nomes:
        nomes.update({name:non.get(name)})
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
        if y==0: print('Salvo')