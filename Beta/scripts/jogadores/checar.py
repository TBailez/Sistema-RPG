import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def checar():
    sair=0
    while True:
        while True:
            au=input('Qual nome do personagem que você deseja testar?\n')
            if au in nomes or au in npcs: break
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
        break