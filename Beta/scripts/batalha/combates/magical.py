import json
from .melee import melee

def magical(natk,combatentes):
    with open('Beta/data/combatentes.json') as f:
        combatentes=json.load(f)

    with open('Beta/data/magias.json') as h:
        magias=json.load(h)

    with open('Beta/data/inventario/armas.json') as j:
        armas=json.load(j)

    with open('Beta/data/inventario/armadura.json') as i:
        armadura=json.load(i)

    with open('Beta/data/inventario/escudos.json') as qq:
        escudos=json.load(qq)

    while True:
        nomedef=input('Qual o nome do defensor?\n')
        if nomedef in combatentes:
            if combatentes.get(nomedef).get('hp')<0: print('Esse combatente está morto')
            else: break
        else: print('burro esse nome n existe')
    non=combatentes.get(natk)
    while True:
        for m in magias:
            for cla in magias.get(m).get('classes'):
                if non.get('classe')==cla:
                    manan=magias.get(m).get('mana')
                    requisiton=magias.get(m).get('requisito')
                    dmin=magias.get(m).get('dificuldade')-non.get('inteligencia')
                    print('  ',m,'/ mana:',manan,'/ requisito:',requisiton,'Dado minimo necessário para completar o spell:',dmin)
                    break
        print(' ',natk,'tem',non.get('mana'),'de mana e',non.get('inteligencia'),'de inteligencia')
        spel=input('Qual spell será usado?')
        if spel in magias and combatentes.get(natk).get('classe') in magias.get(spel).get('classes'):
            spell=magias.get(spel)
            if non.get('classe')=='blood mage': m_or_h='hp'
            else: m_or_h='mana'
            if non.get(m_or_h)<spell.get('mana'):
                print('O atacante n tem mana sufuciente pra esse spell (mana do personagem:',non.get(m_or_h),'/mana do spell:',spell.get('mana'),')')
            elif non.get('inteligencia')<spell.get('requisito'):
                print('O atacante n tem inteligencia sufuciente pra esse spell (inteligencia do personagem:',non.get('inteligencia'),'/requisito do spell:',spell.get('requisito'),')')
            else: break
        elif spel=='melee':
            nomedefm=melee(natk,combatentes)
            return nomedefm
        else: print('Burro esse spell não existe')
    dmin=spell.get('dificuldade')-non.get('inteligencia')
    print('Dado minimo necessário para completar o spell:',dmin)
    while True:
        d=input("dado atk:")
        try: d1=int(float(d))
        except ValueError: true=False
        else: true=True
        if true:
            d1=int(float(d))
            break
        else: print('D1 digitado não é um numero initeiro')
    if (d1+non.get('inteligencia'))>=spell.get('dificuldade') or d1==0:
        if spell.get('Type')=='heal':
            if combatentes.get(nomedef).get('hp')+spell.get('dano')+non.get('inteligencia')+d1-spell.get('dificuldade')>combatentes.get(nomedef).get('chp')*15: combatentes[nomedef]['hp']=combatentes.get(nomedef).get('chp')*15
            else: combatentes[nomedef]['hp']+=spell.get('dano')+non.get('inteligencia')+d1-spell.get('dificuldade')
            with open('Beta/data/combatentes.json','w') as f:
                json.dump(combatentes,f)
            return nomedef
        while spell.get('Type')=='dano':
            d=input("dado def:")
            try: d2=int(float(d))
            except ValueError: true=False
            else: true=True
            if true:
                d2=int(float(d))
                break
            else: print('D2 digitado não é um numero initeiro')
        dd=(d1-d2)
        non[m_or_h]-=spell.get('mana')
        i=int(non.get('inteligencia'))
        ing=non.get('intransigencia')
        lboar=non.get('inventario').get('arma')
        boar=lboar[0]
        if boar in armas: boar_atk=armas.get(boar).get('dma')
        else: boar_atk=0
        lboarm=non.get('inventario').get('armadura')
        boarm=lboarm[0]
        if boarm in armadura: boarm_atk=armadura.get(boarm).get('rma')
        else: boarm_atk=0
        quo_atk=i+boar_atk+dd+spell.get('dano')
        quo_def2=ing+boarm_atk
        quo_vel_atk=dd+int(spell.get('velocidade'))
        non=combatentes.get(nomedef)
        i_def=int(non.get('inteligencia'))
        lboar2=non.get('inventario').get('arma')
        boar2=lboar2[0]
        if boar2 in armas: boar_def=armas.get(boar2).get('dma')
        else: boar_def=0
        lboarm2=non.get('inventario').get('armadura')
        boarm2=lboarm2[0]
        if boarm2 in armadura: armadura_def=int(armadura.get(boarm2).get('rma'))
        else: armadura_def=0
        lescu_def=non.get('inventario').get('escudo')
        escu_def=lescu_def[0]
        if escu_def in escudos: esc_def=int(escudos.get(escu_def).get('rme'))
        else: esc_def=0
        quo_atk2=spell.get('dano')+boar_def+i_def
        quo_def=int(non.get('intransigencia'))+armadura_def
        dano=quo_atk-quo_def
        dano2=quo_atk2-quo_def2
        desvio=quo_vel_atk-int(non.get('velocidade'))
        parry=quo_atk-(i_def+boar_def)
        if d1==20: dano=dano*2
        if d2==20: dano=int(dano/2)
        rp=False
        if dano-esc_def<1: danob=1
        else: danob=dano-esc_def
        if dano<1: dano=1
        print("Se tentar bloquear:\n Dano =",danob,'\nSe tentar desviar:')
        if desvio<=0:
            danod=0
            print(" Desvio")
        else:
            danod=int(dano*1.5)
            print(" Dano=",danod)
        print('Se tentar redirecionar a magia:')
        if parry<0 and desvio<0:
            danop=0
            if (parry+desvio)<=(-5):
                print(' Redirecionamento perfeito')
                rp=True
            else: print(' Redirecionamento inperfeito')
        else:
            danop=dano+armadura_def
            print(' Dano=',danop)
        while True:
            od=input('Qual a opção do defensor?')
            if od.lower()=='bloquar' or od.lower()=='b':
                danof=danob
                break
            elif od.lower()=='desviar' or od.lower()=='d':
                danof=danod
                break
            elif od.lower()=='redirecionar' or od.lower()=='r':
                if rp:
                    d12=int(input('Dado do defensor(que agora está atacando)'))
                    d22=int(input('Dado do atacante'))
                    danof2=dano2+(d12-d22)
                    combatentes[natk]['hp']=combatentes.get(natk).get('hp')-danof2
                else: danof=danop
                break
            else: print('Não existe essa opção')
    else:
        print('Spell falhou')
        danof=0
    combatentes[nomedef]['hp']=combatentes.get(nomedef).get('hp')-danof
    with open('Beta/data/combatentes.json','w') as f:
        json.dump(combatentes,f)
    return nomedef