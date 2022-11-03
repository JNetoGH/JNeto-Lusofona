import pygame, sys
from pygame.locals import *
import math
import numpy

class Entity:
    def __init__(self, initial_pos: list):
        self.position = initial_pos
        self.is_released = False


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,600))
ang_in_rad = 0
ang_in_degree = 0
circle_ray = 100

isGoingToRight: bool = True

# TEXT
textX, textY = 400, 100
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('press A or D to change the direction', True, (0, 255, 0), (0, 0, 128))
textRect = text.get_rect()
textRect.center = (textX // 2, textY // 2)

my_circle = Entity([0,0])
forca = 15
released_angle = 0
has_already_released_circle = False

while True:  # Main loop--

    DISPLAYSURF.fill((0, 0, 0))

    # shows the text
    DISPLAYSURF.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_a:
                isGoingToRight = False
            elif event.key == pygame.K_d:
                isGoingToRight = True
            elif event.key == pygame.K_r:
                my_circle.is_released = True

    dimensions = pygame.display.get_window_size()

    if isGoingToRight:
        ang_in_rad = ang_in_rad - numpy.pi / 10  # incrementa o angulo em 18º, pois, pi == 180º => pi/10 == 18º
    else:
        ang_in_rad = ang_in_rad + numpy.pi / 10  # incrementa o angulo em 18º, pois, pi == 180º => pi/10 == 18º
    ang_in_degree = numpy.degrees(ang_in_rad)

    x = (dimensions[0] / 2) + math.sin(ang_in_rad) * circle_ray  # formula: x = centro + sin(ang) * ray
    y = (dimensions[1] / 2) + math.cos(ang_in_rad) * circle_ray  # formula: y = centro + cos(ang) * ray



    if not my_circle.is_released:
        my_circle.position = [x, y]
        print(ang_in_rad)
        print(ang_in_degree)
    else:
        if not has_already_released_circle:
            released_angle = ang_in_degree
            has_already_released_circle = True
            print()
            print(released_angle)
            print()

    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), [dimensions[0] / 2, dimensions[1] / 2], circle_ray, 1)
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), [dimensions[0] / 2, dimensions[1]/2], my_circle.position, 5)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255),  my_circle.position, 5, 2)

    pygame.time.Clock().tick(15)
    pygame.display.update()