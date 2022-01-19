import pygame

BLACK = (0,0,0)
WHITE = (200,200,200)
stars = []

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                stars.append(list(event.pos))
    screen.fill(BLACK)
    for dot in stars:
        pygame.draw.circle(screen, WHITE, dot, 3)
    if (len(stars) >= 2):
        pygame.draw.lines(screen, WHITE, False, stars)

    pygame.display.flip()
    clock.tick(30)