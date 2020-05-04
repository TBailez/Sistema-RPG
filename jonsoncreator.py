import json

nomes={}
aux=nomes.get('qj')
nomes.update({'qj':0})
with open('c:/Sistema RPG/ded.json','w') as f:
    json.dump(nomes,f)
