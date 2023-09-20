import always
import pygame
screen_3 = always.SCREEN_3
outside_rect_size_x = 250
outside_rect_size_y = 200
iner_rect_size_x = 210
iner_rect_size_y = 160
outside_rect_x = 50
outside_rect_y = 100


MATH = pygame.Rect((outside_rect_x, outside_rect_y), (outside_rect_size_x + outside_rect_x, outside_rect_size_y + outside_rect_y))
ENGLISH = pygame.Rect((outside_rect_x + 300, outside_rect_y), (outside_rect_size_x + outside_rect_x + 300, outside_rect_size_y + outside_rect_y))
HISTORY = pygame.Rect((outside_rect_x + 600, outside_rect_y), (outside_rect_size_x + outside_rect_x + 600, outside_rect_size_y + outside_rect_y))
Hebrew = pygame.Rect((outside_rect_x + 900, outside_rect_y), (outside_rect_size_x + outside_rect_x + 900, outside_rect_size_y + outside_rect_y))
BIBLE = pygame.Rect((outside_rect_x + 65, outside_rect_y + 350), (outside_rect_size_x + outside_rect_x + 65, outside_rect_size_y + outside_rect_y + 350))
LITERATURE = pygame.Rect((outside_rect_x + 415, outside_rect_y + 350), (outside_rect_size_x + outside_rect_x + 415, outside_rect_size_y + outside_rect_y + 350))
CITIZENSHIP = pygame.Rect((outside_rect_x + 765, outside_rect_y + 350), (outside_rect_size_x + outside_rect_x + 765, outside_rect_size_y + outside_rect_y + 350))
def open_screen_3():
    pygame.init()
    screen_3.fill(always.BACKGROUND_COLOR)
    draw_outside_rect_3()
    draw_iner_rect_3()
    text_3()
    pygame.display.flip()



def draw_outside_rect_3():
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(50, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(350, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(650, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(950, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(115, 450, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(465, 450, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(815, 450, 250, 200))
    return


def draw_iner_rect_3():
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(70, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(370, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(670, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(970, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(135, 470, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(485, 470, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(835, 470, 210, 160))
    return


def text_3():
    Font = pygame.font.SysFont(always.FONT_NAME, 50)
    Math = Font.render("Math", True, always.FONT_COLOR)
    screen_3.blit(Math, (125, 175))
    English = Font.render("English", True, always.FONT_COLOR)
    screen_3.blit(English, (405, 175))
    History = Font.render("History", True, always.FONT_COLOR)
    screen_3.blit(History, (700, 175))
    Hebrew = Font.render("Hebrew", True, always.FONT_COLOR)
    screen_3.blit(Hebrew, (995, 175))
    Bible = Font.render("Bible", True, always.FONT_COLOR)
    screen_3.blit(Bible, (190, 525))
    Literature = Font.render("Literature", True, always.FONT_COLOR)
    screen_3.blit(Literature, (500, 525))
    Citizenship = Font.render("Citizenship", True, always.FONT_COLOR)
    screen_3.blit(Citizenship, (835, 525))
    pygame.display.flip()
    return
