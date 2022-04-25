import pygame
import time
import random

# Snake move speed
snake_speed = 15

# Window Size
window_x = 720
window_y = 480

dark_gray = pygame.Color(0, 0, 0)
purple = pygame.Color(132, 94, 194)
green = pygame.Color(0, 142, 155)
orange = pygame.Color(255, 150, 113)

pygame.init()

# Game window
pygame.display.set_caption('Pastel Snake')
window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# Initial snake position
snake_position = [100,50]

snake_body = [[100,50],[90,50],[80,50],[70,50]]

# Food position
food_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
food_spawn = True

# Snake direction
direction = 'Right'
change_dir = direction