import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def restaurar(p,s,y):
    while True:
        if y==1: perso=p
        else: perso=input('Qual personagem você quer restaurar?\n')
        if perso in nomes or perso in npcs: break
        else: print('Esse nome não existe')
    if y==1:
        if s=='h' or s=='hp': status='hp'
        elif s=='m' or s=='mana': status='mana'
        elif s=='f' or s=='full': status='full'
        else: print('Não existe essa opção')
    else: status=input('HP ou Mana?\n')
    if status=='hp' or status=='full':
        if perso in nomes:
            if y==0: print('Seu hp era de', nomes[perso]['hp'])
            reshp=(nomes[perso]['chp'])
            hp=int(reshp*15)
            nomes[perso]['hp'] = hp
        else: 
            if y==0: print('Seu hp era de', npcs[perso]['hp'])
            reshp=(npcs[perso]['chp'])
            hp=int(reshp*15)
            npcs[perso]['hp'] = hp
        if y==0: print('Seu hp foi restaurado para',hp)
    elif status=='mana' or status=='full':
        if perso in nomes:
            if y==0: print('Sua mana era de',(nomes[perso]['mana']))
            resmn=(nomes[perso]['cmana'])
            mana=int(resmn*15)
            nomes[perso]['mana'] = mana
        else:
            if y==0: print('Sua mana era de',(npcs[perso]['mana']))
            resmn=(npcs[perso]['cmana'])
            mana=int(resmn*15)
            npcs[perso]['mana'] = mana
        if y==0: print('Sua mana foi restaurada para',mana)
    else: print('Essa opção não existe')
    if perso in nomes:
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
        print('Salvo')
    if perso in npcs:
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
        print('Salvo')


 
