import always
import pygame

screen_6 = always.SCREEN_6

def open_screen_3():
    pygame.init()
    dict_6 = {'running': True}
    screen_6.fill(always.BACKGROUND_COLOR)
    pygame.display.flip()
    while dict_6['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_6['running'] = False