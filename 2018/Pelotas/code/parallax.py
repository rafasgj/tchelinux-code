"""Implementa um campo de estrelas."""

from random import randrange, choice
import sys
import pygame
pygame.init()


FPS = 30
MAX_STARS = 250
STAR_SPEED = 2
BLACK = (0, 0, 0)


def create_star(x):
    """Create a start at the given X position."""
    # a star is (x, y, speed, magnitude, color)
    return [x, randrange(0, height-1), choice([1, 2, 3]),
            choice([1, 2, 3]), (choice([100, 200, 250]),)*3]


size = width, height = (960, 600)

stars = [create_star(randrange(0, width-1)) for star in range(MAX_STARS)]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Parallax Starfield Simulation")

clock = pygame.time.Clock()

while True:
    # Lock the framerate
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    stars = [[x-speed, y, speed, mag, color]
             if x-speed > 0
             else create_star(width)
             for x, y, speed, mag, color in stars]

    screen.fill(BLACK)
    for x, y, speed, magnitude, color in stars:
        rect = (x, y, magnitude, magnitude)
        screen.fill(color, rect)

    pygame.display.flip()
