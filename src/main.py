# Jerry Zhang
# Feb 15
# pygame templete

# imports
import pygame, random, math, sys
from Obstical import obstical

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pygame review")
cloak = pygame.time.Clock()
pygame.init()

saw_blade_group = pygame.sprite.Group()
saw_blade = obstical(400, 300, 0.25)
saw_blade_group.add(saw_blade)

Rungame = True

while Rungame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Rungame = False
            pygame.quit()
            sys.exit()


    # fill or image
    screen.fill((0, 0, 0))

    saw_blade_group.update()
    saw_blade_group.draw(screen)

    pygame.display.update()
    cloak.tick(60)