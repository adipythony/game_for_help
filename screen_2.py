import always
import pygame

pygame.init()
screen2 = always.SCREEN_2
helper = pygame.Rect((100, 125), (550, 625))
helped = pygame.Rect((700, 125), (1150, 625))


def background():
    # dict_2 = {'running': True}
    screen2.fill(always.BACKGROUND_COLOR)
    squares()
    text()
    pygame.display.flip()
    # while dict_2['running']:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             dict_2['running'] = False


def squares():
    pygame.draw.rect(screen2, always.SQUARE_COLOR, pygame.Rect((100, 125), (450, 500)))
    pygame.draw.rect(screen2, always.INER_SQUARE_COLOR, pygame.Rect((120, 145), (410, 460)))

    pygame.draw.rect(screen2, always.SQUARE_COLOR, pygame.Rect((700, 125), (450, 500)))
    pygame.draw.rect(screen2, always.INER_SQUARE_COLOR, pygame.Rect((720, 145), (410, 460)))
    return


def text():
    font = pygame.font.SysFont(always.FONT_NAME, 80)
    helping = font.render("Helper", True, always.FONT_COLOR)
    screen2.blit(helping, (195, 340))
    helped = font.render("Need Help", True, always.FONT_COLOR)
    screen2.blit(helped, (738, 340))
    return
