import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def restaurar():
    while True:
        perso=input('Qual personagem você quer restaurar?\n')
        if perso in nomes or perso in npcs:
         status=input('HP ou Mana?\n')
         if status=='hp':
            print('Seu hp era de', nomes[perso]['hp'])
            reshp=(nomes[perso]['chp'])
            hp=int(reshp*15)
            nomes[perso]['hp'] = hp
            print('Seu hp foi restaurado para',nomes[perso]['hp'])
         elif status=='mana':
            print('Sua mana era de',(nomes[perso]['mana']))
            resmn=(nomes[perso]['cmana'])
            mana=int(resmn*15)
            nomes[perso]['mana'] = mana
            print('Sua mana foi restaurada para',nomes[perso]['mana'])
        else: print('Esse nome não existe')
        if perso in nomes:
         with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
         print('Salvo')
        if perso in npcs:
         with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
         print('Salvo')


 
