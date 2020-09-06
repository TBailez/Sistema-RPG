import pygame
H=pygame.image.load('hat.png')
H2=pygame.image.load('hel.png')

class s:
    def __init__(self,sprite,x,y,nome,velocidade):
        self.x=x
        self.y=y
        self.sp=sprite
        self.n=nome
        self.v=velocidade

class m:
    def __init__(self,l):
        self.M=pygame.display.set_mode((500,500))
        self.l=l

    def move(self,n):
        run=True
        while run:
            pygame.time.delay(100)
            self.M.fill((0,0,0))
            for S in self.l:
                if S.n==n:
                    P=S
                    v=S.v
                else:
                    self.M.blit(S.sp,(S.x,S.y))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            k=pygame.key.get_pressed()
            if k[pygame.K_LEFT]: P.x-=v
            if k[pygame.K_RIGHT]: P.x+=v
            if k[pygame.K_UP]: P.y-=v
            if k[pygame.K_DOWN]: P.y+=v
            if k[pygame.K_SPACE]: run=False
            for S in self.l:
                if S.n==n:
                    self.M.blit(P.sp,(P.x,P.y))
            pygame.display.update()


p1=s(H,100,200,'mago',20)
p2=s(H2,400,200,'fighter',10)
l=[p1,p2]
Ma=m(l)
for p in l:
    Ma.M.blit(p.sp,(p.x,p.y))
pygame.display.update()
sair=False
vez=0
print(l[0].n,'Vai se mover?')
while True:
    pygame.time.delay(1000)
    pygame.event.pump()
    with open('c:/Users/João Pedro/Desktop/game/T.txt') as T:
        t=T.read()
    if len(t)!=0:
        o=t
        t=''
        with open('c:/Users/João Pedro/Desktop/game/T.txt','w') as T:
            T.write(t)
        print('o:',o)
        if o=='s':
            Ma.move(l[vez].n)
        if vez<(len(l)-1): vez+=1
        else: vez=0
        print(l[vez].n,'Vai se mover?')

Ma.M.quit()