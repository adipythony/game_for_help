import always
import pygame
screen_3 = always.SCREEN_3
x = 150
y = 150
# text_font = pygame.font.SysFont(always.FONT_NAME, 50)
# text = text_font.render('Math', True, always.FONT_COLOR, always.INER_SQUARE_COLOR)
# textRect = text.get_rect()
# textRect.center = (x // 2, y // 2)
# always.SCREEN_3.blit(text, textRect)

def open_screen_3():
    pygame.init()
    dict_3 = {'running' : True}
    screen_3.fill(always.BACKGROUND_COLOR)
    draw_outside_rect()
    draw_iner_rect()
    text()
    pygame.display.flip()
    while dict_3['running']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dict_3['running'] = False
    return always.SCREEN_3



def draw_outside_rect():
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(50, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(350, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(650, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(950, 100, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(115, 450, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(465, 450, 250, 200))
    pygame.draw.rect(screen_3, always.SQUARE_COLOR, pygame.Rect(815, 450, 250, 200))
    return

def draw_iner_rect():
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(70, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(370, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(670, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(970, 120, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(135, 470, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(485, 470, 210, 160))
    pygame.draw.rect(screen_3, always.INER_SQUARE_COLOR, pygame.Rect(835, 470, 210, 160))
    return
def text():
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
    literature = Font.render("literature", True, always.FONT_COLOR)
    screen_3.blit(literature, (500, 525))
    citizenship = Font.render("citizenship", True, always.FONT_COLOR)
    screen_3.blit(citizenship, (835, 525))
    pygame.display.flip()
    return

open_screen_3()