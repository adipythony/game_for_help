import always
import pygame

pygame.init()
screen1 = always.SCREEN_1

text_font = pygame.font.SysFont(always.FONT_NAME, 50)
RECT_WIDTH = 850
RECT_LENGTH = 200
RECT_LOCATION_X = (always.WIDTH - RECT_WIDTH) / 2
RECT_LOCATION_Y = (always.HEIGHT - RECT_LENGTH) / 2
start = pygame.Rect((RECT_LOCATION_X, RECT_LOCATION_Y), (RECT_LOCATION_X + RECT_WIDTH, RECT_LOCATION_Y + RECT_LENGTH))


def draw_text(text, font, text_col, x, y):
    txt = font.render(text, True, text_col)
    screen1.blit(txt, (x, y))


def draw_screen_1():
    always.SCREEN_1.fill(always.BACKGROUND_COLOR)
    pygame.draw.rect(screen1, always.SQUARE_COLOR, pygame.Rect(RECT_LOCATION_X, RECT_LOCATION_Y, RECT_WIDTH, RECT_LENGTH))
    draw_text("Begin Helping Process", text_font, always.FONT_COLOR, RECT_LOCATION_X + 200, RECT_LOCATION_Y + 70)
    draw_text("Welcome to the helping center !", text_font, always.FONT_COLOR, 300, 100)
    pygame.display.flip()

