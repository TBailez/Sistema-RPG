import pygame
from data.classes import Personagem
import pickle

with open('GameRPG/data/players.pickle','rb') as f:
    l=pickle.load(f) 
number=len(l)
window_size=(600,600)
D=pygame.display.set_mode(window_size)
D.fill((200,255,200))

# position players
wx=int(list(window_size)[0]/2)
wy=int(list(window_size)[1]/2)
if (number!=1) and (number<=5): wx+=60
positions=[[wx,wy],[(wx-120),wy],[wx-60,wy+84],[wx-60,wy-84],[wx+60,wy+84],[wx+60,wy-84],[(wx+120),wy]]
if number==1:
    l[0].x=int(list(window_size)[0]/2)
    l[0].y=int(list(window_size)[1]/2)
else:
    index=0
    for p in l:
        p.x=positions[index][0]
        p.y=positions[index][1]
        index+=1

        # load image
        p.sp=pygame.image.load(p.sp)

for p in l: p.draw(D,False,'i')
pygame.display.update()
vez=0
while True:
    for p in l:
        print(p.n,'vai mover?') 
        o=input()
        if o=='s': p.move(D,l)
    print('outro turno')

D.quit()
