import pygame

class Personagem:
    def __init__(self,sprite,x,y,nome,velocidade,tamanho):
        self.x=x
        self.y=y
        self.sp=sprite
        self.n=nome
        self.v=velocidade
        self.t=tamanho
        self.hit=(self.x,self.y,60,60)

    def draw(self,m,p=False,DRAW=True):
        if DRAW: m.blit(self.sp,(self.x,self.y))
        self.hit=(self.x-8,self.y-8,60,60)
        if isinstance(p,bool):
            if p: c=(0,255,0)
            else: c=(255,0,0)
        else: c=(0,0,255)
        hits[self.n]={'centro': [int(self.x+(self.t/2)),int(self.y+(self.t/2))],'raio':int(self.t/2)}
        if DRAW: pygame.draw.circle(m,c,(int(self.x+(self.t/2)),int(self.y+(self.t/2))),int((self.t/2)*1.3),2)

    def check(self,c,r):
        p1=[(self.x+(self.t/2)),(self.y+(self.t/2))]
        x=abs(p1[0]-c[0])
        y=abs(p1[1]-c[1])
        d=(((x**2)+(y**2))**(1/2))
        if d>(int(self.t/2)+r): return True
        else: return False

    def move(self,m,l):
        run=True
        while run:
            pygame.time.delay(30)
            m.fill((200,255,200))
            for S in l:
                if S.n!=self.n: S.draw(m)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            k=pygame.key.get_pressed()
            if k[pygame.K_LEFT]: self.x-=self.v
            if k[pygame.K_RIGHT]: self.x+=self.v
            if k[pygame.K_UP]: self.y-=self.v
            if k[pygame.K_DOWN]: self.y+=self.v
            if k[pygame.K_SPACE]: run=False
            
            self.draw(m,True,False)
            contact=False
            for h in hits:
                if h!=self.n:
                    C=self.check(hits[h].get('centro'),hits[h].get('raio'))
                    if not C:
                        contact=True
                        break

            if not contact:
                oldx=self.x
                oldy=self.y
            else:
                self.x=oldx
                self.y=oldy
            self.draw(m,True)
            if not run:
                for p in l: p.draw(m,'i')
            pygame.display.update()


hits={}
p1=Personagem(pygame.image.load('hat.png'),100,200,'mago',15,50)
p2=Personagem(pygame.image.load('hel.png'),400,200,'fighter',10,50)
p3=Personagem(pygame.image.load('asa.png'),200,400,'assassin',20,50)
l=[p1,p2,p3]
D=pygame.display.set_mode((600,600))
D.fill((200,255,200))
for p in l: p.draw(D,'i')
pygame.display.update()
vez=0
while True:
    for p in l:
        print(p.n,'vai mover?') 
        o=input()
        if o=='s': p.move(D,l)
    print('outro turno')

D.quit()
