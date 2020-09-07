import numpy as np
import cmath
import pygame

class Personagem:
    def __init__(self,sprite,x,y,nome,velocidade,tamanho):
        # true x,y
        self.tx=x
        self.ty=y
        
        self.sp=sprite
        self.n=nome
        self.v=velocidade
        self.t=tamanho

        # x,y do centro
        self.x=int(x+(self.t/2))
        self.y=int(y+(self.t/2))

        # linha de direção inicial
        self.d=[[0,0],[0,0]]
        
        self.hit=(self.x,self.y,self.t/2)

    def draw(self,m,pos=False,p=False,DRAW=True):
        # m = map(display window)
        # pos = mouse position
        # p = personagem q vc está controlando ou n
        # DRAW = if true: draw things

        # update true x,y
        self.tx=(self.x-(self.t/2))
        self.ty=(self.y-(self.t/2))

        # draw sprite
        if DRAW: m.blit(self.sp,(self.tx,self.ty))
        
        # update hitbox
        self.hit=[self.x,self.y,int((self.t/2)*1.3)]
        
        # define color of hitbox
        if isinstance(p,bool):
            if p: c=(0,255,0)
            else: c=(255,0,0)
        else: c=(0,0,255)
        
        # draw hitbox
        if DRAW: pygame.draw.circle(m,c,(self.x,self.y),self.hit[2],2)
        
        # draw line 
        if not isinstance(pos,bool): self.drawline(m,pos)
        newd=[[int(self.d[0][0]),int(self.d[0][1])],[int(self.d[1][0]),int(self.d[1][1])]]
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

    def check(self,c,r):
        # c = centro do outro personagem
        # r = raio da hitbox do outro personagem
        # ve se a distancia entre os centros de 2 personagens é maior q a hitbox dos 2 juntas

        x=abs(self.x-c[0])
        y=abs(self.y-c[1])
        d=(((x**2)+(y**2))**(1/2))
        if d>((int(self.t/2)*1.3)+r): return True
        else: return False

    def check2(self,cr):
        # cr = centro do range
        # ve se o personagem ta dentro do range

        # centro do personagem
        cp=[self.x,self.y]
        
        x=abs(cp[0]-cr[0])
        y=abs(cp[1]-cr[1])
        d=(((x**2)+(y**2))**(1/2))
        if d<=(int((self.t*self.v)-((self.t/2)*1.3))): return True
        else: return False

    def move(self,m,l):
        # m = map(display window)
        # l = lista de personagens

        run=True

        # define contro do range e range distance
        cr=[self.x,self.y]
        dr=int(self.t*self.v)

        while run:
            pygame.time.delay(10)
            m.fill((200,255,200))

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

            if k[pygame.K_LEFT]: self.x-=5
            if k[pygame.K_RIGHT]: self.x+=5
            if k[pygame.K_UP]: self.y-=5
            if k[pygame.K_DOWN]: self.y+=5
            if k[pygame.K_SPACE]: run=False

            # update hitbox
            self.draw(m,False,True,False)

            # check colisions
            go=self.check2(cr)
            contact=False
            for player in l:
                if player.n!=self.n:
                    C=self.check([player.x,player.y],((player.t/2)*1.3))
                    if not C:
                        contact=True
                        break
            
            # update x,y if not in contact
            if go and (not contact):
                oldx=self.x
                oldy=self.y
            else:
                self.x=oldx
                self.y=oldy
            
            # draw quem vc tá controlando
            self.draw(m,pos,True)

            # draw todos os personagens com circulo azul e linha de direção
            if not run:
                self.drawline(m,pos)
                for p in l: p.draw(m,False,'i')
            
            # draw range
            else:
                pygame.draw.circle(m,(0,0,0),(tuple(cr)),dr,2)

            pygame.display.update()