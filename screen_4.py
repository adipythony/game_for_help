import pygame
import sys
import always
import main
import screen_1


pygame.init()

clock = pygame.time.Clock()

screen4 = pygame.display.set_mode((always.WIDTH, always.HEIGHT))

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


def is_enter(user_text):
    always.PEOPLE_LIST[always.subject].append(user_text)


while True:
    for event in pygame.event.get():

        # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:

            if event.type == pygame.K_RETURN:
                is_enter(user_text)
                screen_5
                break

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

    screen4.fill(always.BACKGROUND_COLOR)
    screen_1.draw_text("Enter your email: ", screen_1.text_font, always.FONT_COLOR, 300, 300)

    if active:
        color = color_active
    else:
        color = color_passive

    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen4, color, input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    # render at position stated in arguments
    screen4.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()

    clock.tick(60)
