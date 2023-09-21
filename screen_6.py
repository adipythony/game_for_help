import always
import pygame

screen_6 = always.SCREEN_6
outside_rect_size_x = 1050
outside_rect_size_y = 150
iner_rect_size_x = outside_rect_size_x - 40
iner_rect_size_y = outside_rect_size_y - 40
outside_rect_x = 100
outside_rect_y = 100

def open_screen_6():
    pygame.init()
    dict_6 = {'running': True}
    screen_6.fill(always.BACKGROUND_COLOR)
    draw_outside_rect_6()
    draw_iner_rect_6()
    pygame.display.flip()
    while dict_6['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_6['running'] = False

def draw_outside_rect_6():
    pygame.draw.rect(screen_6, always.SQUARE_COLOR, pygame.Rect(outside_rect_x, outside_rect_y, outside_rect_size_x, outside_rect_size_y))
    pygame.draw.rect(screen_6, always.SQUARE_COLOR, pygame.Rect(outside_rect_x + 100, 315, outside_rect_size_x - 200, outside_rect_size_y - 10))
    pygame.draw.rect(screen_6, always.SQUARE_COLOR, pygame.Rect(outside_rect_x + 300, 520, outside_rect_size_x - 600, outside_rect_size_y - 20))

def draw_iner_rect_6():
    pygame.draw.rect(screen_6, always.INER_SQUARE_COLOR, pygame.Rect(outside_rect_x + 20, outside_rect_y + 20, outside_rect_size_x - 40, outside_rect_size_y - 40))
    pygame.draw.rect(screen_6, always.INER_SQUARE_COLOR, pygame.Rect(outside_rect_x + 120, 335, outside_rect_size_x - 240, outside_rect_size_y - 50))
    pygame.draw.rect(screen_6, always.INER_SQUARE_COLOR, pygame.Rect(outside_rect_x + 320, 540, outside_rect_size_x - 640, outside_rect_size_y - 60))

open_screen_6()