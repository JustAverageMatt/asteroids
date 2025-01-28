import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    Shot.containers = (shots, updatable_group, drawable_group)

    asteroid_field = AsteroidField()

    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable_group:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
