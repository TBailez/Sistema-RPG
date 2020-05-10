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

def checar():
    sair=0
    while True:
        while True:
            au=input('Qual nome do personagem que você deseja testar?\n')
            if au in nomes or au in npcs: break
            elif au.lower()=='checar' or au.lower()=='lista': printar()
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
                sair=True
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