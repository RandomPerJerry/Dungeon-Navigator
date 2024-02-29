import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sprites = []

        for i in range(2):
            image = pygame.image.load(f"assets/image/player{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (100, 100))
            self.sprites.append(image)

        self.sprite_frame = 0

        self.image = self.sprites[self.sprite_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (350, 0)

        self.gravity = 2

    def update(self, screen):
        self.animate()
        self.move()
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.topleft[0] - 10 >= 0:
            self.rect.move_ip(-5, self.gravity)
        elif keys[pygame.K_d] and self.rect.topright[0] + 10 <= 800:
            self.rect.move_ip(5, self.gravity)
        else:
            self.rect.move_ip(0, self.gravity)

        if self.rect.topleft[1] > 600:
            self.rect.topleft = (self.rect.topleft[0], 0)

    def animate(self):

        self.sprite_frame += 0.1
        self.sprite_frame %= 2
        self.image = self.sprites[int(self.sprite_frame)]

    

        



if __name__ == "__main__":
    test = player()
    test.animate()

