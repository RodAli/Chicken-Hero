import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, id, pos):
        pygame.sprite.Sprite.__init__(self)

        self.id = id
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

    def get_location(self):
        return self.rect.center
