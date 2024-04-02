import pygame
from src.constants import *

SPRITESHEET_FILE_LOCATION = "./assets/Chicken.png"

SPRITE_WIDTH, SPRITE_HEIGHT = 32, 32


def load_chicken_sprites():
    image = pygame.image.load(SPRITESHEET_FILE_LOCATION)
    up_sprites = []
    right_sprites = []
    down_sprites = []
    left_sprites = []
    for row in range(SPRITE_DIRECTION_SIZE):
        sprites_in_direction = []
        for col in range(3):
            sprite = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT))
            sprite.set_colorkey((0, 0, 0))
            sprite.blit(image, (0, 0), (SPRITE_WIDTH * col, SPRITE_HEIGHT * row, SPRITE_WIDTH, SPRITE_HEIGHT))
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