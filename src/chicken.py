import pygame

from src.constants import *
from src.spriteController import load_chicken_sprites
from src.utility import generate_rand_point_in_rect
from src.projTypes import Coord


class Chicken(pygame.sprite.Sprite):
    def __init__(self, id: str, pos: Coord):
        pygame.sprite.Sprite.__init__(self)
        
        # Sprites
        sprites = load_chicken_sprites()
        self.sprites_up = sprites[0]
        self.sprites_right = sprites[1]
        self.sprites_down = sprites[2]
        self.sprites_left = sprites[3]

        # Pygame
        self.image = self.sprites_up[0]
        self.image_last_updated = 0
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

        # Other
        self.id = id
        self.current_frame = 0
        self.direction = DIRECTION_RIGHT
        self.prev_direction = None
        self.moving = False
        self.speed = 5
        self.target = generate_rand_point_in_rect(WIDTH, HEIGHT)

    def update(self):
        # Generate move
        direction = self.get_player_movement_input()
        
        # Move the chicken
        self.move(direction)

        # Generate new target if we have reached our target
        self.check_and_adjust_target()

        # Animate the chicken
        self.animate()

    def get_location(self):
        return self.rect.center

    def check_and_adjust_target(self):
        if self.rect.collidepoint(self.target[0], self.target[1]):
            self.target = generate_rand_point_in_rect(WIDTH, HEIGHT)

    def move(self, direction: int):
        # If not moving, set and return
        if direction is None:
            self.moving = False
            return

        # If moving, set values
        self.prev_direction = self.direction
        self.direction = direction
        self.moving = True
        
        # Calculate position
        if self.direction == DIRECTION_RIGHT:
            self.rect.x += self.speed
        elif self.direction == DIRECTION_LEFT:
            self.rect.x -= self.speed
        elif self.direction == DIRECTION_UP:
            self.rect.y -= self.speed
        elif self.direction == DIRECTION_DOWN:
            self.rect.y += self.speed
        elif self.direction == DIRECTION_UP_RIGHT:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.direction == DIRECTION_UP_LEFT:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.direction == DIRECTION_DOWN_RIGHT:
            self.rect.x += self.speed
            self.rect.y += self.speed
        elif self.direction == DIRECTION_DOWN_LEFT:
            self.rect.x -= self.speed
            self.rect.y += self.speed

    @staticmethod
    def get_player_movement_input() -> int:
        # Read key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            return DIRECTION_UP_RIGHT
        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            return DIRECTION_UP_LEFT
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            return DIRECTION_DOWN_RIGHT
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            return DIRECTION_DOWN_LEFT
        elif keys[pygame.K_LEFT]:
            return DIRECTION_LEFT
        elif keys[pygame.K_RIGHT]:
            return DIRECTION_RIGHT
        elif keys[pygame.K_UP]:
            return DIRECTION_UP
        elif keys[pygame.K_DOWN]:
            return DIRECTION_DOWN

    def animate(self):
        now = pygame.time.get_ticks()
        if (now - self.image_last_updated > 200) or (self.direction != self.prev_direction):
            self.image_last_updated = now
            self.current_frame = (self.current_frame + 1) % SPRITE_DIRECTION_SIZE
            sprite_array_to_use = []
            if self.direction == DIRECTION_RIGHT:
                sprite_array_to_use = self.sprites_right
            elif self.direction == DIRECTION_LEFT:
                sprite_array_to_use = self.sprites_left
            elif self.direction == DIRECTION_UP:
                sprite_array_to_use = self.sprites_up
            elif self.direction == DIRECTION_DOWN:
                sprite_array_to_use = self.sprites_down
            elif self.direction == DIRECTION_UP_RIGHT:
                sprite_array_to_use = self.sprites_right
            elif self.direction == DIRECTION_DOWN_RIGHT:
                sprite_array_to_use = self.sprites_right
            elif self.direction == DIRECTION_UP_LEFT:
                sprite_array_to_use = self.sprites_left
            elif self.direction == DIRECTION_DOWN_LEFT:
                sprite_array_to_use = self.sprites_left

            if not self.moving:
                self.image = sprite_array_to_use[0]
            else:
                self.image = sprite_array_to_use[self.current_frame]
