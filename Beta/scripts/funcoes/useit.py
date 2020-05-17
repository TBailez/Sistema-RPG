import json

def useitem(i,N,y):
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    while True:
        if y==1: perso=N
        else: perso=input('Qual personagem quer utilizar o item?\n')
        if perso in nomes or perso in npcs:
            if perso in nomes: non=nomes.get(perso)
            else: non=npcs.get(perso)
            break
        else:
            print('Esse nome não exite')
            if y==1: return 0
    it = non['inventario']['itens']
    while True:
        if y==1: item=i
        else: item=input('Qual o nome do item?\n')
        items=item.split(sep=' ')
        if item in it:
            if items[0]=='sp' or items[0]=='mp' or items[0]=='lp': break
            else: print('Item não é uma poção')
        else:
            print('Esse personagem não tem esse item  /  lista de itens desse personagem:\n   ',it)
            if y==1: return 0
    if items[0]=='sp': add=20
    if items[0]=='mp': add=50
    if items[0]=='lp': add=100
    if items[1]=='hp':
        if add+non['hp']<non['chp']*15:
            hp=add+non['hp']
            non['hp']=hp
        else: non['hp']=non['chp']*15
        it.remove(item)
    if items[1]=='mana':
        if add+non['mana']<non['cmana']*15:
            mana=add+non['mana']
            non['mana']=mana
        else: non['mana']=non['cmana']*15
        it.remove(item)
    if perso in nomes:
        nomes.update({perso:non})
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
        print('Salvo')
    if perso in npcs:
        npcs.update({perso:non})
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
        print('Salvo')