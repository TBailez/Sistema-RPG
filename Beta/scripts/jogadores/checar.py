import json
from .print import printar

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

with open('Beta/data/Racas.json') as h:
    Racas=json.load(h)

with open('Beta/data/classes.json') as i:
    classes=json.load(i)

with open('Beta/data/magias.json') as j:
    magias=json.load(j)

def checar(au2,y):
    sair=0
    while True:
        while True:
            if y==1: au=au2
            else: au=input('Qual nome do personagem que você deseja testar?\n')
            if au in nomes or au in npcs: break
            elif au.lower()=='checar' or au.lower()=='lista': printar('a',1)
            elif au.lower()=='classes' or au.lower()=='c':
                for c in classes:
                    print(c)
                    print('  Força',classes.get(c).get('int_FOR'))
                    print('  Inteligência',classes.get(c).get('int_INT'))
                    print('  Resistência',classes.get(c).get('int_RES'))
                    print('  Intransigência',classes.get(c).get('int_ING'))
                    print('  Velocidade',classes.get(c).get('int_VEL'))
                    print('  CHP',classes.get(c).get('int_CHP'))
                    print('  CMN',classes.get(c).get('int_CMN'))
                sair=True
                break
            elif au.lower()=='racas' or au.lower()=='r':
                for r in Racas:
                    print(r)
                    print('  Força',Racas.get(r).get('int_FOR'))
                    print('  Inteligência',Racas.get(r).get('int_INT'))
                    print('  Resistência',Racas.get(r).get('int_RES'))
                    print('  Intransigência',Racas.get(r).get('int_ING'))
                    print('  Velocidade',Racas.get(r).get('int_VEL'))
                    print('  CHP',Racas.get(r).get('int_CHP'))
                    print('  CMN',Racas.get(r).get('int_CMN'))
                sair=True
                break
            elif au.lower()=='magias' or au.lower()=='m':
                for m in magias:
                    print(m)
                    print('  Requisito',magias.get(m).get('requisito'))
                    print('  Dificuldade',magias.get(m).get('dificuldade'))
                    print('  Mana',magias.get(m).get('mana'))
                    print('  Dano',magias.get(m).get('dano'))
                    print('  Velocidade',magias.get(m).get('velocidade'))
                    print('  Classes',magias.get(m).get('classes'))
                sair=True
                break
            elif au.lower()=='exit' or au.lower()=='sair':
                sair=True
                break
            else: print('Burro esse nome não existe')
        if sair: break
        if au in nomes: non=nomes.copy()
        if au in npcs: non=npcs.copy()
        print('Os status de',au,'são:')
        print('Raça:',(non.get(au).get('raca')))
        print('Classe',(non.get(au).get('classe')))
        xp=(non.get(au).get('xp'))
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
        print('Lvl:',lvl)
        print('xp:',xp)
        print('HP:',(non.get(au).get('hp')))
        print('MANA:',(non.get(au).get('mana')))
        print('Força:',(non.get(au).get('forca')))
        print('Inteligência:',(non.get(au).get('inteligencia')))
        print('Resistência:',(non.get(au).get('resistencia')))
        print('Instransigência:',(non.get(au).get('intransigencia')))
        print('Velocidade:',(non.get(au).get('velocidade')))
        print('    arma:',non.get(au).get('inventario').get('arma'))
        print('    armadura:',non.get(au).get('inventario').get('armadura'))
        print('    gold:',non.get(au).get('inventario').get('gold'))
        break