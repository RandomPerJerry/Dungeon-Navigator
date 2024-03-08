import pygame
import configs

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sprites = []

        for i in range(2):
            image = pygame.image.load(f"assets/image/player{i}.png").convert_alpha()
            image = pygame.transform.scale(image, configs.PLAYER_SIZE)
            self.sprites.append(image)

        self.sprite_frame = 0

        self.image = self.sprites[self.sprite_frame]
        self.rect = self.image.get_rect()

        self.mask1 = pygame.mask.from_surface(self.sprites[0])
        self.mask2 = pygame.mask.from_surface(self.sprites[1])

        self.mask = self.mask1

        self.rect.topleft = (configs.SCREEN_DIMENTION[0]/2 - 50, 0)

        self.game_reset = True

        self.mask_image = None

        self.gravity = 2

    def update(self, screen):
        self.animate()
        self.move()

        if self.sprite_frame == 0:
            self.mask = self.mask1
            

        else:
            self.mask = self.mask2

        if configs.SHOW_HITBOX:
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
            self.game_reset = True
            self.rect.bottomleft = (self.rect.topleft[0], 0)

            
    def animate(self):

        self.sprite_frame += 0.1
        self.sprite_frame %= 2
        self.image = self.sprites[int(self.sprite_frame)]

    def reset_level(self):

        if self.game_reset:
            self.game_reset = False
            return True
        
        return False





if __name__ == "__main__":
    test = player()
    test.animate()

