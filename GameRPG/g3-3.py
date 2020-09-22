import pygame
from data.classes import Personagem
#from scripts.map import mapa
import pickle
from scripts.text import texto

'''
pedras=mapa(list(window_size),'floresta 1')
for p in pedras:
    lista=[]
    for x,y in zip(p[0],p[1]): lista.append([x,y])
    pygame.draw.polygon(D,(100,100,100),lista)
'''

pygame.init()

# define se vai usar a png de grama ou fundo verde
Grass=False

# cria tamanho da area de texto
tat=350
# cria uma lista com todos os textos
textos=[]
#criar fonte para texto
font = pygame.font.Font('freesansbold.ttf', 20)

# load players
with open('GameRPG/data/players.pickle','rb') as f:
    l=pickle.load(f) 
number=len(l)

# create window
window_size=[800,800]
D=pygame.display.set_mode((window_size[0]+tat,window_size[1]))

# fill window com verde ou grama
if Grass: D.blit((pygame.image.load('data/pngs/grass.png')),(0,0))
else: D.fill((200,255,200))

# position players (vai ser mais facil eu te explicar no discord como isso funfa)
wx=int((list(window_size)[0])/2)
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

# draw players
for p in l: p.draw(D,False)

# update display
pygame.display.update()

# loop de perguntas pra ver quem vai mover
vez=0
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    for p in l:
        texto((str(p.n)+' vai mover?'),textos,D,window_size,font,tat)
        print((str(p.n)+' vai mover?'))
        o=input()
        if o=='s': p.move(D,l,window_size)
    print('outro turno')

D.quit()
