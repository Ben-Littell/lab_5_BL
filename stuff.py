import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, BLACK]

# Math Constants
PI = math.pi
HEIGHT = 500
WIDTH = 700
# Game Constants
SIZE = (WIDTH, HEIGHT)
FPS = 60

########################################################################################################################


class Rocket:
    def __init__(self, height, width, center, color1, color2):
        self.height = height
        self.width = width
        self.color1 = color1
        self.color2 = color2
        self.center = center

    def draw_rocket(self):
        # cone
        pygame.draw.polygon(screen, BLACK, [(self.center-self.width//2, self.height+50),
                                            (self.center+self.width//2, self.height+50),
                                            (self.center, self.height)])
        # body
        pygame.draw.rect(screen, BLACK, (self.center-self.width//2, self.height+50, self.width, self.height-25))
        # thruster
        pygame.draw.polygon(screen, BLACK, [(self.center-self.width//2, self.height+150),
                                            (self.center+self.width//2, self.height+150),
                                            (self.center-self.width//2-15, self.height+150)])









########################################################################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()
rocket1 = Rocket(200, 100, 350, BLACK, RED)
running = True
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    rocket1.draw_rocket()
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()





