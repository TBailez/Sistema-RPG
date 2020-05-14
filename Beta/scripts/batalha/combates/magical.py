import json

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

with open('Beta/data/npcs.json') as g:
    npcs=json.load(g)

with open('Beta/data/magias.json') as h:
    magias=json.load(h)

def magical(natk,q,combatentes):
    print('Combate magico n ta funfando 100%')
    print("Vez de",natk,"atacar",q,"vez(es)")
    quanti=0
    while quanti<q:
        while True:
            nomedef=input('Qual o nome do defensor?\n')
            if nomedef in combatentes: break
            else: print('burro esse nome n existe')
        while True:
            for m in magias: print(m)
            spel=input('Qual spell será usado?')
            if spel in magias:
                spell=magias.get(spel)
                break
            else: print('Burro esse spell não existe')
        print(spell)
        d1=int(input("dado atk:"))
        d2=int(input("dado def:"))
        dd=(d1-d2)
        if natk in nomes: non=nomes.get(natk)
        else: non=npcs.get(natk)
        i=int(non.get('inteligencia'))
        boar=int(non.get('inventario').get('arma'))
        quo_atk=i+boar+dd+spell.get('dano')
        quo_vel_atk=dd+int(spell.get('velocidade'))
        if nomedef in nomes: non=nomes.get(nomedef)
        else: non=npcs.get(nomedef)
        #i_def=int(non.get('inteligencia'))
        #boar_def=int(non.get('inventario').get('arma'))
        quo_def=int(non.get('intransigencia'))+int(non.get('inventario').get('armadura'))
        dano=quo_atk-quo_def
        desvio=quo_vel_atk-int(non.get('velocidade'))
        #parry=quo_atk-(f_def+boar_def)
        if d1==20: dano=dano*2
        if d2==20: int(dano=dano/2)
        print("Se tentar bloquear:\n Dano =",dano,'\nSe tentar desviar:')
        if desvio<=0:
            print(" Desvio")
        else:
            print(" Dano=",int(dano*1.5),)
        #print('Se tentar parrear:')
        #if parry<0 and desvio<0:
        #    if (parry+desvio)<=(-5): print(' Parry perfeito')
        #    else: print(' Parry inperfeito')
        #else:
        #    print(' Dano=',dano+int(non.get('inventario').get('armadura')))
        quanti=quanti+1
        od=input('Qual a opção do defensor?')
        if od.lower()=='bloquar' or od.lower()=='b': danof=dano
        if od.lower()=='desviar' or od.lower()=='d': danof=dano*1.5
        #if od.lower()=='parear' or od.lower()=='p': danof=dano+int(non.get('inventario').get('armadura'))
        if nomedef in nomes:
            nomes[nomedef]['hp']=nomes.get(nomedef).get('hp')-danof
            with open('Beta/data/npcs.json','w') as g:
                json.dump(npcs,g)
        if nomedef in npcs:
            npcs[nomedef]['hp']=npcs.get(nomedef).get('hp')-danof
            with open('Beta/data/npcs.json','w') as g:
                json.dump(npcs,g)