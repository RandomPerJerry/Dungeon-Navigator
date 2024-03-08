import pygame, random
import configs


class obstical(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed = 1, move_range = (0, 0)):
        super().__init__()

        self.x = x
        self.y = y
        self.scale = scale
        self.move_location = move_range
        
        self.image = pygame.image.load("assets/image/saw_blade.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, self.scale)

        self.rotating_image = self.image
        self.rotate_angle = 0

        self.direction = random.randint(0, 1)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)
    

        # Create a fixed hitbox
        self.hitbox = self.rect

        if move_range != (0, 0):

            self.speed = speed
            self.move_location = ((x - (move_range[0]//2), y - (move_range[1]//2)), 
                              (x + (move_range[0]//2), y + (move_range[1]//2)))

            self.xspeed = abs(self.move_location[1][0] - self.move_location[0][0])/60 * self.speed
            self.yspeed = abs(self.move_location[1][1] - self.move_location[0][1])/60 * self.speed
        
    def update(self, screen):

        self.rotate_image()
        self.move(screen)

        self.rect = self.image.get_rect(center = self.rect.center)

        self.hitbox.center = self.rect.center

        # Draw the hitbox for debugging
        if configs.SHOW_HITBOX:
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


    def rotate_image(self):

        self.rotate_angle += 20
        if self.rotate_angle >= 360:
            self.rotate_angle = 0
        
        self.image = pygame.transform.rotate(self.rotating_image, self.rotate_angle)
        self.mask = pygame.mask.from_surface(self.image)
        
    def move(self, screen):

        if self.move_location != (0, 0):
        
            if configs.SHOW_HITBOX:
                pygame.draw.line(screen, (0, 0, 0), self.move_location[0], self.move_location[1], 10)

            if self.direction:
                if self.rect.centerx + self.xspeed > self.move_location[1][0]:
                    self.direction = 0

                else:
                    self.rect.move_ip(self.xspeed, self.yspeed)

            else:
                if self.rect.centerx - self.xspeed < self.move_location[0][0]:
                    self.direction = 1

                else:
                    self.rect.move_ip(-self.xspeed, -self.yspeed)


        