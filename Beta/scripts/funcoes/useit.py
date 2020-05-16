import json

def useitem():
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    perso=input('Qual personagem quer utilizar o item?\n')
    if perso in nomes or perso in npcs:
        it = nomes[perso]['inventario']['itens']
        item=input('Qual o nome do item?\n')
        if item in nomes[perso]['inventario']['itens']:
         if item=='sp hp':
            addhp=20
            if int(addhp)+int(nomes[perso]['hp'])<int(nomes[perso]['chp']*15):
             hp=int(addhp) +int(nomes[perso]['hp'])
             nomes[perso]['hp'] = hp    
             it.remove(item)
            else: 
             nomes[perso]['hp'] = int(nomes[perso]['chp']*15)
             it.remove(item)
         if item=='mp hp':
            addhp=50
            if int(addhp)+int(nomes[perso]['hp'])<int(nomes[perso]['chp']*15):
             hp=int(addhp) +int(nomes[perso]['hp'])
             nomes[perso]['hp'] = hp    
             it.remove(item)
            else: 
             nomes[perso]['hp'] = int(nomes[perso]['chp']*15)
             it.remove(item)
         if item=='lp hp':
            addhp=100
            if int(addhp)+int(nomes[perso]['hp'])<int(nomes[perso]['chp']*15):
             hp=int(addhp) +int(nomes[perso]['hp'])
             nomes[perso]['hp'] = hp    
             it.remove(item)
            else: 
             nomes[perso]['hp'] = int(nomes[perso]['chp']*15)
             it.remove(item)
         if item=='sp mana':
            addmana=20
            if int(addmana)+int(nomes[perso]['mana'])<int(nomes[perso]['cmn']*15):
             mana=int(addmana) +int(nomes[perso]['mana'])
             nomes[perso]['mana'] = mana    
             it.remove(item)
            else: 
             nomes[perso]['mana'] = int(nomes[perso]['cmana']*15)
             it.remove(item)
         if item=='mp mana':
            addmana=50
            if int(addmana)+int(nomes[perso]['mana'])<int(nomes[perso]['cmn']*15):
             mana=int(addmana) +int(nomes[perso]['mana'])
             nomes[perso]['mana'] = mana    
             it.remove(item)
            else: 
             nomes[perso]['mana'] = int(nomes[perso]['cmana']*15)
             it.remove(item)
         if item=='lp mana':
            addmana=100
            if int(addmana)+int(nomes[perso]['mana'])<int(nomes[perso]['cmn']*15):
             mana=int(addmana) +int(nomes[perso]['mana'])
             nomes[perso]['mana'] = mana    
             it.remove(item)
            else: 
             nomes[perso]['mana'] = int(nomes[perso]['cmana']*15)
             it.remove(item)
        else:print('Você não possui esse item')
    else: print('Esse nome não existe')
    if perso in nomes:
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
        print('Salvo')
    if perso in npcs:
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
        print('Salvo')