import always
import pygame

pygame.init()
screen_1 = always.SCREEN_1

text_font = pygame.font.SysFont(always.FONT_NAME, 48)
RECT_WIDTH = 480
RECT_LENGTH = 185
RECT_LOCATION_X = 405
RECT_LOCATION_Y = 430
start = pygame.Rect((RECT_LOCATION_X, RECT_LOCATION_Y), (RECT_LOCATION_X + RECT_WIDTH, RECT_LOCATION_Y + RECT_LENGTH))


def draw_text(text, font, text_col, x, y):
    txt = font.render(text, True, text_col)
    screen_1.blit(txt, (x, y))


def draw_screen_1():
    pygame.init()
    # dict_1 = {'running': True}
    always.SCREEN_1.fill(always.BACKGROUND_COLOR)
    draw_outside_rect_1()
    draw_iner_rect_1()
    draw_text("Begin Helping Process", text_font, always.FONT_COLOR, RECT_LOCATION_X + 25, RECT_LOCATION_Y + 70)
    text_font2 = pygame.font.SysFont(always.FONT_NAME, 60)
    draw_text("Welcome to the helping center!", text_font2, always.FONT_COLOR, 250, 200)
    pygame.display.flip()
    # while dict_1['running']:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             dict_1['running'] = False
    # return always.SCREEN_1


def draw_outside_rect_1():
    pygame.draw.rect(screen_1, always.SQUARE_COLOR, pygame.Rect(RECT_LOCATION_X, RECT_LOCATION_Y, RECT_WIDTH, RECT_LENGTH))
    pygame.draw.rect(screen_1, always.SQUARE_COLOR, pygame.Rect((200, 100), (850, 270)))


def draw_iner_rect_1():
    pygame.draw.rect(screen_1, always.INER_SQUARE_COLOR, pygame.Rect(RECT_LOCATION_X + 20, RECT_LOCATION_Y + 20, RECT_WIDTH - 40, RECT_LENGTH - 40))
    pygame.draw.rect(screen_1, always.INER_SQUARE_COLOR, pygame.Rect((220, 120), (810, 230)))

