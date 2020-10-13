import json

def lvlup(x,n,y):
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    with open('Beta/data/bonuslvlup.json') as j:
        bonus=json.load(j)

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
    if y==1:
        name=n
        if name in nomes: non=nomes.copy()
        elif name in npcs: non=npcs.copy()
        else:
            print('Esse nome não existe')
            return 0
    if y==2:
        name=n
        if name in nomes: non=nomes.copy()
        elif name in npcs: non=npcs.copy()
        else:
            print('Esse nome não existe')
            return 0
        tlvlup='t'
    else: tlvlup=input('Deseja só modificar o nivel/xp(digite m) ou dar true lvl up(digite t)?')
    while True:
        if y==0: opcao=input('Deseja adicionar nivel ou xp?')
        else: opcao='x'
        if opcao.lower()=='n' or opcao.lower()=='nivel':
            while True:
                oldlvl=non.get(name).get('lvl')
                print('Nivel atual:',oldlvl)
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
            if nlvl==20: xp=300000
            if nlvl==19: xp=225000
            if nlvl==18: xp=185000
            if nlvl==17: xp=150000
            if nlvl==16: xp=120000
            if nlvl==15: xp=100000
            if nlvl==14: xp=85000
            if nlvl==13: xp=69000
            if nlvl==12: xp=55600
            if nlvl==11: xp=44400
            if nlvl==10: xp=33900
            if nlvl==9: xp=24300
            if nlvl==8: xp=16800
            if nlvl==7: xp=10550
            if nlvl==6: xp=5550
            if nlvl==5: xp=3050
            if nlvl==4: xp=1300
            if nlvl==3: xp=300
            if nlvl==2: xp=50
            if nlvl==1: xp=0
            lvl=nlvl
            break
        elif opcao.lower()=='x' or opcao.lower()=='xp':
            while True:
                if y==0:
                    print('Xp atual:',non.get(name).get('xp'))
                    op=input('Deseja adicionar ou retirar xp?')
                else: op='a'
                if op.lower()=='adicionar' or op.lower()=='a':
                    if y==0: xpi=int(input('Dejesa adicionar quanto de xp?'))
                    else: xpi=int(x)
                    oldxp=non.get(name).get('xp')
                    oldlvl=non.get(name).get('lvl')
                    xp=oldxp+xpi
                    break
                elif op.lower()=='remover' or op.lower()=='r':
                    xpi=int(input('Dejesa remover quanto de xp?'))
                    xp=non.get(name).get('xp')-xpi
                    if xp<0: xp=0
                    break
                else: print('Não existe essa opção')
            if xp>=300000: lvl=20
            elif xp>=225000: lvl=19
            elif xp>=185000: lvl=18
            elif xp>=150000: lvl=17
            elif xp>=120000: lvl=16
            elif xp>=100000: lvl=15
            elif xp>=85000: lvl=14
            elif xp>=69000: lvl=13
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
            break
        else: print('Não existe essa opção')
    if lvl>oldlvl and tlvlup=='t':
        times=lvl-oldlvl
        contador=0
        e1=False
        e2=False
        ra=0
        cla=0
        nor=0
        while contador<times:
            qual_lvlup=oldlvl+contador+1
            if qual_lvlup==5:
                ra+=1
                cla+=1
            if qual_lvlup==7: ra+=1
            if qual_lvlup==8: cla+=1
            if qual_lvlup==10:
                ra+=1
                cla+=1
                e1=True
            if qual_lvlup==12: cla+=1
            if qual_lvlup==13: ra+=1
            if qual_lvlup==15:
                ra+=1
                cla+=1
            if qual_lvlup==17: cla+=1
            if qual_lvlup==18: ra+=1
            if qual_lvlup==20:
                ra+=1
                cla+=1
                e2=True
            nor+=1
            contador+=1
        contador=0
        c2=ra
        tipo='ra'
        t2=non.get(name).get('raca')
        troca=False
        while contador<c2:
            if troca:
                tipo='cla'
                t2=non.get(name).get('classe')
            if not t2=='humano':
                for b in bonus[tipo][t2]:
                    if b=='int_FOR': non[name]['forca']+=b 
                    if b=='int_INT': non[name]['inteligencia']+=b
                    if b=='int_RES': non[name]['resistencia']+=b 
                    if b=='int_ING': non[name]['intransigencia']+=b 
                    if b=='int_VEL': non[name]['velocidade']+=b 
                    if b=='int_CHP':
                        non[name]['chp']+=b
                        non[name]['hp']=non.get(name).get('chp')*15
                    if b=='int_CMN':
                        non[name]['cmana']+=b
                        non[name]['mana']=non.get(name).get('cmana')*15
                contador+=1
                if contador==ra:
                    c2=cla
                    contador=0
                    troca=True
        contador=0
        ppd=nor*3
        if e1: ppd+=1
        elif e2: ppd+=2
        print('Parabens',name,', você passou para o nivel',lvl,', distribua',ppd,'pontos')
        print(' Dados:')
        for dado in non.get(name):
            if isinstance(non.get(name).get(dado),int) and not dado=='lvl' and not dado=='xp':
                print('  ',dado,':',non.get(name).get(dado))
        while True:
            total=ppd
            add_for=0
            add_int=0
            add_res=0
            add_ing=0
            add_vel=0
            add_chp=0
            add_cmn=0
            for hab in non.get(name):
                if isinstance(non.get(name).get(hab),int) and not hab=='xp' and not hab=='lvl' and not hab=='hp' and not hab=='mana':
                    print(hab,non.get(name).get(hab),('atual + '))
                    testeint=input()
                    try: add=int(float(testeint))
                    except ValueError: add=0
                    else: add=int(float(testeint))
                    if hab=='forca': add_for=add
                    if hab=='inteligencia': add_int=add
                    if hab=='resistencia': add_res=add
                    if hab=='intransigencia': add_ing=add
                    if hab=='velocidade': add_vel=add
                    if hab=='chp': add_chp=add
                    if hab=='cmana': add_cmn=add
                    total-=add
                    print('Pontos restantes para adicionar:',total)
            if total==0: break
            elif total>0: print('Você não distribuiu todos os pontos')
            else: print('Você distribuiu pontos demais')
        non[name]['forca']+=add_for
        non[name]['inteligencia']+=add_int
        non[name]['resistencia']+=add_res
        non[name]['intransigencia']+=add_ing
        non[name]['velocidade']+=add_vel
        non[name]['chp']+=add_chp
        non[name]['hp']=non.get(name).get('chp')*15
        non[name]['cmana']+=add_cmn
        non[name]['mana']=non.get(name).get('cmana')*15
    non[name]['lvl']=lvl
    non[name]['xp']=xp
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