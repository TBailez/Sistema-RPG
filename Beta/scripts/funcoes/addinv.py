import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def additem():
    perso=input('Qual personagem você quer dar o item?\n')
    if perso in nomes or perso in npcs:
     item=input('Qual o nome do item?\n')
     nomes[perso]['inventario']['itens'] = item
     print('O item',item,"foi salvo em seu inventário")
    else: print('Esse nome não existe')
additem()