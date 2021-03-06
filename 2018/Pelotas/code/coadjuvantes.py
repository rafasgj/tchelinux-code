"""Exemplo de adição de um "protagonista" ao jogo."""

from GIFImage import GIFImage

from math import sin, cos, pi
from random import randrange, choice, random
import sys
import pygame

pygame.init()


def create_star(x):
    """Create a star for the background parallax."""
    # a star is (x, y, speed, magnitude, color)
    return [x, randrange(0, height-1), choice([1, 2, 3]),
            choice([1, 2, 3]), (choice([100, 200, 250]),)*3]


class GameObject(object):
    """Define a game object."""

    def __init__(self, imagefile, x, y, speed, animate=False):
        """Initialize game object given an image."""
        if animate:
            self.image = GIFImage(imagefile)
        else:
            self.image = pygame.image.load(imagefile)
        self.bounds = self.image.get_rect()
        self.bounds[0] = x
        self.bounds[1] = y
        self.speed = speed
        self.animate = animate

    def draw(self, surface):
        """Draw the game object in the given surface."""
        if self.animate:
            self.image.draw(surface, self.bounds)
        else:
            surface.blit(self.image, self.bounds)

    def move(self, dx, dy):
        """Move the object by the amount given multiplied by object's speed."""
        self.bounds[0] += dx*self.speed
        self.bounds[1] += dy*self.speed

    def set_position(self, x, y):
        """Move the object absolute position."""
        self.bounds[0] = x
        self.bounds[1] = y

    def get_position(self):
        """Retrieve the object's position."""
        return self.bounds[0], self.bounds[1]


def key_down(key):
    """Act based on key that was pressed."""
    global player_move
    if key == pygame.K_LEFT:
        player_move[0] = -1
    if key == pygame.K_RIGHT:
        player_move[0] = +1
    if key == pygame.K_UP:
        player_move[1] = -1
    if key == pygame.K_DOWN:
        player_move[1] = +1
    if key == pygame.K_SPACE:
        print("space down")
    if key == pygame.K_m:
        print("m")


def key_up(key):
    """Act based on key that was released."""
    global player_move
    if key == pygame.K_LEFT:
        player_move[0] = 0
    if key == pygame.K_RIGHT:
        player_move[0] = 0
    if key == pygame.K_UP:
        player_move[1] = 0
    if key == pygame.K_DOWN:
        player_move[1] = 0
    if key == pygame.K_SPACE:
        print("space up")


# ---

FPS = 60
MAX_STARS = 250
STAR_SPEED = 2
BLACK = (0, 0, 0)

size = width, height = (960, 600)

stars = [create_star(randrange(0, width-1)) for star in range(MAX_STARS)]
game_objects = [GameObject('media/images/ufo_spin.gif', 0, 0, 0, True),
                GameObject('media/images/ufo_spin.gif', 0, 0, 0, True),
                GameObject('media/images/ufo_spin.gif', 0, 0, 0, True),
                GameObject('media/images/ufo_spin.gif', 0, 0, 0, True),
                GameObject('media/images/f18.png', width // 2, height//2, 5)]
player_move = [0, 0]
angle = [random() * 360 for _ in game_objects[:-1]]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Star Hunter")

clock = pygame.time.Clock()

while True:
    # Lock the framerate
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            key_up(event.key)
        if event.type == pygame.KEYDOWN:
            key_down(event.key)

    # Move objects
    stars = [[x-speed, y, speed, mag, color]
             if x-speed > 0
             else create_star(width) for x, y, speed, mag, color in stars]

    game_objects[-1].move(*player_move)

    for i, obj in enumerate(game_objects[:-1]):
        x, y = obj.get_position()
        r = (height - 100) // 2
        dx = sin(angle[i] / 180 * pi)
        dy = cos(angle[i] / 180 * pi)
        angle[i] = (angle[i] + 0.5) % 360
        obj.set_position(dx * r + width // 2, dy * r + height // 2)

    # Draw
    screen.fill(BLACK)

    for x, y, speed, magnitude, color in stars:
        rect = (x, y, magnitude, magnitude)
        screen.fill(color, rect)

    for obj in game_objects:
        obj.draw(screen)

    for obj in game_objects:
        obj.draw(screen)

    # always 'flip' at the end
    pygame.display.flip()
