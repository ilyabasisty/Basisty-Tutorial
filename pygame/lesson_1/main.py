import pygame
from settings import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.move()
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (int(player.x), int(player.y), SIZE, SIZE), 1)


    pygame.display.flip()
    clock.tick(FPS)
