import always
import pygame
screen_5 = always.SCREEN_5


def open_screen_5():
    pygame.init()
    dict_5 = {'running': True}
    screen_5.fill(always.BACKGROUND_COLOR)
    draw_outside_rect_5()
    draw_iner_rect_5()
    text_5()
    pygame.display.flip()
    while dict_5['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_5['running'] = False
    return always.SCREEN_5


def draw_outside_rect_5():
    pygame.draw.rect(screen_5, always.SQUARE_COLOR, pygame.Rect(200, 125, 850, 500))


def draw_iner_rect_5():
    pygame.draw.rect(screen_5, always.INER_SQUARE_COLOR, pygame.Rect(220, 145, 810, 460))


def text_5():
    Font = pygame.font.SysFont(always.FONT_NAME, 55)
    text = Font.render("We will look for your best MATCH!", True, always.FONT_COLOR)
    screen_5.blit(text, (245, 275))
    Font_2 = pygame.font.SysFont(always.FONT_NAME, 80)
    text_2 = Font_2.render("Good Luck!", True, always.FONT_COLOR)
    screen_5.blit(text_2, (420, 400))
open_screen_5()
