import json

def lootar():
    with open('Beta/data/combatentes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/nomes.json') as jo:
        jogadores=json.load(jo)

    print('Jogadores: ',jogadores.keys())
    while True:
        print('Quem vai lootar?')
        lutador=input()
        if lutador in jogadores:
            lut={
                'gold':0,
                'arma': [],
                'armadura': [],
                'escudo': [],
                'itens': [],
            }
            new_inventario={}
            for monstro in nomes:
                if not monstro in jogadores and nomes.get(monstro).get('hp')<1:
                    print('Monstro:',monstro,' / Seu inventario:',nomes.get(monstro).get('inventario'))
            while True:
                print('Deseja lootar todos os monstros(all) ou 1 especifico(u)?')
                qual=input()
                if qual=='all' or qual=='u': break
                elif qual=='exit': break
                else: print('Não existe essa opção')
            if qual=='u':
                while True:
                    with open('Beta/data/combatentes.json') as f:
                        nomes=json.load(f)
                    print('Deseja lootar qual monstro?')
                    mon=input()
                    if mon=='exit': break
                    elif  not mon in jogadores and mon in nomes:
                        if nomes.get(mon).get('hp')<1:
                            while True:
                                while True:
                                    print('Inventario de',mon,':',nomes.get(mon).get('inventario'))
                                    print('Deseja lootar tudo(all or a), só o gold(gold or g), todos os itens(i) ou digitar quais itens(d)?')
                                    x=input()
                                    if x=='all' or x=='a':
                                        lut['gold']+=nomes.get(mon).get('inventario').get('gold')
                                        lut['itens'].extend(nomes.get(mon).get('inventario').get('itens'))
                                        lut['arma'].extend(nomes.get(mon).get('inventario').get('arma'))
                                        lut['armadura'].extend(nomes.get(mon).get('inventario').get('armadura'))
                                        lut['escudo'].extend(nomes.get(mon).get('inventario').get('escudo'))
                                        new_inventario={}
                                        break
                                    elif x=='i':
                                        lut['itens'].extend(nomes.get(mon).get('inventario').get('itens'))
                                        new_inventario=nomes.get(mon).get('inventario')
                                        new_inventario.pop('itens',None)
                                        break
                                    elif x=='gold' or x=='g':
                                        lut['gold']+=nomes.get(mon).get('inventario').get('gold')
                                        new_inventario=nomes.get(mon).get('inventario')
                                        new_inventario.pop('gold',None)
                                        break
                                    elif x=='d':
                                        while True:
                                            while True:
                                                print('Qual item deseja lootar?')
                                                qual2=input()
                                                new_inventario=nomes.get(mon).get('inventario')
                                                if qual2 in nomes.get(mon).get('inventario').get('arma'):
                                                    variavel='arma'
                                                    break
                                                elif qual2 in nomes.get(mon).get('inventario').get('armadura'):
                                                    variavel='armadura'
                                                    break
                                                elif qual2 in nomes.get(mon).get('inventario').get('escudo'):
                                                    variavel='escudo'
                                                    break
                                                elif qual2 in nomes.get(mon).get('inventario').get('itens'):
                                                    variavel='itens'
                                                    break
                                                else: print('Esse monstro não tem esse item')
                                            lucy=nomes.get(mon).get('inventario').get(variavel)
                                            indexdalista=lucy.index(qual2)
                                            lut[variavel].append(lucy[indexdalista])
                                            new_inventario[variavel].remove(qual2)
                                            nomes[mon]['inventario']=new_inventario
                                            with open('Beta/data/combatentes.json','w') as f:
                                                json.dump(nomes,f)
                                            print('Deseja lootar outro item desse monstro?')
                                            con=input()
                                            if con=='s': pass 
                                            else: break
                                        break
                                    else: print('Não existe essa opção')
                                print('Deseja lootar esse monstro novamente?')
                                ask=input()
                                if ask=='s': pass
                                else: break
                            for coisa in nomes.get(lutador).get('inventario'):
                                if lut.get(coisa)==None: pass
                                else:
                                    if isinstance((nomes.get(lutador).get('inventario').get(coisa)),list): nomes[lutador]['inventario'][coisa].extend(lut.get(coisa))
                                    else: nomes[lutador]['inventario'][coisa]+=(lut.get(coisa))
                            nomes[mon]['inventario']=new_inventario
                            with open('Beta/data/combatentes.json','w') as f:
                                json.dump(nomes,f)
                        else: print('Não existe esse monstro')
            if qual=='all' or qual=='a':
                for mon in nomes:
                    if not mon in jogadores and nomes.get(mon).get('hp')<1:
                        lut={
                            'gold':0,
                            'arma': [],
                            'armadura': [],
                            'escudo': [],
                            'itens': []
                        }
                        lut['gold']+=nomes.get(mon).get('inventario').get('gold')
                        lut['itens']+=nomes.get(mon).get('inventario').get('itens')
                        lut['arma']+=nomes.get(mon).get('inventario').get('arma')
                        lut['armadura']+=nomes.get(mon).get('inventario').get('armadura')
                        lut['escudo']+=nomes.get(mon).get('inventario').get('escudo')
                        new_inventario={
                            'gold':0,
                            'arma': [],
                            'armadura': [],
                            'escudo': [],
                            'itens': []
                        }
                        for coisa in nomes.get(lutador).get('inventario'):
                            if isinstance(nomes.get(lutador).get('inventario').get(coisa),list): nomes[lutador]['inventario'][coisa].extend(lut.get(coisa))
                            else: nomes[lutador]['inventario'][coisa]+=lut.get(coisa)
                        nomes[mon]['inventario']=new_inventario
                        with open('Beta/data/combatentes.json','w') as f:
                            json.dump(nomes,f)
                    elif mon=='exit': break
                    else: print('Não existe esse monstro')
        elif lutador=='exit': break
        else: print('Esse nome não existe')
    for lootador in jogadores:
        jogadores[lootador]['inventario']=nomes[lootador]['inventario']
    with open('Beta/data/combatentes.json','w') as f:
        json.dump(nomes,f)
    with open('Beta/data/nomes.json','w') as jo:
        json.dump(jogadores,jo)