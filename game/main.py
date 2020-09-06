import pygame
pygame.init()

def move(x,y,v,c,t,s2):
    run=True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        k=pygame.key.get_pressed()
        if k[pygame.K_LEFT]: x-=v
        if k[pygame.K_RIGHT]: x+=v
        if k[pygame.K_UP]: y-=v
        if k[pygame.K_DOWN]: y+=v
        if k[pygame.K_SPACE]: run=False
        w.fill((0,0,0))
        pygame.draw.rect(w,c,(x,y,t[0],t[1]))
        pygame.draw.rect(w,s2[2],(s2[0],s2[1],s2[3][0],s2[3][1]))
        pygame.display.update()
    return [x,y]


w=pygame.display.set_mode((500,500))
pygame.display.set_caption("teste")
x=400
y=200
x2=100
y2=200
run=True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    pygame.draw.rect(w,(0,0,255),(x,y,50,50))
    pygame.draw.rect(w,(0,255,0),(x2,y2,70,70))
    pygame.display.update()
    
    c=input('deseja mover 1?')
    if c=='s':
        xys=move(x,y,20,(0,0,255),[50,50],[x2,y2,(0,255,0),[70,70]])
        x=xys[0]
        y=xys[1]
    c=input('deseja mover 2?')
    if c=='s':
        xys=move(x2,y2,10,(0,255,0),[70,70],[x,y,(0,0,255),[50,50]])
        x2=xys[0]
        y2=xys[1]
    
pygame.quit()
