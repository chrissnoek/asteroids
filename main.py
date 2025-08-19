# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    dt = 0
    time = pygame.time.Clock()
    
    # Create two groups:
    # - updatable: all objects that can be updated
    # - drawable: all objects that can be drawn on the screen
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set both groups as containers for the Player class.
    # This ensures any Player created will automatically be added to these groups.
    Player.containers = (updatable, drawable)
    
    # Create a Player instance at the center of the screen.
    # The instance will be automatically added to both groups.
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Asteroid.containers =  (astroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    astroidField = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        deltaTime = time.tick(60)
        dt = deltaTime / 1000
        updatable.update(dt)
        for astroid in astroids:
            for shot in shots:
                if shot.collision(astroid):
                    shot.kill()
                    astroid.split()
            if astroid.collision(player):
                print("Game over!")
                sys.exit("Game over!")

if __name__ == "__main__":
    main()