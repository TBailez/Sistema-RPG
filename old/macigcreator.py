import json

with open('Beta/data/magias.json') as f:
    magias=json.load(f)

while True:
    while True:
        name=input('Qual o nome da magia?\n')
        if name in magias: print('esse nome ja existe')
        else: break
    r=int(input('Qual o requisito minimo?\n'))
    d=int(input('dificuldade?\n'))
    m=int(input('mana?\n'))
    dano=int(input('dano?\n'))
    v=int(input('velocidade?\n'))
    dados={
        'requisito': r,
        'dificuldade': d,
        'mana': m,
        'dano': dano,
        'velocidade': v
    }
    magias.update({name:dados})
    c=input('dejeja criar outra magia?')
    with open('Beta/data/magias.json','w') as f:
        json.dump(magias,f)
    if c=='s': pass
    else: break