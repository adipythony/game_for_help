import always
import pygame


screen1 = always.SCREEN_1


def draw_screen_1():
    always.SCREEN_1.fill(always.BACKGROUND_COLOR)
    pygame.draw.rect(screen1, always.SQUARE_COLOR, pygame.Rect((always.WIDTH - 850) / 2, (always.HEIGHT - 200) / 2, 850, 200))

    pygame.display.flip()


while True:
    draw_screen_1()
