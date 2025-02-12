#imports
from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2(0, 1)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt