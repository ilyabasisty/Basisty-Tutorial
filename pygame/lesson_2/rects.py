import numbers
import pygame

BLACK = (0,0,0)
WHITE = (200,200,200)
sq_array = [[]]
count = 0
press = False

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                press = True
                sq_array[count] = [event.pos, [0, 0]]
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                press = False
                sq_array.append([])
                count+=1
        if event.type == pygame.MOUSEMOTION:
            if press:
                sq_array[count][1] = list(map(lambda x, y: x - y, event.pos, sq_array[count][0]))
    screen.fill(BLACK)
    for params in sq_array:
        if len(params) == 2:
            pygame.draw.rect(screen, WHITE, (params), 1)

    pygame.display.flip()
    clock.tick(30)