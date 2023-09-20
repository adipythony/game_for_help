import always
import pygame
screen_7 = always.SCREEN_7

outside_rect_x = 200
outside_rect_y = 200
outside_rect_size_x = 850
outside_rect_size_y = 350

def open_screen_7():
    pygame.init()
    dict_7 = {'running': True}
    screen_7.fill(always.BACKGROUND_COLOR)
    pygame.draw.rect(screen_7, always.SQUARE_COLOR, pygame.Rect(outside_rect_x, outside_rect_y, outside_rect_size_x, outside_rect_size_y))
    pygame.draw.rect(screen_7, always.INER_SQUARE_COLOR, pygame.Rect(outside_rect_x + 20, outside_rect_y + 20, outside_rect_size_x - 40, outside_rect_size_y - 40))
    Font = pygame.font.SysFont(always.FONT_NAME, 50)
    text_7 = Font.render("Sorry, we couldn't find your MATCH yet", True, always.FONT_COLOR)
    screen_7.blit(text_7, (125, 175))
    text_7_1 = Font.render("Come again in the future!", True, always.FONT_COLOR)
    screen_7.blit(text_7_1, (125, 175))
    pygame.display.flip()
    while dict_7['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_7['running'] = False
    return always.SCREEN_7

open_screen_7()