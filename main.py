import pygame
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



#initialising groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

#init containers for the groups
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (bullets, updatable, drawable)

def main():
    #initalising pygame
    pygame.init()

    #setting game variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #creating players
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #creating asteroids
    rock = AsteroidField()

    #shots initialising

    #infinite loop
    while True:
        #makes code stop when window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #makes the screen fill with a black bg
        screen.fill((0,0,0))
        
        updatable.update(dt)
        for items in drawable:
            items.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collide(p1):
                print("Game Over!")
                exit()
            else:
                pass
            
        for bullet in bullets:
        # drawable.draw(screen)
            pass
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()