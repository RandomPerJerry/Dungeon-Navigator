import pygame
import configs

class coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.image = pygame.image.load("assets/image/coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.mask = pygame.mask.from_surface(self.image)

    

    
