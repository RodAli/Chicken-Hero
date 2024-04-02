import pygame
from src.chicken import Chicken
from src.constants import *
from src.utility import gen_id
from src.foodCollection import FoodCollection
from src.types import Coord

# Initialize Game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Hero")
clock = pygame.time.Clock()

sprite_group = pygame.sprite.Group()
foodCollection = FoodCollection()


def create_chicken_human(position: Coord):
    new_chicken = Chicken(gen_id(), position)
    sprite_group.add(new_chicken)


def draw_window():
    screen.fill((100, 125, 0))
    sprite_group.draw(screen)
    pygame.display.update()


def game_loop():
    running = True
    create_chicken_human((WIDTH // 2, HEIGHT // 2))
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        sprite_group.update()
        draw_window()


def main():
    game_loop()
    pygame.quit()


if __name__ == "__main__":
    main()
