import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
sand = (194, 178, 128)
sea_blue = (0, 105, 148)
COLORS = [RED, GREEN, BLUE, BLACK]

# animation variables
clouds_corner = 50

# Math Constants
PI = math.pi
HEIGHT = 500
WIDTH = 700
# Game Constants
SIZE = (WIDTH, HEIGHT)
FPS = 60

########################################################################################################################

'''
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
        pygame.draw.polygon(screen, BLACK, [(self.center-self.width//2, self.height+300),
                                            (self.center+self.width//2, self.height+300),
                                            (self.center-self.width//2-15, self.height+300)])

'''


class Clouds:
    def __init__(self, color):
        self.color = color

    def draw_clouds(self, top_left):
        cloud_x1 = top_left
        cloud_x2 = top_left + 10
        cloud_x3 = top_left - 10
        cloud_x4 = top_left + 25
        for numb in range(3):
            change_cx = numb * 110
            change_cy = numb * 20
            pygame.draw.ellipse(screen, self.color, (cloud_x1 + change_cx, 30 + change_cy, 50, 30))
            pygame.draw.ellipse(screen, self.color, (cloud_x2 + change_cx, 45 + change_cy, 50, 30))
            pygame.draw.ellipse(screen, self.color, (cloud_x3 + change_cx, 35 + change_cy, 50, 30))
            pygame.draw.ellipse(screen, self.color, (cloud_x4 + change_cx, 33 + change_cy, 50, 30))


class Boat:
    def __init__(self, b_x_cord, b_y_cord):
        self.x_cord = b_x_cord
        self.y_cord = b_y_cord

    def draw_sail(self, ):


########################################################################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()
running = True
# game loop
clouds = Clouds(WHITE)
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clouds_corner += 3
    if clouds_corner > WIDTH + 1:
        clouds_corner = WIDTH - WIDTH - 285

    screen.fill(WHITE)
    # Background
    pygame.draw.rect(screen, sand, [0, 400, 700, 100])
    pygame.draw.rect(screen, sea_blue, [0, 0, 700, 400])
    clouds.draw_clouds(clouds_corner)
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
