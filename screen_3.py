import always
import pygame

# text_font = pygame.font.SysFont(always.FONT_NAME, 50)


def open_screen_3():
    screen_3 = always.SCREEN_3
    dict_3 = {'running' : True}
    always.SCREEN_3.fill(always.BACKGROUND_COLOR)
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(50, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(350, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(650, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(950, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(115, 450, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(465, 450, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(815, 450, 250, 200))

    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(70, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(370, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(670, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(970, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(135, 470, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(485, 470, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(835, 470, 210, 160))

    pygame.display.flip()
    while dict_3['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_3['running'] = False
    return always.SCREEN_3

open_screen_3()
