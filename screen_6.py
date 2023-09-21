import always
import pygame

screen_6 = always.SCREEN_6
outside_rect_size_x = 1050
outside_rect_size_y = 150
iner_rect_size_x = outside_rect_size_x - 40
iner_rect_size_y = outside_rect_size_y - 40
outside_rect_x = 100
outside_rect_y = 100

# text3 = pygame.Rect(screen_6, always.SQUARE_COLOR, pygame.Rect(outside_rect_x + 300, 520, outside_rect_size_x - 600 + outside_rect_x + 300, outside_rect_size_y - 20 + 520))


def open_screen_6():
    pygame.init()
    # dict_6 = {'running': True}
    screen_6.fill(always.BACKGROUND_COLOR)
    draw_outside_rect_6()
    draw_iner_rect_6()
    text_6()
    pygame.display.flip()
    # always.PEOPLE_LIST[always.subject].remove(always.PEOPLE_LIST[always.PEOPLE_LIST][1])
    # while dict_6['running']:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             dict_6['running'] = False

def draw_outside_rect_6():
    pygame.draw.rect(screen_6, always.SQUARE_COLOR, pygame.Rect(outside_rect_x, outside_rect_y, outside_rect_size_x, outside_rect_size_y))
    pygame.draw.rect(screen_6, always.SQUARE_COLOR, pygame.Rect(outside_rect_x + 100, 315, outside_rect_size_x - 200, outside_rect_size_y - 10))
    pygame.draw.rect(screen_6, always.SQUARE_COLOR, pygame.Rect(outside_rect_x + 300, 520, outside_rect_size_x - 600, outside_rect_size_y - 20))

def draw_iner_rect_6():
    pygame.draw.rect(screen_6, always.INER_SQUARE_COLOR, pygame.Rect(outside_rect_x + 20, outside_rect_y + 20, outside_rect_size_x - 40, outside_rect_size_y - 40))
    pygame.draw.rect(screen_6, always.INER_SQUARE_COLOR, pygame.Rect(outside_rect_x + 120, 335, outside_rect_size_x - 240, outside_rect_size_y - 50))
    pygame.draw.rect(screen_6, always.INER_SQUARE_COLOR, pygame.Rect(outside_rect_x + 320, 540, outside_rect_size_x - 640, outside_rect_size_y - 60))

def text_6():
    Font = pygame.font.SysFont(always.FONT_NAME, 55)
    text1 = Font.render("Thank you for choosing MATCH!", True, always.FONT_COLOR)
    screen_6.blit(text1, (215, 145))
    Font1 = pygame.font.SysFont(always.FONT_NAME, 50)
    text2 = Font1.render("Your MATCH is:", True, always.FONT_COLOR)
    screen_6.blit(text2, (430, 357))
    Font2 = pygame.font.SysFont(always.FONT_NAME, 40)
    text3 =Font2.render(str(always.PEOPLE_LIST[always.subject][1]), True, always.FONT_COLOR)
    screen_6.blit(text3, (425, 560))


