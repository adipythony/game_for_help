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

next = 1

SUBJECT_LIST = {"Math": [], "English": [], "Literature": [], "Bible": [], "Citizenship": [], "History": [], "Hebrew": []}
PEOPLE_LIST = [[], [], [], [], [], [], []]
