import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shots import *

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (bullets, updatable, drawable)
    FPS = pygame.time.Clock()
    Spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    FO = AsteroidField()
    begin_loop = 1
    while True:
         if begin_loop == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill((0,0,0))
            for drawables in drawable:
                drawables.draw(screen)
            dt = FPS.tick(60) / 1000
            updatable.update(dt)
            for asteroid in asteroids:
                for bullet in bullets:
                    if bullet.collision(asteroid):
                        asteroid.split()
                        bullet.kill()
            for asteroid in asteroids:
                if asteroid.collision(Spaceship):
                    print("Game over!")
                    sys.exit()
            pygame.display.flip()
            
            







if __name__ == "__main__":
     main()