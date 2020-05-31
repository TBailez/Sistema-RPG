import json

def melee(natk,combatentes):
    with open('Beta/data/combatentes.json') as fa:
        combatentes=json.load(fa)

    with open('Beta/data/inventario/armas.json') as h:
        armas=json.load(h)

    with open('Beta/data/inventario/armadura.json') as i:
        armadura=json.load(i)

    with open('Beta/data/inventario/escudos.json') as es:
        escudos=json.load(es)

    while True:
        nomedef=input('Qual o nome do defensor?\n')
        if nomedef in combatentes:
            if combatentes.get(nomedef).get('hp')<0: print('Esse combatente está morto')
            else: break
        else: print('burro esse nome n existe')
    while True:
        d=input("dado atk:")
        try: d1=int(float(d))
        except ValueError: true=False
        else: true=True
        if true:
            d1=int(float(d))
            break
        else: print('D1 digitado não é um numero initeiro')
    while True:
        d=input("dado def:")
        try: d2=int(float(d))
        except ValueError: true=False
        else: true=True
        if true:
            d2=int(float(d))
            break
        else: print('D2 digitado não é um numero initeiro')
    dd=(d1-d2)
    non=combatentes.get(natk)
    f=int(non.get('forca'))
    res=non.get('resistencia')
    lar=non.get('inventario').get('arma')
    ar=lar[0]
    larm=non.get('inventario').get('armadura')
    arm=larm[0]
    if ar in armas: boar=int(armas.get(ar).get('dme'))
    else: boar=0
    if arm in armadura: boarm=armadura.get(arm).get('rme')
    else: boarm=0
    quo_atk=f+boar+dd
    quo_def2=boarm+res
    quo_vel_atk=dd+int(non.get('velocidade'))
    non=combatentes.get(nomedef)
    f_def=int(non.get('forca'))
    lar_def=non.get('inventario').get('arma')
    ar_def=lar_def[0]
    if ar_def in armas: boar_def=int(armas.get(ar).get('dme'))
    else: boar_def=0
    larmd_def=non.get('inventario').get('armadura')
    armad_def=larmd_def[0]
    if armad_def in armadura: armadura_def=int(armadura.get(armad_def).get('rme'))
    else: armadura_def=0
    lescu_def=non.get('inventario').get('escudo')
    escu_def=lescu_def[0]
    if escu_def in escudos: esc_def=int(escudos.get(escu_def).get('rme'))
    else: esc_def=0
    quo_atk2=(f_def+boar_def)
    quo_def=int(non.get('resistencia'))+armadura_def
    dano=quo_atk-quo_def
    dano2=quo_atk2-quo_def2
    desvio=quo_vel_atk-int(non.get('velocidade'))
    parry=quo_atk-(f_def+boar_def)
    if d1==20: dano=dano*2
    if d2==20: dano=int(dano/2)
    if dano<1: dano=1
    if dano-esc_def<1: danob=1
    else: danob=dano-esc_def
    print("Se tentar bloquear:\n Dano =",danob,'\nSe tentar desviar:')
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
        danop=armadura_def+dano
        print(' Dano=',danop)
    while True:
        od=input('Qual a opção do defensor?')
        if od.lower()=='bloquar' or od.lower()=='b':
            danof=danob  
            break
        elif od.lower()=='desviar' or od.lower()=='d':
            danof=danon
            break
        elif od.lower()=='parear' or od.lower()=='p':
            if pp:
                while True:
                    dx=input('Dado do defensor(que agora está atacando)')
                    try: d12=int(float(dx))
                    except ValueError:print('Digite um número seu animal!')
                    else:
                        d12=int(float(dx))  
                        break
                while True:
                    dy=input('Dado do atacante')
                    try: d22=int(float(dy))
                    except ValueError:print('Digite um número seu animal!')
                    else:
                        d22=int(float(dy))
                        break
                danof2=dano2+(d12-d22)
                combatentes[natk]['hp']=combatentes.get(natk).get('hp')-danof2
                danof=0
            else: danof=danop
            break
        else: print('Não existe essa opção')
    combatentes[nomedef]['hp']=combatentes.get(nomedef).get('hp')-danof
    with open('Beta/data/combatentes.json','w') as fa:
        json.dump(combatentes,fa)
    return nomedef
