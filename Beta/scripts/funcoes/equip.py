import json

def equipar():
   with open('Beta/data/nomes.json') as f:
      nomes=json.load(f)

   with open('Beta/data/npcs.json') as g:
      npcs=json.load(g)

   perso=input('Qual personagem você quer equipar?\n')
   if perso in nomes or perso in npcs:
      eq=input('Arma, armadura ou escudo?\n')
   if eq=='arma' or eq=="a":
       arma=nomes.get(perso).get('inventario').get('arma')
       print(arma)
       no=input('Qual arma você quer equipar?\n')
       if no in arma:
        arma.remove(no)
        arma.insert(0,no)
        print('Você equipou',arma[0])
   elif eq=='armadura' or eq=="arm":
       armadura=nomes.get(perso).get('inventario').get('armadura')
       print(armadura)
       no=input('Qual armadrua você quer equipar?\n')
       if no in armadura:
        armadura.remove(no)
        armadura.insert(0,no)
        print('Você equipou',armadura[0])
   elif eq=='escudo' or eq=="e":
       escudo=nomes.get(perso).get('inventario').get('escudo')
       print(escudo)
       no=input('Qual escudo você quer equipar?\n')
       if no in escudo:
        escudo.remove(no)
        escudo.insert(0,no)
        print('Você equipou',escudo[0])
   else: print('Esse nome não existe')
   if perso in nomes:
      with open('Beta/data/nomes.json','w') as f:
         json.dump(nomes,f)
      print('Salvo')
   if perso in npcs:
      with open('Beta/data/npcs.json','w') as g:
         json.dump(npcs,g)
      print('Salvo')




