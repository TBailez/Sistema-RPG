import json

def wcreator():
 with open('Beta/data/inventario/armas.json') as f:
    armas=json.load(f)

 while True:
    while True:
        name=input('Qual o nome da arma?\n')
        if name in armas: print('Essa arma ja existe')
        else: break
    dme=int(input('Qual o dano melee\n'))
    dma=int(input('Qual o dano magico\n'))
    v=int(input('Qual a alteração na velocidade\n'))
    dados={
        'dme': dme,
        'dma': dma,
        'int_VEL': v,
    }
    armas.update({name:dados})
    c=input('dejeja criar outra arma?')
    with open('Beta/data/inventario/armas.json','w') as f:
        json.dump(armas,f)
    if c=='s': pass
    else: break