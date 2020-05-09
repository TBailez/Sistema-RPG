import json

with open('c:/Sistema RPG/ded.json') as f:
    ded=json.load(f)
nomes=ded.get('nomes').copy()
npcs=ded.get('npcs').copy()
rAcas=ded.get('racas').copy()

while True:
    while True:
        non={}
        n=[]
        v2=[]
        q2=[]
        print('Npc list:')
        for npc in npcs:
            print('  ',npc)
        while True:
            NPC=input('Quais npcs estaram no combate?(para não adicionar mais npcs digite exit)')
            if NPC in npcs:
                non.update({NPC:npcs.get(NPC)})
                n.append(NPC)
                u2=(2.71828**((0.0423*(npcs.get(NPC).get('velocidade'))+0.0423)))
                v2.append(npcs.get(NPC).get('velocidade'))
                non[NPC].update({'iniciativa':u2})
                non[NPC].update({'auxiliar':u2})
                non[NPC].update({'q':int(u2)})
            elif NPC.lower()=='exit': break
            else: print('Não existe esse npc')
        for z in nomes: 
            non.update({z:nomes.get(z)})
            n.append(z)
            u2=(2.71828**((0.0423*(nomes.get(z).get('velocidade'))+0.0423)))
            v2.append(nomes.get(z).get('velocidade'))
            non[z].update({'iniciativa':u2})
            non[z].update({'auxiliar':u2})
            non[z].update({'q':int(u2)})
        u=0
        u2=0
        v2.sort(reverse=True)
        x=1
        print('Combatentes:',n)
        while x>0:
            for z in non:
                A={(non.get(z).get('auxiliar')+non.get(z).get('iniciativa')-non.get(z).get('q'))}
                non[z].update({'auxiliar':A})
            while u<(len(n)):
                print('entrou',u+1)
                for z in non:
                    if non[z].get('velocidade')==v2[u]:
                        print("Vez de",z,"atacar",non.get(z).get('q'),"vez(es)")
                        quanti=0
                        while quanti<non.get(z).get('q'):
                            while True:
                                nomedef=input('Qual o nome do defensor?\n')
                                if nomedef in non: break
                                else: print('burro esse nome n existe')
                            d1=int(input("dado atk:"))
                            d2=int(input("dado def:"))
                            dd=(d1-d2)
                            f=int(non.get(z).get('forca'))
                            f=int(non.get(z).get('forca'))
                            ba=int(non.get(z).get('inventario').get('arma'))
                            qva=dd+int(non.get(z).get('velocidade'))
                            f2=int(non.get(nomedef).get('forca'))
                            ba2=int(non.get(nomedef).get('inventario').get('arma'))
                            qa=f+ba+dd
                            qd=int(non.get(nomedef).get('resistencia'))+int(non.get(nomedef).get('inventario').get('armadura'))
                            dano=qa-qd
                            desvio=qva-int(non.get(nomedef).get('velocidade'))
                            pa=qa-(f2+ba2)
                            if d1==20: dano=dano*2
                            if d2==20: int(dano=dano/2)
                            print("Se tentar bloquear:\n Dano =",dano,'\nSe tentar desviar:')
                            if desvio<=0:
                                danod=0
                                print(" Desvio")
                            else:
                                danod=int(dano*1.5)
                                print(" Dano=",danod,"(x1,5)")
                            print('Se tentar parrear:')
                            if pa<0 and desvio<0:
                                danop=0
                                if (pa+desvio)<=(-5): print(' Parry perfeito')
                                else: print(' Parry inperfeito')
                            else:
                                danop=dano+int(non.get(nomedef).get('inventario').get('armadura'))
                                print(' Dano=',danop)
                            while True:
                                esc=input('Escolha do defensor:\n')
                                if esc.lower()=='desviar' or esc.lower()=='desvio' or esc.lower()=='d':
                                    non[nomedef].update({'hp':((non.get(nomedef).get('hp'))-danod)})
                                    break
                                elif esc.lower()=='bloquear' or esc.lower()=='bloqueio' or esc.lower()=='b':
                                    non[nomedef].update({'hp':((non.get(nomedef).get('hp'))-dano)})
                                    break
                                elif esc.lower()=='parrear' or esc.lower()=='parry' or esc.lower()=='p':
                                    non[nomedef].update({'hp':((non.get(nomedef).get('hp'))-danop)})
                                    break
                                else: print('Não existe essa opção')
                            if (non.get(nomedef).get('hp'))<=0:
                                print(nomedef,'morreu')
                                non[nomedef].update({'hp':0})
                                non.pop(nomedef)
                            quanti=quanti+1
                        break
                    else: u+=1
                u=0
                u2+=1
            u2=0
            for z in non:
                non[z].update({'q':int(non.get(z).get('auxiliar'))})
                q2.append(int(non.get(z).get('auxiliar')))
            u=0
            q2.sort()
            for z in non:
                non[z].update({'q':(non.get(n).get('q')-q2[0]-1)})
            xstr=input('Quer continuar o combate?(especial=e)')
            if xstr.lower()=='s' or xstr.lower()=='sim': x=1
            if xstr.lower()=='e' or xstr.lower()=='especial': x=1
            if xstr.lower()=='n' or xstr.lower()=='nao': x=0
        for name in non:
            if name in nomes:
                print(name,'ficou com',(nomes.get(name).get('hp')),'de vida')
                nomes[name].update({'hp':((nomes.get(name).get('chp'))*15)})
            if name in npcs:
                print(name,'ficou com',(npcs.get(name).get('hp')),'de vida')
                npcs[name].update({'hp':((npcs.get(name).get('chp'))*15)})
        do = input('O que deseja fazer? \n')