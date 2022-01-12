import pygame
from settings import *

class Player:
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.speed = SPEED

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
