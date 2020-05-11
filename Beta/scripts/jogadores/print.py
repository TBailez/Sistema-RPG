import json

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

def printar():
    ldq=input('Lista de que?(personagens,jogadores,npcs,classes,raças,magias)')
    if ldq.lower()=='personagens' or ldq.lower()=='jogadores' or ldq.lower()=='sim' or ldq.lower()=='p' or ldq.lower()=='j' or ldq.lower()=='s': 
        print('Lista de jogadores: ')
        for n in nomes: print('  ',n)
    if ldq.lower()=='personagens' or ldq.lower()=='npcs' or ldq.lower()=='sim' or ldq.lower()=='p' or ldq.lower()=='n' or ldq.lower()=='s':
        print('Lista de npcs: ')
        for p in npcs: print('  ',p)
    if ldq.lower()=='classes' or ldq.lower()=='sim' or ldq.lower()=='c' or ldq.lower()=='s':
        print('Lista de classes:')
        for c in classes: print('  ',c)
    if ldq.lower()=='racas' or ldq.lower()=='sim' or ldq.lower()=='r' or ldq.lower()=='s':
        print('Lista de raças:')
        for r in Racas: print('  ',r)
    if ldq.lower()=='magias' or ldq.lower()=='sim' or ldq.lower()=='m' or ldq.lower()=='s':
        print('Lista de magias:')
        for m in magias: print('  ',m)