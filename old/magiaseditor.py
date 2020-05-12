import json

with open('Beta/data/magias.json') as f:
    magias=json.load(f)

with open('Beta/data/classes.json') as g:
    classes=json.load(g)

me={}
clase=[]
while True:
    while True:
        m=input('Qual nome da magia que você deseja editar?\n')
        continuar=0
        if m in magias: break
        elif m=='lista':
            for ma in magias:
                print(ma)
                continuar=1
        elif continuar==0: print('Burro esse nome não existe')
        else: print('Erro 1')
    me=(magias.get(m))
    if magias.get(m).get('classes')==None: clase=[]
    else: clase=(magias.get(m).get('classes'))
    aux3=0
    while aux3<6:
        if aux3==1: aux1='requisito'
        if aux3==2: aux1='dificuldade'
        if aux3==3: aux1='mana'
        if aux3==4: aux1='dano'
        if aux3==5: aux1='velocidade'
        if aux3==0: aux1='classes'
        if aux3==0:
            print('Deseja mudar as',aux1,'?(',aux1,'atuais:',(me.get(aux1)),')')
            aux2=input()
            if aux2=='s':
                while True:
                    o=input('Deseja adicionar ou remover uma classe?')
                    if o=='a':
                        while True:
                            qual=input('Qual classe deseja adicionar?')
                            continuar=0
                            if qual in classes: break
                            elif qual=='lista':
                                for cl in classes: print(cl)
                                continuar=1
                            elif continuar==0: print('Não existe essa classe(Digite lista se quiser ver a lista de classes)')
                            else: print('Erro 2')
                        clase.append(qual)
                        print(clase)
                        me.update({'classes':clase})
                    if o=='r':
                        while True:
                            qual=input('Qual classe deseja remover?')
                            continuar=0
                            if qual in me['classes']: break
                            elif qual=='lista':
                                for cla in me['classes']: print(cla)
                                continuar=1
                            elif continuar==0: print('Não existe essa classe nessa maiga(Digite lista se quiser ver a lista de classes dessa magia)')
                            else: print('Erro 3')
                        clase.remove(qual)
                        print(clase)
                        me.update({'classes':clase})
                decisao=input('Deseja fazer outra mudança nas classes?')
                if decisao=='s': pass
                else: break
        else:
            print('Deseja mudar',aux1,'?(',aux1,'atual:',me.get(aux1),')')
            aux2=input()
            if aux2=='s':
                print('Nova',aux1,':')
                aux2=int(input())
                me.update({aux1:aux2})
        aux3+=1
    magias.update({m:me})
    with open('Beta/data/magias.json','w') as f:
        json.dump(magias,f)
    print('Salvo')
    p=input('Deseja editar outra magia?\n')
    if p=='s': pass
    else: break

