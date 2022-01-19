import pygame
import math

BLACK = (0,0,0)
WHITE = (200,200,200)

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(BLACK)
    # LINE
    # pygame.draw.line(screen, WHITE, 
                #  [10, 30], 
                #  [290, 30])
    # pygame.draw.line(screen, WHITE, 
                # [10, 50], 
                # [290, 50], 1)
    # pygame.draw.line(screen, WHITE, 
                    # [10, 70], 
                    # [290, 70], 5)
    # pygame.draw.line(screen, WHITE, 
                    # [10, 90], 
                    # [290, 90], 20)
    
    # LINES
    # pygame.draw.lines(screen, WHITE, True, [[20, 120], [120, 20], [220, 120]])
    # pygame.draw.lines(screen, WHITE, False, [[300, 120], [400, 20], [500, 120]], 3)

    # POLYGON
    # pygame.draw.polygon(screen, WHITE,
    #                 [[20, 120], [120, 20],[220, 120]])

    # RECT
    # pygame.draw.rect(screen, WHITE, (20, 20, 100, 80))
    # pygame.draw.rect(screen, WHITE, (20, 120, 200, 40), 1)
    # pygame.draw.rect(screen, WHITE, (20, 190, 60, 100), 5)

    # CIRCLE
    # pygame.draw.circle(screen, WHITE, 
    #                (100, 100), 40)
    # pygame.draw.circle(screen, WHITE, 
    #                 (210, 100), 45, 2)
    # pygame.draw.circle(screen, WHITE, 
    #                 (300, 100), 30, 9)

    # ELLIPSE
    # pygame.draw.ellipse(screen, WHITE, (20, 40, 250, 100), 3)
    # pygame.draw.ellipse(screen, WHITE, (20, 170, 200, 60))


    # ARC
    # pygame.draw.arc(screen, WHITE,
    #             (30, 40, 200, 70),
    #             0, math.pi)
    # pygame.draw.arc(screen, WHITE,
    #                 (250, 10, 200, 80),
    #                 math.pi, 2*math.pi, 3)
    # pygame.draw.arc(screen, WHITE,
    #                 (30, 100, 170, 60),
    #                 0.3*math.pi, 1.75*math.pi, 5)


    pygame.display.flip()
    clock.tick(30)