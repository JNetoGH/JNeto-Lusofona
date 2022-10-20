import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
ang = 0
circle_ray = 100

isGoingToRight:bool = True

while True:  # Main loop--



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_a:
                isGoingToRight = False
            elif event.key == pygame.K_d:
                isGoingToRight = True
                
    DISPLAYSURF.fill((0, 0, 0))
    dimensions = pygame.display.get_window_size()

    if isGoingToRight:
        ang = ang - numpy.pi / 10  # incrementa o angulo em 18º, pois, pi == 180º => pi/10 == 18º
    else:
        ang = ang + numpy.pi / 10  # incrementa o angulo em 18º, pois, pi == 180º => pi/10 == 18º

    x = (dimensions[0] / 2) + math.sin(ang) * circle_ray  # formula: x = centro + sin(ang) * ray
    y = (dimensions[1] / 2) + math.cos(ang) * circle_ray  # formula: y = centro + cos(ang) * ray

    pygame.draw.circle(DISPLAYSURF, (255,255,255), [dimensions[0] / 2, dimensions[1] / 2], circle_ray, 1)
    pygame.draw.line(DISPLAYSURF, (255,0,0), [dimensions[0] / 2, dimensions[1]/2] , [x,y], 5)

    pygame.time.Clock().tick(15)
    pygame.display.update()