import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, other_shape):
        # # print(self.position, other.position)
        # distance = pygame.math.Vector2.distance_to(self.position, other_shape.position)
        # if distance > (self.radius + other_shape.radius):
        #     return True
        # else:
        #     return False

        distance = pygame.Vector2.distance_to(self.position, other_shape.position)
        if distance <= self.radius + other_shape.radius:
            return True
        else:
            return False

        # #not sure how this works
        # if pygame.Vector2.distance_to(self.position,other_shape.position) < PLAYER_RADIUS or pygame.Vector2.distance_to(self.position, other_shape.position) < self.radius:
        #     return True
        # else:
        #     return False


        # distance = self.position.distance_to(other_shape.position) <= self.radius + other_shape.radius
        # if distance:
        #     return True
        # else:
        #     return False