import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([25, 25])
        self.image.fill((255, 0 , 0))
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

    def update(self):
        self.rect.x += 1