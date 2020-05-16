import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def add():
        perso=input('Qual personagem você quer modificar?\n')
        if perso in nomes or perso in npcs:
         status=input('HP, mana ou gold?\n')
         if status=='hp':
            print('Seu hp era de', nomes[perso]['hp'])
            addhp=input('Quanto vai adicionar?\n')
            hp=int(addhp) +int(nomes[perso]['hp'])
            nomes[perso]['hp'] = hp
            print('Seu hp foi modificado para',nomes[perso]['hp'])
         elif status=='mana':
            print('Sua mana era de', nomes[perso]['mana'])
            addmana=input('Quanto vai adicionar?\n')
            mana=int(addmana) +int(nomes[perso]['mana'])
            nomes[perso]['mana'] = mana
            print('Sua mana modificado para',nomes[perso]['mana'])
         elif status=='gold':
            print('Seu gold era de', nomes[perso]['inventario']['gold'])
            addgold=input('Quanto vai adicionar?\n')
            gold=int(addgold) +int(nomes[perso]['inventario']['gold'])
            nomes[perso]['inventario']['gold'] = gold
            print('Seu gold foi modificado para',nomes[perso]['inventario']['gold'])
         elif status=='xp':
            print('Seu xp era de', nomes[perso]['xp'])
            addxp=input('Quanto vai adicionar?\n')
            xp=int(addxp) +int(nomes[perso]['xp'])
            nomes[perso]['xp'] = xp
            print('Seu xp foi atualizado para',nomes[perso]['xp'])
        else: print('Esse nome não existe')
        if perso in nomes:
         with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
         print('Salvo')
        if perso in npcs:
         with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
         print('Salvo')
