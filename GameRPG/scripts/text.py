import pygame

# printa os textos na tela
def texto(txt,textos,D,window_size,font,tat):
    # adiciona o texto dado a lista de textos
    textos.insert(0,txt)

    # draw area de texto
    pygame.draw.rect(D,(0,0,0),(window_size[0],0,tat,window_size[1]))

    # print all texts
    for t in textos:
        # ve qual é a posição do texto dentro da lista
        n=textos.index(t)

        #criando o texto
        text = font.render(t, True, (255,255,255))

        #criando retangulo do texto
        textRect = list(text.get_rect())
        # rect = (x do canto superior direito,y do canto superior direito,largura do texto,altura do texto)
        rect=(window_size[0]+10 , ((window_size[1]-50)-(n*(textRect[3]))-10) , textRect[2] , textRect[3])

        #display do texto
        D.blit(text,rect)
        pygame.display.update()