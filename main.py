import pygame
import random
from src.chicken import Chicken
from src.constants import *
from src.utility import gen_id
from src.foodCollection import FoodCollection
from src.constants import Coord
from src.truck import Truck

# Initialize Game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Hero")
clock = pygame.time.Clock()

sprite_group = pygame.sprite.Group()
foodCollection = FoodCollection()

def add_truck():
    rand_y = random.randrange(0, HEIGHT)
    sprite_group.add(Truck(gen_id(), (0, rand_y)))

def create_chicken_human(position: Coord):
    new_chicken = Chicken(gen_id(), position)
    sprite_group.add(new_chicken)


def draw_window():
    screen.fill((100, 125, 0))
    sprite_group.draw(screen)
    pygame.display.update()


def game_loop():
    counter = 0
    running = True
    create_chicken_human((WIDTH // 2, HEIGHT // 2))
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        if counter % 50 == 0:
            add_truck()
            print("ADD TRUCK")

        counter += 1

        sprite_group.update()
        draw_window()


def main():
    game_loop()
    pygame.quit()


if __name__ == "__main__":
    main()
