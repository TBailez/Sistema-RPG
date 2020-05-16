import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

with open('Beta/data/Racas.json') as k:
    Racas=json.load(k)

with open('Beta/data/classes.json') as l:
    classes=json.load(l)
    
with open('Beta/data/inventario/armas.json') as o:
    armas=json.load(o)

with open('Beta/data/inventario/armadura.json') as q:
    armaduras=json.load(q)
def personagem():
        nome = input('Qual é o seu nome? \n')
        npc=input('É um npc?\n')
        gold=input('Quanto de dinheiro inicial você tem?\n')
        while True:
            RAÇA=input('Qual a sua raça?\n')
            if RAÇA in Racas: break
            else: print('Não existe essa raça')
        while True:    
            CLASSE=input('Qual a sua classe\n') 
            if CLASSE in classes: break
            else: print('Não existe essa classe')
        lvl=int(input('Qual nivel do personagem?\n'))
        if lvl==20: xp=294850
        if lvl==19: xp=225850
        if lvl==18: xp=183850
        if lvl==17: xp=148850
        if lvl==16: xp=121350
        if lvl==15: xp=101350
        if lvl==14: xp=84100
        if lvl==13: xp=69100
        if lvl==12: xp=55600
        if lvl==11: xp=44400
        if lvl==10: xp=33900
        if lvl==9: xp=24300
        if lvl==8: xp=16800
        if lvl==7: xp=10550
        if lvl==6: xp=5550
        if lvl==5: xp=3050
        if lvl==4: xp=1300
        if lvl==3: xp=300
        if lvl==2: xp=50
        if lvl==1: xp=0     
        while True:
            int_CHP = Racas.get(RAÇA).get('int_CHP') + classes.get(CLASSE).get('int_CHP')
            int_CMN = Racas.get(RAÇA).get('int_CMN') + classes.get(CLASSE).get('int_CMN')
            int_FOR = Racas.get(RAÇA).get('int_FOR') + classes.get(CLASSE).get('int_FOR')
            int_INT = Racas.get(RAÇA).get('int_INT') + classes.get(CLASSE).get('int_RES')
            int_RES = Racas.get(RAÇA).get('int_RES') + classes.get(CLASSE).get('int_INT') 
            int_ING = Racas.get(RAÇA).get('int_ING') + classes.get(CLASSE).get('int_ING')
            int_VEL = Racas.get(RAÇA).get('int_VEL') + classes.get(CLASSE).get('int_VEL')
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
            if ATR==21 or ATR==23 and CLASSE == 'dark lord': break
            else:
                if ATR>21 or ATR>23 and CLASSE == 'dark lord': print('Você distribuiu pontos demais, vai ter que recomeçar do zero por fazer tudo errado')
                if ATR<21 or ATR<23 and CLASSE == 'dark lord': print('Você não distribuiu todos os pontos, vai ter que recomeçar do zero por fazer tudo errado')
                int_CHP = 0
                int_CMN = 0
                int_FOR = 0
                int_INT = 0
                int_RES = 0
                int_ING = 0
                int_VEL = 0
        info=input('Tem arma?\n')
        if info.lower() == 'sim' or info=='s':
            while True:
             BoArm=input('Qual a sua arma?\n')
             if BoArm in armas: break
             else: print('Essa arma não existe')
        else: BoArm=0
        info=input('Tem armadrua?\n')
        if info.lower() == 'sim' or info=='s':
            while True:
             BoAr=input('Qual a sua armadura?\n')
             if BoAr in armaduras: break
             else: print('Essa armadura não existe')
        else: BoArm=0
        itens = list()
        inventario={
            'gold':gold,
            'armadura':BoAr,
            'arma':BoArm,
            'itens': itens
        }
        dados={
            'forca':int_FOR,
            'velocidade' : int_VEL,
            'resistencia' : int_RES,
            'chp': int_CHP,
            'hp': HP,
            'cmana': int_CMN,
            'mana': MN,
            'inteligencia' : int_INT,
            'intransigencia' : int_ING,
            'raca':RAÇA,
            'classe':CLASSE,
            'inventario':inventario,
            'lvl': lvl,
            'xp' : xp
        }
        if npc.lower()=='sim' or npc=='s':
            npcs.update({nome:dados})
            with open('Beta/data/npcs.json','w') as g:
                json.dump(npcs,g)
            print('Salvo')
        else:
            nomes.update({nome:dados})
            with open('Beta/data/nomes.json','w') as f:
                json.dump(nomes,f)
            print('Salvo')
