import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def editar():
    print('editor n esta funfando')
    while True:
        au=input('Qual nome do personagem que você deseja testar?\n')
        if au in nomes or au in npcs: break
        else: print('Burro esse nome não existe')
    if au in nomes: non=nomes.copy()
    if au in npcs: non=npcs.copy()
    aux3=0
    while aux3<10:
        if aux3==0: aux1='raca'
        if aux3==1: aux1='classe'
        if aux3==2: aux1='hp'
        if aux3==3: aux1='mana'
        if aux3==4: aux1='forca'
        if aux3==5: aux1='resistencia'
        if aux3==6: aux1='inteligencia'
        if aux3==7: aux1='intransigencia'
        if aux3==8: aux1='velocidade'
        if aux3==9: aux1='inventario'
        if aux3==0 or aux3==1:
            print('Deseja mudar',aux1,'?(',aux1,'atual:',(non.get(au).get(aux1)),')')
            aux2=input()
            if aux2=='s':
                print('Nova',aux1,':')
                aux2=input()
                non[au].update({aux1:aux2})
                aux2=0
        elif aux3==9:
            print('Deseja mudar',aux1,'?(',aux1,'atual:',(non.get(au).get(aux1)),')')
            aux2=input()
            if aux2=='s':
                aux3=0
                while aux3<2:
                    if aux3==0: aux1='arma'
                    if aux3==1: aux1='armadura'
                    if aux3==2: aux1='gold'
                    aux2=input('Deseja mudar',aux1,'?(',aux1,'atual:',non.get(au).get('inventario').get(aux1),')')


#     aqui q n funfa pq n sei dar update em dicionario dentro de dicionario


                    #if aux2=='s':
                    #    aux2=int(input('Nova',aux1,':\n')
                    #    non.update(au).update()
                    #aux3+=1      
        else:
            print('Deseja mudar',aux1,'?(',aux1,'atual:',(non.get(au).get(aux1)),')')
            aux2=input()
            if aux2=='s':
                print('Nova',aux1,':')
                aux2=int(input())
                non[au].update({aux1:aux2})
                aux2=0
        aux3+=1
    if au in npcs:
        npcs.update({au:non.get(au)})
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
        print('Salvo')
    if au in nomes:
        nomes.update({au:non.get(au)})
        with open('Beta/dada/nomes.json','w') as f:
            json.dump(nomes,f)
        print('Salvo')