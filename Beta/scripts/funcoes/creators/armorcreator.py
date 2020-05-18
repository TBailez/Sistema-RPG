import json

def acreator():
 with open('Beta/data/inventario/armadura.json') as f:
    armadura=json.load(f)

 while True:
    while True:
        name=input('Qual o nome da armadura?\n')
        if name in armadura: print('Essa armadura ja existe')
        else: break
    rme=int(input('Qual a resistência melee\n'))
    rma=int(input('Qual a resistência magica\n'))
    v=int(input('Qual a alteração na velocidade\n'))
    dados={
        'rme': rme,
        'rma': rma,
        'int_VEL': v,
    }
    armadura.update({name:dados})
    c=input('dejeja criar outra armadura?')
    with open('Beta/data/inventario/armadura.json','w') as f:
        json.dump(armadura,f)
    if c=='s': pass
    else: break