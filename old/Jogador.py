do = input('O que você deseja fazer? \n')
while do == 'Criar jogador 1' or do =='Criar personagem 1' or do == 'criar jogador 1':
 nome = input('Qual é o seu nome? \n')
 info = input('Você quer adicionar informações adicionais? \n')
 if info == 'Sim' or info == 'SIM' or info == 'sim' :
    idade = input('Quantos anos você tem? \n')
    cabelo = input('Qual a cor de seu cabelo? \n')
    altura = input('Qual a sua altura? \n')
    peso = input('Quanto você pesa? \n')
    alinhamento = input('Qual o seu alinhamento? \n')
    vestimenta = input('Descreva sua vestimenta \n')
 elif info == 'Não' or info == 'não' or info == 'NÃO' or info == 'NAO' or info == 'Nao' or info == 'nao' :
        print("Ótima escolha")
 else:
        print("As opções eram sim ou não, mas tudo bem, vou considerar um não!")
 FOR = input('Quanto de força você tem? \n')
 INT = input('Quanto de inteligência você tem? \n')
 RES = input('Quanto de resistência você tem? \n')
 ING = input('Quanto de intransigência você tem? \n')
 VEL = input('Quanto de velocidade você tem? \n')
 CHP = input('Quanto é seu coeficiente de HP? \n')
 CMN = input('Quanto é seu coeficiente de MANA? \n')
 int_CHP = int(CHP)
 int_CMN = int(CMN)
 int_FOR = int(FOR)
 int_INT = int(INT)
 int_RES = int(RES)
 int_ING = int(ING)
 int_VEL = int(VEL)
 ATR =int_CHP+int_CMN+int_FOR+int_ING+int_INT+int_RES+int_VEL
 if ATR > 15:
     print('Você distribuiu pontos demais, vai ter que recomeçar do zero por fazer tudo errado')
     do = 0
     do = input('O que voçê deseja fazer? \n')
 RAÇA = input('Qual a sua Raça? \n')
 if RAÇA == 'Humano' or RAÇA =='humano' or RAÇA == 'HUMANO' :
    print('Você pode distribuir 3 pontos')
   
    
 elif RAÇA == 'Elfo' or RAÇA == 'elfo' or RAÇA =='ELFO':
    int_INT += 2
    int_VEL += 1
 elif RAÇA == 'Orc' or RAÇA == 'orc' or RAÇA == 'ORC':
    int_FOR += 2
    int_RES += 2
    int_CHP += 1
    int_INT -= 1
    int_VEL -= 1
    
 CLASSE = input('Qual a sua classe \n') 


 HP = int_CHP*15
 MN = int_CMN*15
 print('Os status de',(nome),'são:')
 print('Raça:',(RAÇA))
 print('Classe',(CLASSE))
 print('HP:',(HP))
 print('MANA:',(MN))
 print('Força:',(int_FOR))
 print('Inteligência:',(int_INT))
 print('Resistência:',(int_RES))
 print('Instransigência:',(int_ING))
 print('Velocidade:',(int_VEL))
 do = 0
 do = input('O que deseja fazer? \n')
while do == 'Checar status Jogador 1':
 print('Os status de',(nome),'são:')
 print('Raça:',(RAÇA))
 print('Classe',(CLASSE))
 print('HP:',(HP))
 print('MANA:',(MN))
 print('Força:',(int_FOR))
 print('Inteligência:',(int_INT))
 print('Resistência:',(int_RES))
 print('Instransigência:',(int_ING))
 print('Velocidade:',(int_VEL))
 do = 0
 do = input('O que deseja fazer? \n')