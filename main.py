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
                    screen_3.open_screen_3()
                    always.next = 2
        else:
            event_2(event)


def event_2(event):
    if always.next == 2:
        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            if screen_3.MATH(pos2):
                always.subject = always.SUBJECT_LIST["Math"]
            if screen_3.BIBLE(pos2):
                always.subject = always.SUBJECT_LIST["Bible"]
            if screen_3.CITIZENSHIP(pos2):
                always.subject = always.SUBJECT_LIST["Citizenship"]
            if screen_3.ENGLISH(pos2):
                always.subject = always.SUBJECT_LIST["English"]
            if screen_3.Hebrew(pos2):
                always.subject = always.SUBJECT_LIST["Hebrew"]
            if screen_3.HISTORY(pos2):
                always.subject = always.SUBJECT_LIST["History"]
            if screen_3.LITERATURE(pos2):
                always.subject = always.SUBJECT_LIST["Literature"]
            screen_2.background()
            always.next = 3
    else:
        event_3(event)


def event_3(event):
    if always.next == 3:
        if event.type == pygame.MOUSEBUTTONUP:
            pos3 = pygame.mouse.get_pos()
            if screen_2.helped.collidepoint(pos3) or screen_2.helper.collidepoint(pos3):
                screen_1.draw_screen_1()


main()
