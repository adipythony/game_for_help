import always
import pygame
screen_5 = always.SCREEN_5

def open_screen_5():
    pygame.init()
    dict_5 = {'running': True}
    screen_5.fill(always.BACKGROUND_COLOR)

    pygame.display.flip()
    while dict_5['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_5['running'] = False
    return always.SCREEN_5



open_screen_5()