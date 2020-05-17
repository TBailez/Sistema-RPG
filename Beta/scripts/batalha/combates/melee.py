import json

def melee(natk,q,combatentes):
    with open('Beta/data/combatentes.json') as fa:
        combatentes=json.load(fa)

    with open('Beta/data/inventario/armas.json') as h:
        armas=json.load(h)

    with open('Beta/data/inventario/armadura.json') as i:
        armadura=json.load(i)

    with open('Beta/data/inventario/escudos.json') as es:
        escudos=json.load(es)

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


        non=combatentes.get(natk)
        f=int(non.get('forca'))
        res=non.get('resistencia')
        ar=non.get('inventario').get('arma')
        arm=non.get('inventario').get('armadura')
        if ar in armas: boar=int(armas.get(ar).get('dme'))
        else: boar=0
        if arm in armadura: boarm=armadura.get(arm).get('rme')
        else: boarm=0


        quo_atk=f+boar+dd
        quo_def2=boarm+res
        quo_vel_atk=dd+int(non.get('velocidade'))


        non=combatentes.get(nomedef)
        f_def=int(non.get('forca'))
        ar_def=non.get('inventario').get('arma')
        if ar_def in armas: boar_def=int(armas.get(ar).get('dme'))
        else: boar_def=0
        armad_def=non.get('inventario').get('armadura')
        if armad_def in armadura: armadura_def=int(armadura.get(armad_def).get('rme'))
        else: armadura_def=0
        escu_def=non.get('inventario').get('escudo')
        if escu_def in escudos: esc_def=int(escudos.get(escu_def).get('rme'))
        else: esc_def=0
        
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
            if dano-esc_def<1: danof=1
            else: danof=dano-esc_def
        if od.lower()=='desviar' or od.lower()=='d':
            if danon<1: danof=1
            else: danof=danon
        if od.lower()=='parear' or od.lower()=='p':
            if pp:
                d12=int(input('Dado do defensor(que agora está atacando)'))
                d22=int(input('Dado do atacante'))
                danof2=dano2+(d12-d22)
                combatentes[natk]['hp']=combatentes.get(natk).get('hp')-danof2
            else: danof=danop
        combatentes[nomedef]['hp']=combatentes.get(nomedef).get('hp')-danof
        with open('Beta/data/combatentes.json','w') as fa:
            json.dump(combatentes,fa)
    return nomedef