import pygame
from constants import *
from player import *

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    FPS = pygame.time.Clock()
    Spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    begin_loop = 1
    while True:
         if begin_loop == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill((0,0,0))
            Spaceship.draw(screen)
            dt = FPS.tick(60) / 1000
            pygame.display.flip()
            
            







if __name__ == "__main__":
     main()