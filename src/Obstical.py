import pygame, random


class obstical(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed = 1, move_range = (0, 0)):
        super().__init__()

        self.x = x
        self.y = y
        self.scale = scale
        self.move_range = move_range
        
        self.image = pygame.image.load("assets/image/saw_blade.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, self.scale)

        self.rotating_image = self.image
        self.rotate_angle = 0

        self.direction = random.randint(0, 1)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    

        # Create a fixed hitbox
        self.hitbox = self.rect.copy()

        if move_range != (0, 0):

            self.speed = speed
            self.move_range = ((x - (move_range[0]//2), y - (move_range[1]//2)), 
                              (x + (move_range[0]//2), y + (move_range[1]//2)))

            self.xspeed = abs(self.rect.centerx - self.move_range[self.direction][0])/20 * self.speed
            self.yspeed = abs(self.rect.centery - self.move_range[self.direction][1])/20 * self.speed

    def update(self, screen):

        self.rotate_image()
        self.move(screen)

        self.rect = self.image.get_rect(center = self.rect.center)

        self.hitbox.center = self.rect.center

        # Draw the hitbox for debugging
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def rotate_image(self):

        self.rotate_angle += 20
        if self.rotate_angle >= 360:
            self.rotate_angle = 0
        
        self.image = pygame.transform.rotate(self.rotating_image, self.rotate_angle)
        
    def move(self, screen):

        if self.move_range != (0, 0):
        
            pygame.draw.line(screen, (255, 0, 0), self.move_range[0], self.move_range[1], 2)

            if self.direction:
                if self.rect.centerx + self.xspeed >= self.move_range[1][0]:
                    self.direction = 0

                else:
                    self.rect.move_ip(self.xspeed, self.yspeed)

            else:
                if self.rect.centerx - self.xspeed <= self.move_range[0][0]:
                    self.direction = 1

                else:
                    self.rect.move_ip(-self.xspeed, -self.yspeed)

    def collide_hitbox(sprite1, sprite2):
        return sprite1.hitbox.colliderect(sprite2.rect)
    
if __name__ == "__main__":
    test = obstical(1, 1, 1)