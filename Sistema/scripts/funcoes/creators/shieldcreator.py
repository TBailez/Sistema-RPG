import json

def screator():
 with open('Beta/data/inventario/escudos.json') as f:
    escudos=json.load(f)

 while True:
    while True:
        name=input('Qual o nome do escudo?\n')
        if name in escudos: print('Esse escudo ja existe')
        else: break
    rme=int(input('Qual a resistência melee\n'))
    rma=int(input('Qual a resistência magica\n'))
    v=int(input('Qual a alteração na velocidade\n'))
    dados={
        'rme': rme,
        'rma': rma,
        'int_VEL': v,
    }
    escudos.update({name:dados})
    c=input('dejeja criar outro escudo?')
    with open('Beta/data/inventario/escudos.json','w') as f:
        json.dump(escudos,f)
    if c=='s': pass
    else: break