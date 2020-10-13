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
    
    with open('Beta/data/inventario/armas.json') as k:
        armas=json.load(k)

    with open('Beta/data/inventario/armadura.json') as le:
        armaduras=json.load(le)

    with open('Beta/data/inventario/escudos.json') as e:
        escudos=json.load(e)

    while True:
        if y==1: au=au2
        else: au=input('Qual nome do personagem que você deseja checar?\n')
        if au in nomes or au in npcs or au in magias or au in classes or au in Racas or au in armas or au in armaduras or au in escudos: break
        else:
            print('Burro esse nome não existe')
            if y==1: return 0
    if au in nomes: non=nomes.get(au)
    if au in npcs: non=npcs.get(au)
    if au in magias: non=magias.get(au)
    if au in classes: non=classes.get(au)
    if au in Racas: non=Racas.get(au)
    if au in armas: non=armas.get(au)
    if au in armaduras: non=armaduras.get(au)
    if au in escudos: non=escudos.get(au)
    print(au,':')
    for aux in non:
        print('  ',aux,':',non.get(aux))