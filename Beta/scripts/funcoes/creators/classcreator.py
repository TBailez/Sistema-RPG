import json

def ccreator():
 with open('Beta/data/classes.json') as f:
    classes=json.load(f)

 while True:
    while True:
        name=input('Qual o nome da classe?\n')
        if name not in classes:
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
        else: print('Essa classe já existe')
    dados={
        'int_CHP': chp,
        'int_CMN': cmn,
        'int_FOR': f,
        'int_INT': it,
        'int_RES': r,
        'int_ING': ig,
        'int_VEL': v,
    }
    classes.update({name:dados})
    c=input('Deseja criar outra classe?')
    with open('Beta/data/classes.json','w') as f:
        json.dump(classes,f)
    if c=='s': pass
    else: break