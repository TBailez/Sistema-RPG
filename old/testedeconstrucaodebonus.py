import json

with open('Beta/data/classes.json') as f:
    teste=json.load(f)

with open('Beta/data/classes.json') as g:
    teste1=json.load(g)

for x in teste:
    for y in teste.get(x):
        if teste.get(x).get(y)<1: teste1[x].pop(y)
teste=teste1.copy()
print(teste1)

with open('Beta/data/teste.json','w') as g:
    json.dump(teste,g)