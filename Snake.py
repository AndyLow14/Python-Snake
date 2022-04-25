import sys
from turtle import distance
import pygame
import time
import random
from math import dist
from operator import add

# Snake move speed
snake_speed = 500

# Window Size
window_x = 720
window_y = 480

dark_gray = pygame.Color(18, 18, 18)
white = pygame.Color(255, 255, 255)
orange = pygame.Color(255, 150, 113)

pygame.init()

# Game window
pygame.display.set_caption('Snake')
window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# Initial snake position [x,y]
snake_position = [100,50]
snake_body = [[100,50],[90,50],[80,50],[70,50]]

# Food position [x,y]
food_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
food_spawn = True

# Snake direction
direction = 'RIGHT'
change_to = direction

# Available Moves
moves = [[0,-10], #UP
        [0,10],  #DOWN
        [-10,0], #LEFT
        [10,0]]  #RIGHT

# Main function
while True:

    # # Detect actions
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()

    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_UP:
    #             change_to = 'UP'
    #         if event.key == pygame.K_DOWN:
    #             change_to = 'DOWN'
    #         if event.key == pygame.K_LEFT:
    #             change_to = 'LEFT'
    #         if event.key == pygame.K_RIGHT:
    #             change_to = 'RIGHT'

    # if change_to == 'UP' and direction != 'DOWN':
    #     direction = 'UP'
    # if change_to == 'DOWN' and direction != 'UP':
    #     direction = 'DOWN'
    # if change_to == 'LEFT' and direction != 'RIGHT':
    #     direction = 'LEFT'
    # if change_to == 'RIGHT' and direction != 'LEFT':
    #     direction = 'RIGHT'

    #  # Snake movement
    # if shortest_path == 'UP':
    #     snake_position[1] -= 10
    # if shortest_path == 'DOWN':
    #     snake_position[1] += 10
    # if shortest_path == 'LEFT':
    #     snake_position[0] -= 10
    # if shortest_path == 'RIGHT':
    #     snake_position[0] += 10

    # AI Euclidean Pathfinding
    shortest_path = moves[0]
    shortest_dir = dist(list(map(add, snake_position, moves[0])), food_position)

    for i in range(1,len(moves)):
        distance = dist(list(map(add, snake_position, moves[i])), food_position)
        if distance < shortest_dir:
            shortest_path = moves[i]
            shortest_dir = distance

    snake_position = list(map(add, snake_position, shortest_path))

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        # score += 10
        food_spawn = False
    else:
        snake_body.pop()
         
    if not food_spawn:
        food_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
         
    food_spawn = True
    window.fill(dark_gray)
    
    # Render snake
    for pos in snake_body:
        pygame.draw.rect(window, white, pygame.Rect(pos[0], pos[1], 10, 10))

    # Render food
    food = pygame.Rect(food_position[0], food_position[1], 10, 10)
    pygame.draw.rect(window, orange, food)

    pygame.display.update()
    fps.tick(snake_speed)

