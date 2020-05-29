import json

with open('Beta/data/Racas.json') as h:
    Racas=json.load(h)

with open('Beta/data/classes.json') as i:
    classes=json.load(i)

with open('Beta/data/inventario/armas.json') as o:
    arma=json.load(o)

with open('Beta/data/inventario/armadura.json') as q:
    armadura=json.load(q)

for coisa in Racas:
    print(coisa,':')
    for aux in Racas.get(coisa):
        print('  ',aux,':',Racas.get(coisa).get(aux))

print('\n')
print('\n')

for coisa in classes:
    print(coisa,':')
    for aux in classes.get(coisa):
        print('  ',aux,':',classes.get(coisa).get(aux))

print('\n')
print('\n')

for coisa in arma:
    print(coisa,':')
    for aux in arma.get(coisa):
        print('  ',aux,':',arma.get(coisa).get(aux))

print('\n')
print('\n')

for coisa in armadura:
    print(coisa,':')
    for aux in armadura.get(coisa):
        print('  ',aux,':',armadura.get(coisa).get(aux))