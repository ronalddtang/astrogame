#imports
from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        #original asteroid will dissapear upon touching a bullet
        self.kill()        
        #random angle
        random_angle = random.uniform(20, 50)
        
        #changing the radius size
        random_radius = self.radius - ASTEROID_MIN_RADIUS
        
        #defining the speed to the asteroid
        speed = random.randint(40, 100)

        #check if asteroid radius is too small
        if self.radius >= ASTEROID_MIN_RADIUS:
            #direction
            direction = pygame.Vector2(0,1).rotate(random_angle)
            
            #generates 1 an ansteroid that is smaller
            asteroid_1 = Asteroid(self.position.x, self.position.y, random_radius)
            asteroid_1.velocity = direction * speed
            
            #generates 2nd asteroid
            asteroid_2 = Asteroid(self.position.x, self.position.y, random_radius)
            asteroid_2.velocity = -direction * speed