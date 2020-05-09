import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

with open('Beta/data/Racas.json') as k:
   Racas=json.load(k)
rAcas=Racas.copy()

def personagem():
        nome = input('Qual é o seu nome? \n')
        npc=input('É um npc?\n')
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