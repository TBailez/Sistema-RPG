import pygame
from data.classes import Personagem
from scripts.map.criamap import mapa
import pickle
from scripts.text import texto
from scripts.text import main

pygame.init()

# define se vai usar a png de grama ou fundo verde
Grass=False
# define se vai ter arvores e pedras ou n
Back=False

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
window_size=[500,500]
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

# Cria os objetos do background ou n
if Back:
    # ve qual o x,y max e min dos personagens
    minx=l[0].x
    maxx=l[0].x
    miny=l[0].y
    maxy=l[0].y
    for p in l:
        p.draw(D,False)
        if p.x<minx: minx=p.x
        if p.x>maxx: maxx=p.x
        if p.y<miny: miny=p.y
        if p.y>maxy: maxy=p.y
    # cria tudo
    back=mapa(list(window_size),'floresta 1',[minx-40,maxx+40,miny-40,maxy+40])
    # draw tudo
    for p in back['pedras']: pygame.draw.polygon(D,(100,100,100),p.l)
    for a in back['arvores']: pygame.draw.circle(D,(139,69,19),tuple(a.c),a.t)
else: back={}

# draw players
for p in l: p.draw(D,False)

# update display
pygame.display.update()

# loop de perguntas pra ver quem vai mover
vez=0
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    while vez<len(l):
        p=l[vez]
        texto((str(p.n)+' vai mover?'),textos,D,window_size,font,tat)
        resposta=main(D,window_size)
        o=resposta
        textos.insert(0,'   '+o)
        if o=='s':
            p.move(D,l,window_size,back)
            vez+=1
        elif o=='n': vez+=1
        else: textos.insert(0,'Não existe essa opção')
    vez=0
    print('outro turno')
     
D.quit()
