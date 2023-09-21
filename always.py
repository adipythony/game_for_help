import pygame
WIDTH = 1250
HEIGHT = 750
SCREEN_1 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_2 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_3 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_4 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_5 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_6 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_7 = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = (230, 230, 250)
SQUARE_COLOR = (137, 104, 205)
INER_SQUARE_COLOR = (171,130,255)
FONT_COLOR = (255, 255, 255)
FONT_NAME = "georgia"

next = 1

SUBJECT_LIST = {"Math": 0, "English": 1, "Literature": 2, "Bible": 5, "Citizenship": 6, "History": 2, "Hebrew": 4}
PEOPLE_LIST = [[], [], [], [], [], [], []]
subject = 6
