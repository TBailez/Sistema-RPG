import json
from ..jogadores.editor import editar

def editor(N,y):
    with open('Beta/data/Racas.json') as h:
        Racas=json.load(h)

    with open('Beta/data/classes.json') as i:
        classes=json.load(i)

    with open('Beta/data/magias.json') as j:
        magias=json.load(j)
    
    with open('Beta/data/inventario/armas.json') as k:
        armas=json.load(k)

    with open('Beta/data/inventario/armadura.json') as le:
        armaduras=json.load(le)

    with open('Beta/data/inventario/escudos.json') as e:
        escudos=json.load(e)
    
    while True:
        if y==1: au=N
        else: au=input('Qual tipo de coisa você deseja editar(jogadores,npcs,classes,raças,magias,armas,armaduras,escudos)?\n')
        if au.lower()=='classes' or au.lower()=='classe' or au.lower()=='c':
            print(classes)
            a=input('Qual classe deseja editar?\n')
            if a in classes:
                non=classes.get(a)
                break
            else: ('Nome digitado não existe')
        elif au.lower()=='jogadores' or au.lower()=='npcs' or au.lower()=='j' or au.lower()=='n':
            editar(0,0)
            return 0
        elif au.lower()=='racas' or au.lower()=='raca' or au.lower()=='r':
            print(Racas)
            a=input('Qual raça deseja editar?\n')
            if a in Racas:
                non=Racas.get(a)
                break
            else: ('Nome digitado não existe')
        elif au.lower()=='magias' or au.lower()=='magia' or au.lower()=='m':
            print(magias)
            a=input('Qual magia deseja editar?\n')
            if a in magias:
                non=magias.get(a)
                break
            else: ('Nome digitado não existe')
        elif au.lower()=='armaduras' or au.lower()=='armadura' or au.lower()=='arm':
            print(armaduras)
            a=input('Qual armadura deseja editar?\n')
            if a in armaduras:
                non=armaduras.get(a)
                break
            else: ('Nome digitado não existe')
        elif au.lower()=='armas' or au.lower()=='arma' or au.lower()=='ar':
            print(armas)
            a=input('Qual arma deseja editar?\n')
            if a in armas:
                non=armas.get(a)
                break
            else: ('Nome digitado não existe')
        elif au.lower()=='escudos' or au.lower()=='escudo' or au.lower()=='e':
            print(escudos)
            a=input('Qual escudo deseja editar?\n')
            if a in escudos:
                non=escudos.get(a)
                break
            else: ('Nome digitado não existe')
        else: print('Essa opção não existe')
    print(au,':')
    for aux in non:
        print('Deseja mudar',aux,'(',aux,'atual:',non.get(aux),')')
        d=input()
        if d.lower()=='s' or d.lower()=='sim':
            if isinstance(non.get(aux),int):
                d=int(input('New',aux,':'))
                non[aux]=d
            elif isinstance(non.get(aux),list):
                while True:
                    print(aux,':',non.get(aux))
                    d2=input('Deseja adicionar, remover itens ou manter lista como está?')
                    if d2=='a':
                        aux2=non.get(aux)
                        d3=input('Digite oque deseja adicioar:\n')
                        aux2.append(d3)
                    elif d2=='r':
                        aux2=non.get(aux)
                        d3=input('Digite oque deseja remover:\n')
                        if d3 in aux2: aux2.remove(d3)
                        else: print('Não existe isso na lista')
                    elif d2=='m': break
                    else: print('Não existe essa opção(opções: a, r, m)')
                non[aux]=aux2
            else:
                d=input('New',aux,':')
                non[aux]=d

    if au.lower()=='classes' or au.lower()=='classe' or au.lower()=='c':
        classes[au]=non
        with open('Beta/data/classes.json','w') as i:
            json.dump(classes,i)
    elif au.lower()=='racas' or au.lower()=='raca' or au.lower()=='r':
        Racas[au]=non
        with open('Beta/data/Racas.json','w') as h:
            json.dump(Racas,h)
    elif au.lower()=='magias' or au.lower()=='magia' or au.lower()=='m':
        magias[au]=non
        with open('Beta/data/magias.json','w') as j:
            json.dump(magias,j)
    elif au.lower()=='armaduras' or au.lower()=='armadura' or au.lower()=='arm':
        armaduras[au]=non
        with open('Beta/data/inventario/armadura.json','w') as le:
            json.dump(armaduras,le)
    elif au.lower()=='armas' or au.lower()=='arma' or au.lower()=='ar':
        armas[au]=non
        with open('Beta/data/inventario/armas.json','w') as k:
            json.dump(armas,k)
    elif au.lower()=='escudos' or au.lower()=='escudo' or au.lower()=='e':
        escudos[au]=non
        with open('Beta/data/inventario/escudos.json','w') as e:
            json.dump(escudos,e)