import pygame
import screen_1

state = {"running": True}
def main():
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
            if

main()