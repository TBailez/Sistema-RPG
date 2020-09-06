import pygame
import numpy as np
import cmath

class Personagem:
    def __init__(self,sprite,x,y,nome,velocidade,tamanho):
        self.x=x
        self.y=y
        self.sp=sprite
        self.n=nome
        self.v=velocidade
        self.t=tamanho
        self.d=[[0,0],[0,0]]
        self.hit=(self.x,self.y,60,60)

    def draw(self,m,pos=False,p=False,DRAW=True):
        if DRAW: m.blit(self.sp,(self.x,self.y))
        self.hit=(self.x-8,self.y-8,60,60)
        if isinstance(p,bool):
            if p:
                c=(0,255,0)
                if isinstance(pos,bool): pygame.draw.line(m,(0,0,0),self.d[0],self.d[1],1)
                else: self.drawline(pos,m)
            else:
                c=(255,0,0)
                pygame.draw.line(m,(0,0,0),self.d[0],self.d[1],1)
        else: c=(0,0,255)
        hits[self.n]={'centro': [int(self.x+(self.t/2)),int(self.y+(self.t/2))],'raio':int(self.t/2)}
        if DRAW: pygame.draw.circle(m,c,(int(self.x+(self.t/2)),int(self.y+(self.t/2))),int((self.t/2)*1.3),2)
        #print('pos:',pos)
        if isinstance(pos,bool): pass
        else: self.drawline(pos,m)
            
    def drawline(self,md,m,save=False):
        inil=[[((self.t/2)*1.3),0],[((self.t/2)*1.7),0]]
        v1=[1,0]
        p=list(md)
        v2=[(p[0]-(self.x+(self.t/2))),(p[1]-(self.y+(self.t/2)))]
        a=np.arccos(((v1[0]*v2[0])+(v1[1]*v2[1]))/((((v1[0]**2)+(v1[1]**2))**(1/2))*(((v2[0]**2)+(v2[1]**2))**(1/2))))
        if v2[1]<0: a=(-a)
        newx=[]
        newy=[]
        e=np.exp((complex(0,1))*a)
        for point in inil:
            newp=complex(point[0],point[1])*e
            newx.append(newp.real)
            newy.append(newp.imag)
        p1=((newx[0]+self.x+(self.t/2)),(newy[0]+self.y+(self.t/2)))
        p2=((newx[1]+self.x+(self.t/2)),(newy[1]+self.y+(self.t/2)))
        if save: return [p1,p2]
        else: pygame.draw.line(m,(0,0,0),p1,p2,1)

    def check(self,c,r):
        p1=[(self.x+(self.t/2)),(self.y+(self.t/2))]
        x=abs(p1[0]-c[0])
        y=abs(p1[1]-c[1])
        d=(((x**2)+(y**2))**(1/2))
        if d>(int(self.t/2)+r): return True
        else: return False

    def check2(self,cr):
        #cr = centro do range
        #rd= range distance
        cp=[(self.x+(self.t/2)),(self.y+(self.t/2))]
        #cp = centro do personagem
        x=abs(cp[0]-cr[0])
        y=abs(cp[1]-cr[1])
        d=(((x**2)+(y**2))**(1/2))
        if d<=(int((self.t*self.v)-(self.t/2))): return True
        else: return False

    def move(self,m,l):
        run=True
        cr=[int(self.x+(self.t/2)),int(self.y+(self.t/2))]
        dr=int(self.t*self.v)
        while run:
            pygame.time.delay(30)
            m.fill((200,255,200))
            for S in l:
                if S.n!=self.n:
                    S.draw(m)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            k=pygame.key.get_pressed()
            if k[pygame.K_LEFT]: self.x-=15
            if k[pygame.K_RIGHT]: self.x+=15
            if k[pygame.K_UP]: self.y-=15
            if k[pygame.K_DOWN]: self.y+=15
            if k[pygame.K_SPACE]: run=False
            pos=pygame.mouse.get_pos()
            self.draw(m,False,True,False)
            go=self.check2(cr)
            contact=False
            for h in hits:
                if h!=self.n:
                    C=self.check(hits[h].get('centro'),hits[h].get('raio'))
                    if not C:
                        contact=True
                        break
            if go and (not contact):
                oldx=self.x
                oldy=self.y
            else:
                self.x=oldx
                self.y=oldy
            self.draw(m,pos,True)
            if not run:
                self.d=self.drawline(pos,m,True)
                for p in l: p.draw(m,False,'i')
            else:
                pygame.draw.circle(m,(0,0,0),(tuple(cr)),dr,2)
            pygame.display.update()


hits={}
p1=Personagem(pygame.image.load('game/hat.png'),100,200,'mago',3,50)
p2=Personagem(pygame.image.load('game/hel.png'),400,200,'fighter',2,50)
p3=Personagem(pygame.image.load('game/asa.png'),200,400,'assassin',5,50)
l=[p1,p2,p3]
window_size=(600,600)
D=pygame.display.set_mode(window_size)
D.fill((200,255,200))
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
