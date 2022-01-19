import pygame
import random

BLACK = (0,0,0)
WHITE = (200,200,200)
stars = [[]]
count = 0

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            stars[count].append(list(event.pos))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                stars.append([])
                count+=1
    screen.fill(BLACK)
    for array in stars:
        for dot in array:
            pygame.draw.circle(screen, WHITE, dot, random.randint(3, 5))
        if (len(array) >= 2):
            pygame.draw.aalines(screen, WHITE, False, array)


    pygame.display.flip()
    clock.tick(10)