import json

def addeq():
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)

    with open('Beta/data/npcs.json') as g:
        npcs=json.load(g)

    with open('Beta/data/inventario/armas.json') as h:
        ar=json.load(h)

    with open('Beta/data/inventario/armadura.json') as j:
        arm=json.load(j)

    with open('Beta/data/inventario/escudos.json') as k:
        esc=json.load(k)

    while True:
        perso=input('Qual personagem você quer dar o item?\n')
        if perso in nomes or perso in npcs:
            if perso in nomes: non=nomes.get(perso)
            else: non=npcs.get(perso)
            break
        else:
            print('Esse nome não existe')
    while True:
     item=input('Deseja adicionar uma arma, armadura ou escudo?\n')
     if item=="arma":
      arma = non['inventario']['arma']
      a=input('Qual o nome da arma?\n')
      if a in ar:
       arma.append(a)
       non['inventario']['arma'] = arma
       break
      else:print('Essa arma não existe')
     elif item=="armadura":
      armadura = non['inventario']['armadura']
      a=input('Qual o nome da armadura?\n')
      if a in arm:
       armadura.append(a)
       non['inventario']['armadura'] = armadura
       break
      else:print('Essa armadura não existe')
     elif item=="escudo":
      escudo = non['inventario']['escudo']
      a=input('Qual o nome do escudo?\n')
      if a in esc:
       escudo.append(a)
       non['inventario']['escudo'] = escudo  
       break
      else: print('Esse escudo não existe')
    if perso in nomes:
        nomes.update({perso:non})
        with open('Beta/data/nomes.json','w') as f:
            json.dump(nomes,f)
    if perso in npcs:
        npcs.update({perso:non})
        with open('Beta/data/npcs.json','w') as g:
            json.dump(npcs,g)
    print("Salvo")
