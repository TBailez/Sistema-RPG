import json

def additem(i,N,y):
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    while True:
        if y==1: perso=N
        else: perso=input('Qual personagem você quer dar o item?\n')
        if perso in nomes or perso in npcs:
            if perso in nomes: non=nomes.get(perso)
            else: non=npcs.get(perso)
            break
        else:
            print('Esse nome não existe')
            if y==1: return 0
    it = non['inventario']['itens']
    if y==1: item=i
    else: item=input('Qual o nome do item?\n')
    it.append(item)
    non['inventario']['itens'] = it
    if perso in nomes:
        nomes.update({perso:non})
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
    if perso in npcs:
        npcs.update({perso:non})
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
    print('O item',item,"foi salvo em seu inventário")


