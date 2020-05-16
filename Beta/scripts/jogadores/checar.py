import json
from .print import printar

def checar(au2,y):
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
    
    if y==1: au=au2
    else: au=input('Qual nome do personagem que você deseja checar?\n')
    while True:
        if au in nomes or au in npcs or au in magias or au in classes or au in Racas: break
        else:
            print('Burro esse nome não existe')
            if y==1: return 0
    if au in nomes: non=nomes.get(au)
    if au in npcs: non=npcs.get(au)
    if au in magias: non=magias.get(au)
    if au in classes: non=classes.get(au)
    if au in Racas: non=Racas.get(au)
    print(au,':')
    for aux in non:
        print('  ',aux,':',non.get(aux))