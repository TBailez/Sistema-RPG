import pygame
from data.classes import Personagem
#from scripts.map import mapa
import pickle

pygame.init()

with open('GameRPG/data/players.pickle','rb') as f:
    l=pickle.load(f) 
number=len(l)
window_size=(600,600)
D=pygame.display.set_mode(window_size)
#pedras=mapa(list(window_size),'floresta 1')
#D.blit((pygame.image.load('data/pngs/grass.png')),(0,0))
D.fill((200,255,200))
#criar fonte para texto
font = pygame.font.Font('freesansbold.ttf', 32)
#criar variaveis para cores o que facilita mt coisa
green = (0,255,0)
blue= (0,0,128)
#criando o texto
text = font.render('Sexy Time', True, green, blue)
#criando retangulo do texto
textRect = text.get_rect()
#variaveis de posição do texto
X=300
Y=500
#posição do texto
textRect.center = (X,Y) 
#display do texto
D.blit(text,textRect)

'''
for p in pedras:
    lista=[]
    for x,y in zip(p[0],p[1]): lista.append([x,y])
    pygame.draw.polygon(D,(100,100,100),lista)
'''

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

for p in l: p.draw(D,False)
pygame.display.update()
vez=0
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    for p in l:
        print(p.n,'vai mover?') 
        o=input()
        if o=='s': p.move(D,l)
    print('outro turno')

D.quit()
