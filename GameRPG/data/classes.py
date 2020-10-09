import numpy as np
import cmath
import pygame
from scripts.text import texto

class Pedra:
    def __init__(self,centro,lista,maior):
        self.c=centro
        self.l=lista
        self.t=maior

    def update(self,x,y):
        newl=[]
        for p in self.l: newl.append([p[0]+x,p[1]+y])
        self.l=newl
        self.c=[self.c[0]+x,self.c[1]+y]
    
    def draw(self,m,x,y):
        self.update(x,y)
        pygame.draw.polygon(m,(100,100,100),self.l)

class Arvore:
    def __init__(self,centro,tamanho):
        self.c=centro
        self.t=int(tamanho)

    def update(self,x,y):
        self.c=[self.c[0]+x,self.c[1]+y]

    def draw(self,m,x,y):
        self.update(x,y)
        pygame.draw.circle(m,(139,69,19),tuple(self.c),self.t)

class Personagem:
    def __init__(self,sprite,x,y,nome,velocidade,tamanho,color=(0,0,255)):
        # true x,y
        self.tx=x
        self.ty=y
        
        self.sp=sprite
        self.n=nome
        self.v=velocidade
        self.t=tamanho

        # hitbox color = blue
        self.hc=color

        # x,y do centro
        self.x=int(x+(self.t/2))
        self.y=int(y+(self.t/2))

        # centro do range
        self.cr=[int(x+(self.t/2)),int(y+(self.t/2))]

        # linha de direção inicial
        self.d=[[0,0],[0,0]]
        
        self.hit=(self.x,self.y,self.t/2)

    def updateline(self,x,y,Re=False):
        if Re: return [[int(self.d[0][0])+x,int(self.d[0][1])+y],[int(self.d[1][0])+x,int(self.d[1][1])+y]]
        else: self.d=[[int(self.d[0][0])+x,int(self.d[0][1])+y],[int(self.d[1][0])+x,int(self.d[1][1])+y]]

    def draw(self,m,pos=False,DRAW=True):
        # m = map(display window)
        # pos = mouse position
        # DRAW = if true: draw things

        # update true x,y
        self.tx=(self.x-(self.t/2))
        self.ty=(self.y-(self.t/2))

        # draw sprite
        if DRAW: m.blit(self.sp,(self.tx,self.ty))
        
        # update hitbox
        self.hit=[self.x,self.y,int((self.t/2)*1.3)]
        
        # draw hitbox
        if DRAW: pygame.draw.circle(m,self.hc,(self.x,self.y),self.hit[2],2)
        
        # draw line 
        if not isinstance(pos,bool): self.drawline(m,pos)
        newd=self.updateline(0,0,True)
        pygame.draw.line(m,(0,0,0),newd[0],newd[1],1)
            
    def drawline(self,m,pos):
        # m = map(display window)
        # pos = mouse position

        # a linha q vai ser rotacionada
        inil=[[((self.t/2)*1.3),0],[((self.t/2)*1.7),0]]

        # mouse position
        p=list(pos)

        # 
        v2=[p[0]-self.x,p[1]-self.y]

        # a=np.arccos(((v1[0]*v2[0])+(v1[1]*v2[1]))/((((v1[0]**2)+(v1[1]**2))**(1/2))*(((v2[0]**2)+(v2[1]**2))**(1/2)))) com v1=[1,0]:
        a=np.arccos(v2[0]/(((v2[0]**2)+(v2[1]**2))**(1/2)))

        # check if angle is negative or positive
        if v2[1]<0: a=(-a)

        newx=[]
        newy=[]

        # rotaciona os 2 pontos
        e=np.exp((complex(0,1))*a)
        for point in inil:
            newp=complex(point[0],point[1])*e
            newx.append(newp.real)
            newy.append(newp.imag)

        # bota os pontos no lugar certo e update linha
        p1=[int(newx[0]+self.x),int(newy[0]+self.y)]
        p2=[int(newx[1]+self.x),int(newy[1]+self.y)]
        self.d=[p1,p2]

    def check(self,l,pos):
        # ve se o mouse ta em cima de algum personagem
        teste=False
        for p in l:
            if pos[0]>=p.tx:
                if pos[0]<=(p.tx+p.t):
                    if pos[1]>=p.ty:
                        if pos[1]<=(p.ty+p.t):
                            teste=True
                            return p.n
        if not teste: return ('n')
    
    def collisions(self,players,objects):
        # check 1
        for p in players:
            if p.n!=self.n:
                x=(self.x-p.x)
                y=(self.y-p.y)
                d=(((x**2)+(y**2))**(1/2))
                if d<=((((self.t/2)*1.3)+((p.t/2)*1.3))): return True

        # check 2
        for Tipo in objects:
            for Object in objects[Tipo]:
                d=((((self.x-Object.c[0])**2)+((self.y-Object.c[1])**2))**(1/2))
                if d<=((((self.t/2)*1.3)+((Object.t*0.8)))): return True

        # check 3
        x=(self.x-self.cr[0])
        y=(self.y-self.cr[1])
        d=(((x**2)+(y**2))**(1/2))
        if d>=(((self.t*self.v)-((self.t/2)*1.3))): return True

        # se n sair ate aqui: return contanct=False, pq n encostou em nada
        return False

    def move(self,m,l,ws,Back,background=False):
        # ws = window_size
        # m = map(display window)
        # l = lista de personagens
        # Back = all background objects
        # background = Fasle(n tem imagem) ou um png

        # update hitbox color
        self.hc=(0,255,0)
        for p in l:
            if p.n!=self.n:
                p.hc=(255,0,0)

        # update range
        for p in l: p.cr=[p.x,p.y]

        run=True
        Clk=True
        while run:
            # update old x,y
            oldx=self.x
            oldy=self.y

            # draw background
            if isinstance(background,bool):
                pygame.time.delay(15)
                pygame.draw.rect(m,(200,255,200),(0,0,ws[0],ws[1]))
            else:
                # aumentei o delay pq usar png na imagem deixa tudo mais lento
                pygame.time.delay(15)
                m.blit(background,(0,0))

            # draw todo mundo menos quem vc ta controlando
            for player in l:
                if player.n!=self.n:
                    player.draw(m)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            
            # pega as informações do teclado e mouse
            k=pygame.key.get_pressed()
            pos=pygame.mouse.get_pos()

            # ve se vc clicou com o mouse
            click=pygame.mouse.get_pressed()
            if (list(click)[0]==1):
                if Clk:
                    # printa o nome do personagem q vc clicou e muda a cor da hitbox dele pra amarelo
                    n=self.check(l,list(pygame.mouse.get_pos()))
                    if n!='n':
                        for p in l:
                            if p.n==n: p.hc=(255,255,0)
                        print('clicou em',n)
                    Clk=False
            else: Clk=True

            # move camera
            allx=0
            ally=0
            if k[pygame.K_a]: allx=-5
            if k[pygame.K_d]: allx=5
            if k[pygame.K_w]: ally=-5
            if k[pygame.K_s]: ally=5
            for p in l:
                p.x+=allx
                p.y+=ally
            cr=self.cr
            cr[0]+=allx
            cr[1]+=ally
            self.cr=cr
            for x in l:
                if x.n!=self.n:
                    x.updateline(allx,ally)

            # draw all rocks and things
            for Tipo in Back:
                for Object in Back[Tipo]:
                    Object.draw(m,allx,ally)
            
            # move player
            if k[pygame.K_LEFT]: self.x-=5
            if k[pygame.K_RIGHT]: self.x+=5
            if k[pygame.K_UP]: self.y-=5
            if k[pygame.K_DOWN]: self.y+=5
            if k[pygame.K_SPACE]:
                run=False
                # update centro do range
                self.cr=[self.x,self.y]

            # update hitbox
            self.draw(m,False,False)

            # check colisions
            contact=self.collisions(l,Back)
            
            # update x,y if not in contact
            if not contact:
                oldx=self.x
                oldy=self.y
            else:
                self.x=oldx
                self.y=oldy
            
            # draw quem vc tá controlando
            self.draw(m,pos)

            # draw todos os personagens com circulo azul e linha de direção
            if not run:
                self.drawline(m,pos)
                for p in l:
                    p.hc=(0,0,255)
                    p.draw(m,False)
            
            # draw range
            else: pygame.draw.circle(m,(0,0,0),(tuple(cr)),(int(self.t*self.v)),2)
            pygame.display.update((0,0,ws[0],ws[1]))