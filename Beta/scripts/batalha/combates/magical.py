import json
from .melee import melee

def magical(natk,q,combatentes):
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    with open('Beta/data/magias.json') as h:
        magias=json.load(h)

    with open('Beta/data/inventario/armas.json') as j:
        armas=json.load(j)

    with open('Beta/data/inventario/armadura.json') as i:
        armadura=json.load(i)

    #print('Combate magico n ta funfando 100%')
    print("Vez de",natk,"atacar",q,"vez(es)")
    quanti=0
    while quanti<q:
        while True:
            nomedef=input('Qual o nome do defensor?\n')
            if nomedef in combatentes: break
            else: print('burro esse nome n existe')

        
        if natk in nomes: non=nomes.get(natk)
        else: non=npcs.get(natk)
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
            if spel in magias:
                spell=magias.get(spel)
                if non.get('mana')<spell.get('mana'):
                    print('O atacante n tem mana sufuciente pra esse spell (mana do personagem:',non.get('mana'),'/mana do spell:',spell.get('mana'),')')
                elif non.get('inteligencia')<spell.get('requisito'):
                    print('O atacante n tem inteligencia sufuciente pra esse spell (inteligencia do personagem:',non.get('inteligencia'),'/requisito do spell:',spell.get('requisito'),')')
                else: break
            elif spel=='melee':
                nomedefm=melee(natk,q,combatentes)
                return nomedefm
            else: print('Burro esse spell não existe')
        dmin=spell.get('dificuldade')-non.get('inteligencia')
        print('Dado minimo necessário para completar o spell:',dmin)
        d1=int(input("dado atk:"))
        if (d1+non.get('inteligencia'))<spell.get('dificuldade') or not d1==0:
            print('Spell falhou')
            danof=0
        else:
            d2=int(input("dado def:"))
            dd=(d1-d2)
            non['mana']-=spell.get('mana')
            i=int(non.get('inteligencia'))
            ing=non.get('intransigencia')
            boar=non.get('inventario').get('arma')
            if boar in armas: boar_atk=armas.get(boar).get('dma')
            else: boar_atk=0
            boarm=non.get('inventario').get('armadura')
            if boarm in armadura: boarm_atk=armas.get(boarm).get('rma')
            else: boarm_atk=0
            
            quo_atk=i+boar_atk+dd+spell.get('dano')
            quo_def2=ing+boarm_atk
            quo_vel_atk=dd+int(spell.get('velocidade'))


            if nomedef in nomes: non=nomes.get(nomedef)
            else: non=npcs.get(nomedef)
            i_def=int(non.get('inteligencia'))
            boar2=non.get('inventario').get('arma')
            if boar2 in armas: boar_def=armas.get(boar2).get('dma')
            else: boar_def=0
            boarm2=non.get('inventario').get('armadura')
            if boarm2 in armadura: armadura_def=int(armadura.get(boarm2).get('rma'))
            else: armadura_def=0
            

            quo_atk2=spell.get('dano')+boar_def+i_def
            quo_def=int(non.get('intransigencia'))+armadura_def
            dano=quo_atk-quo_def
            dano2=quo_atk2-quo_def2
            desvio=quo_vel_atk-int(non.get('velocidade'))
            parry=quo_atk-(i_def+boar_def)
            if d1==20: dano=dano*2
            if d2==20: int(dano=dano/2)
            rp=False

            print("Se tentar bloquear:\n Dano =",dano,'\nSe tentar desviar:')
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
            quanti=quanti+1
            od=input('Qual a opção do defensor?')
            if od.lower()=='bloquar' or od.lower()=='b': danof=dano
            if od.lower()=='desviar' or od.lower()=='d': danof=danod
            if od.lower()=='redirecionar' or od.lower()=='r':
                if rp:
                    d12=int(input('Dado do defensor(que agora está atacando)'))
                    d22=int(input('Dado do atacante'))
                    danof=dano2+(d12-d22)
                else: danof=danop
            if od.lower()=='0': danof=0
        if nomedef in nomes:
            nomes[nomedef]['hp']=nomes.get(nomedef).get('hp')-danof
            with open('Beta/data/nomes.json','w') as g:
                json.dump(nomes,g)
        if nomedef in npcs:
            npcs[nomedef]['hp']=npcs.get(nomedef).get('hp')-danof
            with open('Beta/data/npcs.json','w') as g:
                json.dump(npcs,g)
    return nomedef