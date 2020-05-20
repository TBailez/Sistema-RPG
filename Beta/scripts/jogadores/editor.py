import json

def editar(N,y):
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)
    while True:
        if y==1: au=N
        else: au=input('Qual nome do personagem que você deseja editar?\n')
        if au in nomes or au in npcs: break
        else:
            print('Burro esse nome não existe')
            if y==1: return 0
    if au in nomes: non=nomes.get(au)
    if au in npcs: non=npcs.get(au)
    for aux3 in non:
        if aux3=='raca' or aux3=='classe':
            print('Deseja mudar',aux3,'?(',aux3,'atual:',(non.get(aux3)),')')
            aux2=input()
            if aux2=='s':
                print('Nova',aux3,':')
                aux2=input()
                non.update({aux3:aux2})
                aux2=0
        elif aux3=='inventario':
            print('Deseja mudar',aux3,'?(',aux3,'atual:',(non.get(aux3)),')')
            aux2=input()
            if aux2=='s':
                for inv in non.get('inventario'):
                    if inv=='itens':
                        aux2=input('Deseja editar os itens?')
                        if aux2=='s':
                            print('Itens de',au,':',non.get('inventario').get('itens'))
                            while True:
                                o=input('Deseja adicionar ou remover um item?(Para sair digite sair ou exit ou s)')
                                os=o.split(sep=' ')
                                if o.lower()=='adicionar' or o=='a' or os[0]=='add':
                                    if len(os)==2:
                                        itens_de_au=non.get('inventario').get('itens')
                                        itens_de_au.append(os[1])
                                    else:
                                        aux2=input('Adicionar qual item?\n')
                                        itens_de_au=non.get('inventario').get('itens')
                                        itens_de_au.append(aux2)
                                elif o.lower()=='remover' or o=='r' or os[0]=='r':
                                    if len(os)==2:
                                        if os[1] in non.get('inventario').get('itens'):
                                            itens_de_au=non.get('inventario').get('itens')
                                            itens_de_au.remove(os[1])
                                        else: print('Esse item não está no inventario desse personagem')
                                    else:
                                        aux2=input('Remover qual item?\n')
                                        itens_de_au=non.get('inventario').get('itens')
                                        itens_de_au.remove(aux2)
                                elif o.lower()=='sair' or o.lower()=='exit' or o.lower()=='s': break
                                else: print('Não existe essa opção')
                    else:
                        print('Deseja mudar',inv,'?(',inv,'atual:',non.get('inventario').get(inv),')')
                        aux2=input()
                        if aux2=='s':
                            if inv=='gold':
                                aux2=int(input('Novo gold:\n'))
                                non['inventario']['gold']=aux2
                            else:
                                print('Nova',inv,':')
                                aux2=input()
                                non['inventario'][inv]=aux2
        else:
            print('Deseja mudar',aux3,'?(',aux3,'atual:',(non.get(aux3)),')')
            aux2=input()
            if aux2=='s':
                print('Nova',aux3,':')
                aux2=int(input())
                non.update({aux3:aux2})
                aux2=0
    if au in npcs:
        npcs.update({au:non})
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
        print('Salvo')
    if au in nomes:
        nomes.update({au:non})
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
        print('Salvo')