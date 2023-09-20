import pygame
WIDTH = 1250
HEIGHT = 750
SCREEN_1 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_2 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_3 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_4 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_5 = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_6 = pygame.display.set_mode((WIDTH, HEIGHT))


BACKGROUND_COLOR = (143, 188, 143)
SQUARE_COLOR = (83, 134, 139)
INER_SQUARE_COLOR = (173, 216, 230)
FONT_COLOR = (255, 255, 255)
FONT_NAME = "freesansbold.ttf"

SUBJECT_DICT = {"Math": 0, "English": 1, "History": 2, "Hebrew": 3, "Bible": 4, "Literature": 5, "Citizenship": 6}
PEOPLE_LIST = [[], [], [], [], [], [], []]
