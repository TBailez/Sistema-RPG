import json

def rcreator():
 with open('Beta/data/Racas.json') as f:
    Racas=json.load(f)

 while True:
    while True:
        name=input('Qual o nome da raça?\n')
        if name not in Racas:
            chp=int(input('Qual o coeficiente de hp?\n'))
            cmn=int(input('Qual o coeficiente de mana?\n'))
            f=int(input('força?\n'))    
            it=int(input('inteligência?\n'))
            r=int(input('resistência?\n'))
            ig=int(input('intransigência?\n'))
            v=int(input('velocidade?\n'))
            soma=int(chp)+int(cmn)+int(f)+int(r)+int(it)+int(ig)+int(v)
            if soma>3 or soma<3: print('Você não distribuiu certo os pontos') 
            break
        else: print('Essa raça já existe')
    dados={
        'int_CHP': chp,
        'int_CMN': cmn,
        'int_FOR': f,
        'int_INT': it,
        'int_RES': r,
        'int_ING': ig,
        'int_VEL': v,
    }
    Racas.update({name:dados})
    c=input('Deseja criar outra raça?')
    with open('Beta/data/Racas.json','w') as f:
        json.dump(Racas,f)
    if c=='s': pass
    else: break
