import pygame

import always
import screen_1
import screen_2
import screen_3

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
        if always.next == 1:
            if event.type == pygame.MOUSEBUTTONUP:
               pos = pygame.mouse.get_pos()
               if screen_1.start.collidepoint(pos):
                    screen_2.background()
                    always.next = 2
        else:
            event_2(event)


def event_2(event):
    if always.next == 2:
        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            if screen_2.helped.collidepoint(pos2) or screen_2.helper.collidepoint(pos2):
                screen_1.draw_screen_1()


main()
