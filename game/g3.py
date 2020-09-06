import pygame

class Personagem:
    def __init__(self,sprite,x,y,nome,velocidade):
        self.x=x
        self.y=y
        self.sp=sprite
        self.n=nome
        self.v=velocidade
        self.hit=(self.x,self.y,60,60)

    def draw(self,m,p=False,DRAW=True):
        if DRAW: m.blit(self.sp,(self.x,self.y))
        self.hit=(self.x-8,self.y-8,60,60)
        if isinstance(p,bool):
            if p: c=(0,255,0)
            else: c=(255,0,0)
        else: c=(0,0,255)
        #pygame.draw.rect(m,c,self.hit,3)
        self.drawhit(60,m,c,DRAW)

    def drawhit(self,t,m,c,DRAW):
        l=[]
        y=t/((2/(2**(1/2)))+1)
        t2=(((y**2)/2)**(1/2))
        l.append((((self.x+25)+(y/2)),((self.y+25)-(t/2))))
        a=1
        while a<8:
            b='{0:03b}'.format(a)
            d1=int(float(b[0]))
            d2=int(float(b[1]))
            d3=int(float(b[2]))
            if d3==1:
                X=t2
                Y=t2
            else:
                if d2==1:
                    X=0
                    Y=y
                else:
                    X=y
                    Y=0
            if d1==1: Ym=-1
            else: Ym=1
            if d1==d2: Xm=1
            else: Xm=-1
            l.append(((l[a-1][0]+(X*Xm)),(l[a-1][1]+(Y*Ym))))
            a+=1
        hits[self.n]=l
        self.l=l
        self.c=[(self.x+25),(self.y+25)]
        if DRAW: pygame.draw.polygon(m,c,l,1)

    def check(self,P):
        l=self.l
        c=self.c
        ta=True
        for point in l:
            p=list(point)
            i=l.index(point)
            if i==(len(l)-1): i2=0
            else: i2=i+1
            p2=list(l[i2])
            if p2[0]==p[0]: p2[0]+=0.001
            a=((p2[1]-p[1])/(p2[0]-p[0]))
            b=(p[1]-(a*p[0]))
            ty=((c[0]*a)+b)
            teste=(ty-c[1])
            teste2=(((P[0]*a)+b)-P[1])
            if (teste*teste2)<0:
                ta=False
                break
        return ta



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
                    for ps in hits.get(h):
                        C=self.check(list(ps))
                        if C:
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
p1=Personagem(pygame.image.load('hat.png'),100,200,'mago',15)
p2=Personagem(pygame.image.load('hel.png'),400,200,'fighter',10)
p3=Personagem(pygame.image.load('asa.png'),200,400,'assassin',20)
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
