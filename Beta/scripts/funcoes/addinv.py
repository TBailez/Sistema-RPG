import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def additem():
    perso=input('Qual personagem você quer dar o item?\n')
    if perso in nomes or perso in npcs:
     it = nomes[perso]['inventario']['itens']
     item=input('Qual o nome do item?\n')
     it.append(item)
     nomes[perso]['inventario']['itens'] = it
     print('O item',item,"foi salvo em seu inventário")
    else: print('Esse nome não existe')
    if perso in nomes:
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
        print('Salvo')
    if perso in npcs:
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
        print('Salvo')


