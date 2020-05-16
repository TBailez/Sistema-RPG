import json

def melee(natk,q,combatentes):
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    with open('Beta/data/inventario/armas.json') as h:
        armas=json.load(h)

    with open('Beta/data/inventario/armadura.json') as i:
        armadura=json.load(i)

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
        res=non.get('resistencia')
        ar=non.get('inventario').get('arma')
        arm=non.get('inventario').get('armadura')
        if ar in armas: boar=int(armas.get(ar).get('dme'))
        else: boar=0
        if arm in armadura: boarm=armas.get(arm).get('rme')
        else: boarm=0


        quo_atk=f+boar+dd
        quo_def2=boarm+res
        quo_vel_atk=dd+int(non.get('velocidade'))


        if nomedef in nomes: non=nomes.get(nomedef)
        else: non=npcs.get(nomedef)
        f_def=int(non.get('forca'))
        ar_def=non.get('inventario').get('arma')
        if ar_def in armas: 
            print('entrou aqui')
            boar_def=int(armas.get(ar).get('dme'))
        else: boar_def=0
        armad_def=non.get('inventario').get('armadura')
        if armad_def in armadura: armadura_def=int(armadura.get(armad_def).get('rme'))
        else: armadura_def=0
        
        quo_atk2=(f_def+boar_def)
        quo_def=int(non.get('resistencia'))+armadura_def
        dano=quo_atk-quo_def
        dano2=quo_atk2-quo_def2
        desvio=quo_vel_atk-int(non.get('velocidade'))
        parry=quo_atk-(f_def+boar_def)
        if d1==20: dano=dano*2
        if d2==20: int(dano=dano/2)
        print("Se tentar bloquear:\n Dano =",dano,'\nSe tentar desviar:')
        if desvio<=0:
            danon=0
            print(" Desvio")
        else:
            danon=int(dano*1.5)
            print(" Dano=",danon)
        print('Se tentar parrear:')
        pp=False
        if parry<0 and desvio<0:
            if (parry+desvio)<=(-5):
                print(' Parry perfeito')
                pp=True
            else: print(' Parry inperfeito')
            danop=0
        else:
            danopa=non.get('inventario').get('armadura')
            danop=int(armadura[danopa]['rme'])+dano
            print(' Dano=',danop)
        quanti=quanti+1
        od=input('Qual a opção do defensor?')
        if od.lower()=='bloquar' or od.lower()=='b':
            if dano<1: danof=1
            else: danof=dano
        if od.lower()=='desviar' or od.lower()=='d':
            if danon<1: danof=1
            else: danof=danon
        if od.lower()=='parear' or od.lower()=='p':
            if pp:
                d12=int(input('Dado do defensor(que agora está atacando)'))
                d22=int(input('Dado do atacante'))
                danof=dano2+(d12-d22)
            else: danof=danop
        if nomedef in nomes:
            nomes[nomedef]['hp']=nomes.get(nomedef).get('hp')-danof
            with open('Beta/data/nomes.json','w') as g:
                json.dump(nomes,g)
        if nomedef in npcs:
            npcs[nomedef]['hp']=npcs.get(nomedef).get('hp')-danof
            with open('Beta/data/npcs.json','w') as g:
                json.dump(npcs,g)
    return nomedef