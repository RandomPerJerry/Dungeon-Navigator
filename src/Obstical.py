import pygame

class obstical(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, move = (0, 0)):
        super().__init__()

        self.x = x
        self.y = y
        self.scale = scale
        self.move = move

        self.image = pygame.image.load("assets/image/saw_blade.png")
        self.image = pygame.transform.rotozoom(self.image, 0, self.scale)

        self.rotating_image = self.image

        self.rotate_angle = 0

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def update(self):
        
        self.rotate_angle += 8
        if self.rotate_angle >= 360:
            self.rotate_angle = 0
        
        self.image = pygame.transform.rotate(self.rotating_image, self.rotate_angle)
        self.rect = self.image.get_rect(center = self.rect.center)

