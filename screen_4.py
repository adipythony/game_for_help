import pygame
import sys
import always
import main
import screen_1
import screen_5
import clock

screen4 = always.SCREEN_4
RECT_WIDTH = 850
RECT_LENGTH = 200
RECT_LOCATION_X = (always.WIDTH - RECT_WIDTH) / 2
RECT_LOCATION_Y = (always.HEIGHT - RECT_LENGTH) / 2
base_font = pygame.font.SysFont(always.FONT_NAME, 32)
user_text = ''
input_rect = pygame.Rect(300, 375, 300, 50)
color_active = pygame.Color(always.INER_SQUARE_COLOR)
color_passive = pygame.Color(always.SQUARE_COLOR)
color = color_passive
active = False

def open_screen_4():
    pygame.init()
    screen4.fill(always.BACKGROUND_COLOR)
    screen_1.draw_text("Enter your email: ", screen_1.text_font, always.FONT_COLOR, 300, 300)
    is_enter(user_text)
    pygame.display.flip()

def is_enter(user_text):
    always.PEOPLE_LIST[always.subject].append(user_text)
    color = color_passive
    active = False
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_enter(user_text)
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen4, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen4.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        clock.tick(60)

# open_screen_4()
