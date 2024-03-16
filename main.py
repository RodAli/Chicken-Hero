import pygame
from src.chicken import Chicken
from src.constants import *
from src.food import Food
from src.utility import gen_id
from src.foodCollection import FoodCollection

# Initialize Game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Hero")
clock = pygame.time.Clock()

sprite_group = pygame.sprite.Group()
foodCollection = FoodCollection()


def create_chicken_ai(position):
    new_chicken = Chicken(gen_id(), position, chicken_type = CHICKEN_TYPE_AI)
    sprite_group.add(new_chicken)


def create_chicken_human(position):
    new_chicken = Chicken(gen_id(), position, foodCollection, chicken_type = CHICKEN_TYPE_HUMAN)
    sprite_group.add(new_chicken)


def create_food(position):
    new_food = Food(gen_id(), position)
    sprite_group.add(new_food)
    foodCollection.add_food(new_food)


def draw_window():
    screen.fill((100, 125, 0))
    sprite_group.draw(screen)
    pygame.display.update()


def game_loop():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if event.button == 1: # left click
                    print("Chicken created")
                    create_chicken_human(pos)
                elif event.button == 3: # right click 
                    print("Food created")
                    # create_chicken_human(pos)
                    create_food(pos)

        sprite_group.update()
        draw_window()


def main():
    game_loop()
    pygame.quit()


if __name__ == "__main__":
    main()
