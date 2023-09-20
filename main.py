import pygame
import screen_1
import screen_2

state = {"running": True}


def main():
    screen_1.draw_screen_1()
    pygame.init()
    screen_1.draw_screen_1()
    while state["running"]:
        event()


def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["running"] = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if screen_1.start.collidepoint(pos):
                screen_2.background()

main()