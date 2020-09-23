import pygame 


def main(D1):
    screen = D1
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(505, 465, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    tx = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Selecionar a caixa de input
                if input_box.collidepoint(event.pos):
                    # Ativa a caixa para escrever
                    active = not active
                else:
                    active = False
                # Aletera a cor para saber que foi selecionada
                color = color_active if active else color_inactive
                # Escreve o txo
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(tx)
                        tx = ''
                    elif event.key == pygame.K_BACKSPACE:
                        tx = tx[:-1]
                    else:
                        tx += event.unicode

        # Renderiza o txo
        txt_surface = font.render(tx, True, color)
        # Altera o tamanho da caixa caso necessario
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Montar o txo
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Montar a caixa
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
