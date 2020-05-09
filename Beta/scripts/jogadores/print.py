import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def printar():
    print('Lista de jogadores: ')
    for n in nomes: print('  ',n)
    print('Lista de npcs: ')
    for p in npcs: print('  ',p)