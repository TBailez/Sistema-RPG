import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

def melee(natk,q,combatentes):
    print("Vez de",natk,"atacar",q,"vez(es)")
    quanti=0
    while quanti<q:
        while True:
            nomedef=input('Qual o nome do defensor?\n')
            if nomedef in combatentes: break
            else: print('burro esse nome n existe')
        d1=int(input("dado atk:"))
        d2=int(input("dado def:"))
        dd=(d1-d2)
        if natk in nomes: non=nomes.get(natk)
        else: non=npcs.get(natk)
        f=int(non.get('forca'))
        boar=int(non.get('inventario').get('arma'))
        quo_atk=f+boar+dd
        quo_vel_atk=dd+int(non.get('velocidade'))
        if nomedef in nomes: non=nomes.get(nomedef)
        else: non=npcs.get(nomedef)
        f_def=int(non.get('forca'))
        boar_def=int(non.get('inventario').get('arma'))
        quo_def=int(non.get('resistencia'))+int(non.get('inventario').get('armadura'))
        dano=quo_atk-quo_def
        desvio=quo_vel_atk-int(non.get('velocidade'))
        parry=quo_atk-(f_def+boar_def)
        if d1==20: dano=dano*2
        if d2==20: int(dano=dano/2)
        print("Se tentar bloquear:\n Dano =",dano,'\nSe tentar desviar:')
        if desvio<=0:
            print(" Desvio")
        else:
            print(" Dano=",int(dano*1.5),)
        print('Se tentar parrear:')
        if parry<0 and desvio<0:
            if (parry+desvio)<=(-5): print(' Parry perfeito')
            else: print(' Parry inperfeito')
        else:
            print(' Dano=',dano+int(non.get('inventario').get('armadura')))
        quanti=quanti+1