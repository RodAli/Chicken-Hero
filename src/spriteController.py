import pygame
from src.constants import *

CHICKEN_SPRITESHEET_FILE_LOCATION = "./assets/Chicken.png"
RED_TRUCK_SPRITESHEET_FILE_LOCATION = "./assets/RedTruck.png"
GREEN_TRUCK_SPRITESHEET_FILE_LOCATION = "./assets/GreenTruck.png"

CHICKEN_SPRITE_WIDTH, CHICKEN_SPRITE_HEIGHT = 32, 32
TRUCK_SPRITE_WIDTH, TRUCK_SPRITE_HEIGHT = 20, 15


def load_chicken_sprites():
    image = pygame.image.load(CHICKEN_SPRITESHEET_FILE_LOCATION)
    up_sprites = []
    right_sprites = []
    down_sprites = []
    left_sprites = []
    for row in range(SPRITE_DIRECTION_SIZE):
        sprites_in_direction = []
        for col in range(3):
            sprite = pygame.Surface((CHICKEN_SPRITE_WIDTH, CHICKEN_SPRITE_HEIGHT))
            sprite.set_colorkey((0, 0, 0))
            sprite.blit(image, (0, 0), (CHICKEN_SPRITE_WIDTH * col, CHICKEN_SPRITE_HEIGHT * row, CHICKEN_SPRITE_WIDTH, CHICKEN_SPRITE_HEIGHT))
            sprites_in_direction.append(sprite)
        ordered_sprites = [sprites_in_direction[1], sprites_in_direction[0], sprites_in_direction[1],
                            sprites_in_direction[2]]
        if row == 0:
            up_sprites.extend(ordered_sprites)
        elif row == 1:
            right_sprites.extend(ordered_sprites)
        elif row == 2:
            down_sprites.extend(ordered_sprites)
        elif row == 3:
            left_sprites.extend(ordered_sprites)

    return up_sprites, right_sprites, down_sprites, left_sprites

def load_truck_sprite():
    image = pygame.image.load(RED_TRUCK_SPRITESHEET_FILE_LOCATION)
    sprite = pygame.Surface((TRUCK_SPRITE_WIDTH, TRUCK_SPRITE_HEIGHT))
    sprite.set_colorkey((0, 0, 0))
    sprite.blit(image, (0, 0), )

    multiplier = 2
    sprite = pygame.transform.scale(sprite, (TRUCK_SPRITE_WIDTH * multiplier, TRUCK_SPRITE_HEIGHT * multiplier))

    return sprite