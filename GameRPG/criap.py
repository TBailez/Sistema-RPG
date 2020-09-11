import pickle
from PIL import Image as img
import os
from data.classes import Personagem

i={}
for name in os.listdir('GameRPG/data/pngs'):
    I=img.open('GameRPG/data/pngs/'+name)
    i[name]={'image':I,'path':('GameRPG/data/pngs/'+name)}

while True:
    print('Digite o nome do personagem(para sair digite n/para ver os outros personagens digite read/para deletar os personagens digite delete):')
    n=input()
    if n=='n': break
    if n=='delete':
        P=[]
        with open('GameRPG/data/players.pickle','wb') as f:
            pickle.dump(P,f)
    elif n=='read':
        with open('GameRPG/data/players.pickle','rb') as f:
            Pi=pickle.load(f)
            for x in Pi:
                print(x)
    else:
        while True:
            print('Digite o nome da sprite para o personagem(se quiser ver as fotos digite show - só funciona se vc tiever a biblioteca pillow):')
            p=input()
            Deucerto=False
            if p=='show':
                for I in i:
                    print('name:',I)
                    i[I].get('image').show()
            else:
                for x in i:
                    l=splitx=x.split(sep='.')
                    if p==l[0]:
                        Ip=('GameRPG/data/pngs/'+x)
                        Deucerto=True
                        break
                if Deucerto: break
                else: print('Não existe essa opção')
        print('Digite o tamanho do personagem(so funciona com 50):')
        t=int(input())
        print('Digite a velocidade do personagem:')
        v=int(input())
        p=Personagem(Ip,0,0,n,v,t)
        with open('GameRPG/data/players.pickle','rb') as f:
            Pi=pickle.load(f)
        Pi.append(p)
        with open('GameRPG/data/players.pickle','wb') as f:
            pickle.dump(Pi,f)