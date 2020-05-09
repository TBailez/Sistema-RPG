#mudar o json
import json

with open('old\ded.json') as f:
    ded=json.load(f)
nomes=ded.get('nomes').copy()
npcs=ded.get('npcs').copy()
rAcas=ded.get('racas').copy()
dados={}
aux1=0
aux2=0
aux3=1
do = input('O que você deseja fazer? \n')
while True:
    if do.lower()=='criar jogador' or do =='cp':
        nome = input('Qual é o seu nome? \n')
        npc=input('É um npc?\n')
        #info = input('Você quer adicionar informações adicionais? \n')
        #if info == 'Sim' or info == 'SIM' or info == 'sim' or info =='s':
        #    idade = input('Quantos anos você tem? \n')
        #    cabelo = input('Qual a cor de seu cabelo? \n')
        #    altura = input('Qual a sua altura? \n')
        #    peso = input('Quanto você pesa? \n')
        #    alinhamento = input('Qual o seu alinhamento? \n')
        #    vestimenta = input('Descreva sua vestimenta \n')
        #elif info == 'Não' or info == 'não' or info == 'NÃO' or info == 'NAO' or info == 'Nao' or info == 'nao' or info =='n':
        #    print("Ótima escolha")
        #else:
        #    print("As opções eram sim ou não, mas tudo bem, vou considerar um não!")
        RAÇA=input('Qual a sua Raça?\n')
        while True:
            if RAÇA in rAcas: break
            elif RAÇA=='humano': break
            else: print('N existe essa raça')
        CLASSE=input('Qual a sua classe\n') 
        while True: 
            int_CHP = rAcas.get(RAÇA).get('int_CHP')
            int_CMN = rAcas.get(RAÇA).get('int_CMN')
            int_FOR = rAcas.get(RAÇA).get('int_FOR')
            int_INT = rAcas.get(RAÇA).get('int_INT')
            int_RES = rAcas.get(RAÇA).get('int_RES')
            int_ING = rAcas.get(RAÇA).get('int_ING')
            int_VEL = rAcas.get(RAÇA).get('int_VEL')
            print('Quanto de força você tem? (',int_FOR,')+')
            FOR = int(input())
            print('Quanto de inteligência você tem? (',int_INT,')+ ')
            INT = int(input())
            print('Quanto de resistência você tem? (',int_RES,')+')
            RES = int(input())
            print('Quanto de intransigência você tem? (',int_ING,')+') 
            ING = int(input())
            print('Quanto de velocidade você tem? (',int_VEL,')+') 
            VEL = int(input())
            print('Quanto é seu coeficiente de HP? (',int_CHP,')+') 
            CHP = int(input())
            print('Quanto é seu coeficiente de MANA? (',int_CMN,')+') 
            CMN = int(input())
            int_CHP = int(CHP)+int_CHP
            int_CMN = int(CMN)+int_CMN
            int_FOR = int(FOR)+int_FOR
            int_INT = int(INT)+int_INT
            int_RES = int(RES)+int_RES
            int_ING = int(ING)+int_ING
            int_VEL = int(VEL)+int_VEL
            ATR =int_CHP+int_CMN+int_FOR+int_ING+int_INT+int_RES+int_VEL
            HP = int_CHP*15
            MN = int_CMN*15
            if ATR==18: break
            else:
                if ATR>18: print('Você distribuiu pontos demais, vai ter que recomeçar do zero por fazer tudo errado')
                if ATR<18: print('Você não distribuiu todos os pontos, vai ter que recomeçar do zero por fazer tudo errado')
                int_CHP = 0
                int_CMN = 0
                int_FOR = 0
                int_INT = 0
                int_RES = 0
                int_ING = 0
                int_VEL = 0
        info=input('Tem armadura?\n')
        if info.lower() == 'sim' or info=='s':
            BoAr=input('Quanto de bonus de armadura?\n')
        else: BoAr=0
        info=input('Tem arma?\n')
        if info.lower() == 'sim' or info=='s':
            BoArm=input('Quanto de bonus de arma?\n')
        else: BoArm=0
        inventario={
            'armadura':BoAr,
            'arma':BoArm
        }
        dados={
            'forca':int_FOR,
            'velocidade' : int_VEL,
            'resistencia' : int_RES,
            'hp' : HP,
            'mana' : MN,
            'inteligencia' : int_INT,
            'intransigencia' : int_ING,
            'raca':RAÇA,
            'classe':CLASSE,
            'inventario':inventario
        }
        if npc.lower()=='sim' or npc=='s': npcs.update({nome:dados})
        else: nomes.update({nome:dados})
        do=input('O que deseja fazer?\n')
    elif do=='Checar status Jogador'or do=='c':
        jon=(input('Checar jogador ou npc?'))
        if jon.lower()=='jogador' or jon=='j': 
            non2=nomes.copy()
            while True:
                au=input('Qual nome do jogador que você deseja testar?\n')
                if au in nomes: break
                else: print('Burro esse nome não existe')
        elif jon.lower()=='npc' or jon=='n': 
            non2=npcs.copy()
            while True:
                au=input('Qual nome do npc que você deseja testar?\n')
                if au in npcs: break
                else: print('Burro esse nome não existe')
        else: print('Não existe essa opção')
        print('Os status de',au,'são:')
        print('Raça:',(non2.get(au).get('raca')))
        print('Classe',(non2.get(au).get('classe')))
        print('HP:',(non2.get(au).get('hp')))
        print('MANA:',(non2.get(au).get('mana')))
        print('Força:',(non2.get(au).get('forca')))
        print('Inteligência:',(non2.get(au).get('inteligencia')))
        print('Resistência:',(non2.get(au).get('resistencia')))
        print('Instransigência:',(non2.get(au).get('intransigencia')))
        print('Velocidade:',(non2.get(au).get('velocidade')))
        do = input('O que deseja fazer? \n')
    elif do=='Combate'or do=='co':
        non={}
        n=[]
        v=[]
        i=[]
        a=[]
        q=[]
        v2=[]
        q2=[]
        auxi=1
        print('Npc list:')
        for npc in npcs:
            print('  ',npc)
        while True:
            NPC=input('Quais npcs estaram no combate?(para não adicionar mais npcs digite exit)')
            if NPC in npcs: 
                n.append(NPC)
                u=(npcs.get(NPC).get('velocidade'))
                u2=(2.71828**((0.0423*u+0.0423)))
                v.append(u)
                v2.append(u)
                i.append(u2)
                a.append(u2)
                q.append(int(u2))
            elif NPC.lower()=='exit': break
            else: print('Não existe esse npc')
        u=0
        u2=0
        for z in nomes: 
            n.append(z)
            u=(nomes.get(z).get('velocidade'))
            u2=(2.71828**((0.0423*u+0.0423)))
            v.append(u)
            v2.append(u)
            i.append(u2)
            a.append(u2)
            q.append(int(u2))
        u=0
        u2=0
        v.sort(reverse=True)
        x=1
        print('Combatentes:',n)
        while x>0:
            while u<(len(n)):
                a[u]+=(i[u]-q[u])
                u+=1
            u=0
            while u2<(len(n)):
                while u<(len(n)):
                    if v[u2]==v2[u]:
                        print("Vez de",n[u],"atacar",q[u],"vez(es)")
                        quanti=0
                        while quanti<q[u]:
                            while True:
                                nomedef=input('Qual o nome do defensor?\n')
                                if nomedef in n: break
                                else: print('burro esse nome n existe')
                            d1=int(input("dado atk:"))
                            d2=int(input("dado def:"))
                            dd=(d1-d2)
                            if n[u] in nomes: non=nomes.copy()
                            else: non=npcs.copy()
                            f=int(non.get(n[u]).get('forca'))
                            f=int(non.get(n[u]).get('forca'))
                            ba=int(non.get(n[u]).get('inventario').get('arma'))
                            qva=dd+int(non.get(n[u]).get('velocidade'))
                            if nomedef in nomes: non=nomes.copy()
                            else: non=npcs.copy()
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
                                print(" Desvio")
                            else:
                                print(" Dano=",int(dano*1.5),"(x1,5)")
                            print('Se tentar parrear:')
                            if pa<0 and desvio<0:
                                if (pa+desvio)<=(-5): print(' Parry perfeito')
                                else: print(' Parry inperfeito')
                            else:
                                print(' Dano=',dano+int(non.get(nomedef).get('inventario').get('armadura')))
                            quanti=quanti+1
                        break
                    else: u+=1
                u=0
                u2+=1
            u2=0
            while u<(len(n)):
                q[u]=int(a[u])
                if auxi==1:
                    q2.insert(u,int(a[u]))
                else:
                    q2[u]=int(a[u])
                u+=1
            auxi=auxi-1
            u=0
            q2.sort()
            while u<(len(n)):
                q[u]=q[u]-((q2[0])-1)
                u=u+1
            u=0
            x=int(input('Quer continuar o combate?(1=s)'))
        do = input('O que deseja fazer? \n')
    elif do=='e':
        jon=(input('Editar jogador ou npc?'))
        if jon.lower()=='jogador' or jon=='j': 
            non2=nomes.copy()
            while True:
                au=input('Qual nome do jogador que você deseja editar?\n')
                if au in nomes: break
                else: print('Burro esse nome não existe')
        elif jon.lower()=='npc' or jon=='n': 
            non2=npcs.copy()
            while True:
                au=input('Qual nome do npc que você deseja editar?\n')
                if au in npcs: break
                else: print('Burro esse nome não existe')
        aux3=0
        while aux3<9:
            if aux3==0: aux1='raca'
            if aux3==1: aux1='classe'
            if aux3==2: aux1='hp'
            if aux3==3: aux1='mana'
            if aux3==4: aux1='forca'
            if aux3==5: aux1='resistencia'
            if aux3==6: aux1='inteligencia'
            if aux3==7: aux1='intransigencia'
            if aux3==8: aux1='velocidade'
            if aux3==0 or aux3==1:
                print('Deseja mudar',aux1,'?(',aux1,'atual:',(non2.get(au).get(aux1)),')')
                aux2=input()
                if aux2=='s':
                    print('Nova',aux1,':')
                    aux2=input()
                    nomes[au].update({aux1:aux2})
                    aux2=0
            else:
                print('Deseja mudar',aux1,'?(',aux1,'atual:',(non2.get(au).get(aux1)),')')
                aux2=input()
                if aux2=='s':
                    print('Nova',aux1,':')
                    aux2=int(input())
                    nomes[au].update({aux1:aux2})
                    aux2=0
            aux3+=1
        do = input('O que deseja fazer? \n')
    elif do=='s':
        ded={
            'nomes': nomes,
            'racas': rAcas,
            'npcs' : npcs
        }
        with open('c:/Sistema RPG/ded.json','w') as f:
            json.dump(ded,f)
        print('salvo')
        do = input('O que deseja fazer? \n')
    elif do=='p':
        print(nomes)
        do = input('O que deseja fazer? \n')
    else: 
        print('Não existe essa opção')
        do = input('O que você deseja fazer? \n')
