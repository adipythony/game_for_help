import pygame
import always
import screen_1
import screen_2
import screen_3
import screen_4
import screen_6
import screen_7

state = {"running": True}


def main():
    screen_1.draw_screen_1()
    pygame.init()
    pygame.display.set_caption("The Help Center")
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
            if screen_3.MATH.collidepoint(pos2):
                always.subject = always.SUBJECT_LIST["Math"]
            if screen_3.BIBLE.collidepoint(pos2):
                always.subject = always.SUBJECT_LIST["Bible"]
            if screen_3.CITIZENSHIP.collidepoint(pos2):
                always.subject = always.SUBJECT_LIST["Citizenship"]
            if screen_3.ENGLISH.collidepoint(pos2):
                always.subject = always.SUBJECT_LIST["English"]
            if screen_3.Hebrew.collidepoint(pos2):
                always.subject = always.SUBJECT_LIST["Hebrew"]
            if screen_3.HISTORY.collidepoint(pos2):
                always.subject = always.SUBJECT_LIST["History"]
            if screen_3.LITERATURE.collidepoint(pos2):
                always.subject = always.SUBJECT_LIST["Literature"]
            screen_2.background()
            always.next = 3
    else:
        event_3(event)


def event_3(event):
    if always.next == 3:
        if event.type == pygame.MOUSEBUTTONUP:
            pos3 = pygame.mouse.get_pos()
            if screen_2.helped.collidepoint(pos3):
                screen_4.open_screen_4()
            if screen_2.helper.collidepoint(pos3):
                if len(always.PEOPLE_LIST[always.subject]) != 1:
                    screen_6.open_screen_6()
                else:
                    screen_7.open_screen_7()



main()
