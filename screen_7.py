import always
import pygame
screen_7 = always.SCREEN_7

def open_screen_7():
    pygame.init()
    screen_7.fill(always.BACKGROUND_COLOR)
    pygame.display.flip()