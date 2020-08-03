from scripts.creator import cria
import pickle

while True:
    i='c'
    #i=input('Deseja usar qual função?')
    if i=='c': cria()
    if i=='b': break
    break
    
#  Vc tem q usar a função isso antes de qualquer outra coisa pro programa funfar(Só se n tiver nada em nos pickles):
'''
with open('Sistema-RPG/class2/data/a.pickle','wb') as f:
    dic={'teste':2}
    pickle.dump(dic,f)
    print('entrou')
'''