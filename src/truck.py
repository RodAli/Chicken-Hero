import pygame
from src.spriteController import load_truck_sprite

from src.constants import Coord

class Truck(pygame.sprite.Sprite):

    def __init__(self, id: str, pos: Coord):
        pygame.sprite.Sprite.__init__(self)

        self.image = load_truck_sprite()
        self.rect = self.image.get_rect()

        self.rect.center = pos

    def update(self):
        self.rect.x += 5
