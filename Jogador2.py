nomes={}
dados={}
aux=0
aux2=0
aux3=1
do = input('O que você deseja fazer? ')
while True:
    if do=='Criar jogador 1' or do =='Criar personagem 1' or do == 'criar jogador 1' or do =='cp':
        nome = input('Qual é o seu nome? \n')
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
        int_CHP = 0
        int_CMN = 0
        int_FOR = 0
        int_INT = 0
        int_RES = 0
        int_ING = 0
        int_VEL = 0
        RAÇA=input('Qual a sua Raça?\n')
        CLASSE=input('Qual a sua classe\n') 
        if RAÇA == 'Humano' or RAÇA =='humano' or RAÇA == 'HUMANO' :
            print('Você pode distribuir 3 pontos a mais')
        elif RAÇA == 'Elfo' or RAÇA == 'elfo' or RAÇA =='ELFO':
            int_INT += 2
            int_VEL += 1
        elif RAÇA == 'Orc' or RAÇA == 'orc' or RAÇA == 'ORC':
            int_FOR += 2
            int_RES += 2
            int_CHP += 1
            int_INT -= 1
            int_VEL -= 1
        while True:
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
            break
            #if ATR==18: break
            #else:
            #    if ATR>18: print('Você distribuiu pontos demais, vai ter que recomeçar do zero por fazer tudo errado')
            #    if ATR<18: print('Você não distribuiu todos os pontos, vai ter que recomeçar do zero por fazer tudo errado')
            #    int_CHP = 0
            #    int_CMN = 0
            #    int_FOR = 0
            #    int_INT = 0
            #    int_RES = 0
            #    int_ING = 0
            #    int_VEL = 0
        info=input('Tem armadura?')
        if info == 'Sim' or info == 'SIM' or info == 'sim' or info =='s':
            BoAr=input('Quanto de bonus de armadura?')
        else: BoAr=0
        info=input('Tem arma?')
        if info == 'Sim' or info == 'SIM' or info == 'sim' or info =='s':
            BoArm=input('Quanto de bonus de arma?')
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
        nomes.update({nome:dados})
        aux=aux+1
        do=input('O que deseja fazer?\n')
    elif do=='Checar status Jogador'or do=='c':
        if aux==0: 
            print('n existem jogadores pra testar')
            do = input('O que você deseja fazer? \n')
            break
        while True:
            au=input('qual nome do jogador q vc deseja testar?')
            if au in nomes: break
            else: 
                print('burro esse nome n existe')
        print('Os status de',au,'são:')
        print('Raça:',(nomes.get(au).get('raca')))
        print('Classe',(nomes.get(au).get('classe')))
        print('HP:',(nomes.get(au).get('hp')))
        print('MANA:',(nomes.get(au).get('mana')))
        print('Força:',(nomes.get(au).get('forca')))
        print('Inteligência:',(nomes.get(au).get('inteligencia')))
        print('Resistência:',(nomes.get(au).get('resistencia')))
        print('Instransigência:',(nomes.get(au).get('intransigencia')))
        print('Velocidade:',(nomes.get(au).get('velocidade')))
        do = input('O que deseja fazer? \n')
    elif do=='Combate'or do=='co':
        n=[]
        v=[]
        i=[]
        a=[]
        q=[]
        v2=[]
        q2=[]
        u=0
        u2=0
        auxi=1
        for z in nomes:
            v1=(nomes.get(z).get('velocidade'))
            n.insert(u,z)
            v.insert(u,v1)
            i.insert(u,(2.71828**((0.0423*v1)+0.0423)))
            q.insert(u,(int(i[u])))
            v2.insert(u,v[u])
            a.insert(u,(2.71828**((0.0423*v1)+0.0423)))
            u+=1
        u=0
        v.sort(reverse=True)
        x=1
        while x>0:
            while u<aux:
                a[u]=a[u]+(i[u]-q[u])
                u+=1
            u=0
            while u2<aux:
                while u<aux:
                    if v[u2]==v2[u]:
                            print("Vez de",n[u],"atacar",q[u],"vez(es)")
                            quanti=0
                            while quanti<q[u]:
                                while True:
                                    nomedef=input('Qual o nome do defensor?')
                                    if nomedef in nomes: break
                                    else: print('burro esse nome n existe')
                                d1=int(input("dado atk:"))
                                d2=int(input("dado def:"))
                                dd=(d1-d2)
                                f=int(nomes.get(n[u]).get('forca'))
                                ba=int(nomes.get(n[u]).get('inventario').get('arma'))
                                f2=int(nomes.get(nomedef).get('forca'))
                                ba2=int(nomes.get(nomedef).get('inventario').get('arma'))
                                qa=f+ba+dd
                                qd=int(nomes.get(nomedef).get('resistencia'))+int(nomes.get(nomedef).get('inventario').get('armadura'))
                                qva=dd+int(nomes.get(n[u]).get('velocidade'))
                                dano=qa-qd
                                desvio=qva-int(nomes.get(nomedef).get('velocidade'))
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
                                    print(' Dano=',dano+int(nomes.get(nomedef).get('inventario').get('armadura')))
                                quanti=quanti+1
                    u=u+1
                u=0
                u2=u2+1
            u2=0
            while u<aux:
                q[u]=int(a[u])
                if auxi==1:
                    q2.insert(u,int(a[u]))
                else:
                    q2[u]=int(a[u])
                u=u+1
            auxi=auxi-1
            u=0
            q2.sort()
            while u<aux:
                q[u]=q[u]-((q2[0])-1)
                u=u+1
            u=0
            x=int(input('Quer continuar o combate?(1=s)'))
        do = input('O que deseja fazer? \n')
    elif do=='e':
        if aux==0: 
            print('n existem jogadores pra editar')
            do = input('O que você deseja fazer? \n')
            break
        while True:
            au=input('qual nome do jogador q vc deseja editar?')
            if au in nomes: break
            else: 
                print('burro esse nome n existe')
        print('Os status de',au,'são:')
        
        input('Raça:',(nomes.get(au).get('raca')),'Nova raça: ')
        
        print('Classe',(nomes.get(au).get('classe')))
        print('HP:',(nomes.get(au).get('hp')))
        print('MANA:',(nomes.get(au).get('mana')))
        print('Força:',(nomes.get(au).get('forca')))
        print('Inteligência:',(nomes.get(au).get('inteligencia')))
        print('Resistência:',(nomes.get(au).get('resistencia')))
        print('Instransigência:',(nomes.get(au).get('intransigencia')))
        print('Velocidade:',(nomes.get(au).get('velocidade')))
        
    else: 
        print('N existe essa opção')
        do = input('O que você deseja fazer? ')
