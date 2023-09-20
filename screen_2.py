import always
import pygame

pygame.init()
screen2 = always.SCREEN_2

def background():
    screen2.fill(always.BACKGROUND_COLOR)
    squares()
    text()
    pygame.display.flip()

def squares():
    size = (450, 500)
    helper_location = (100, 125)
    needs_help_location = (700, 125)
    pygame.draw.rect(screen2, always.SQUARE_COLOR, pygame.Rect((helper_location), (size)))
    pygame.draw.rect(screen2, always.SQUARE_COLOR, pygame.Rect((needs_help_location), (size)))
    return

def text():
    font = pygame.font.SysFont(always.FONT_NAME, 50)
    helping = font.render("Helper", True, always.FONT_COLOR)
    screen2.blit(helping, (100, 125))
    helped = font.render("Need Help", True, always.FONT_COLOR)
    screen2.blit(helped, (700, 125))
    return

while True:
    background()