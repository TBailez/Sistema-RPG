import json

def mcreator():
 with open('Beta/data/magias.json') as f:
    magias=json.load(f)

 with open('Beta/data/classes.json') as g:
    classes=json.load(g)

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
    c=[]
    while True:
        cl=input('Qual classe?\n')
        if cl=='all' or cl=='a':
            c.append("clerigo")
            c.append("druida")
            c.append("wizard")
            c.append("blood mage")
            c.append("sorcerer")
            c.append("dark lord")
            break
        if cl in classes:
            c.append(cl)
            con=input('Dejesa adicionar outra classe?\n')
            if con=='s': pass
            else: break
        elif c=='l':
            for cla in classes:
                print(cla)
        else: print('burro essa classe n exite')
    t=input('Qual o tipo da magia, dano ou heal?\n')
    dados={
        'requisito': r,
        'dificuldade': d,
        'mana': m,
        'dano': dano,
        'velocidade': v,
        'classes': c,
        'Type': t
    }
    magias.update({name:dados})
    c=input('dejeja criar outra magia?\n')
    with open('Beta/data/magias.json','w') as f:
        json.dump(magias,f)
    if c=='s': pass
    else: break