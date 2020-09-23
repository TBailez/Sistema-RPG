import pygame

d=pygame.display.set_mode((900,900))
objects={}
t=15
Clk=True
while True:
    pygame.time.delay(15)
    k=pygame.key.get_pressed()
    pos=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    x=0
    y=0
    if k[pygame.K_a]: x=5
    if k[pygame.K_d]: x=-5
    if k[pygame.K_w]: y=5
    if k[pygame.K_s]: y=-5
    if k[pygame.K_UP]: t+=2
    if k[pygame.K_DOWN]:
        if t>=3: t-=2
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            break
    newpos=((list(pos)[0]+x),((list(pos)[1]+y)))
    d.fill((0,0,0))
    for o in objects:
        if o=='arvores':
            for a in objects.get(o):
                npos=((list(a.get('centro'))[0]+x),(list(a.get('centro'))[1]+y))
                i=objects.get(o).index(a)
                objects['arvores'][i]['centro']=npos
                #A={'centro':npos,'tamanho':a.get('tamanho')}
                pygame.draw.circle(d,(150,100,40),npos,a.get('tamanho'))
    pygame.draw.circle(d,(150,100,40),newpos,t)
    pygame.display.update() 
    if (list(click)[0]==1):
        if Clk:
            c={'centro':newpos,'tamanho':t}
            try: x=type(objects['arvores'])
            except: objects['arvores']=[c]
            else: objects['arvores'].append(c)
            t=15
            Clk=False
    else: Clk=True
