import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def restaurar():
    while True:
        perso=input('Qual personagem você quer restorar?\n')
        if perso in nomes or perso in npcs:
         status=input('HP ou Mana?\n')
         if status=='hp':
            print('Seu hp agora é de',(nomes[perso]['hp']))
            reshp=(nomes[perso]['chp'])
            hp=int(reshp*15)
            print(hp)
            nomes[perso]['hp'] = hp
            print('Seu hp foi restourado para',nomes[perso]['hp'])
         elif status=='mana':
            print('Sua mana agora é de',(nomes[perso]['mana']))
            resmn=(nomes[perso]['cmana'])
            mana=int(resmn*15)
            print(mana)
            nomes[perso]['mana'] = mana
            print('Sua mana foi restourada para',nomes[perso]['mana'])
        else: print('Esse nome não existe')

restaurar()


 
