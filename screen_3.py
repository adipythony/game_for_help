import always
import pygame


# def draw_screen_1():
#     always.SCREEN_1.fill(always.BACKGROUND_COLOR)
#     pygame.draw.rect(screen1, always.SQUARE_COLOR, pygame.Rect(150, 275, 200, 200))
#     pygame.draw.rect(screen1, always.SQUARE_COLOR, pygame.Rect(650, 275, 200, 200))
#     pygame.display.flip()
#
#
# while True:
#     draw_screen_1()

def open_screen_3():
    screen_3 = always.SCREEN_3
    dict_3 = {'running' : True}
    always.SCREEN_3.fill(always.BACKGROUND_COLOR)
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(50, 237.5, 187.5, 187.5))
    pygame.display.flip()
    while dict_3['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_3['running'] = False
    return always.SCREEN_3

open_screen_3()
