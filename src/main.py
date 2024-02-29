# Jerry Zhang
# Feb 27
# Dungeon Navigator 

# imports
import pygame, random, math, sys
from Obstical import obstical
from Player import player

SCREEN_DIMENTION = (800, 600)

screen = pygame.display.set_mode(SCREEN_DIMENTION)
pygame.display.set_caption("pygame review")
cloak = pygame.time.Clock()
pygame.init()

character = pygame.sprite.GroupSingle()
bobby = player()
character.add(bobby)

saw_blade_group = pygame.sprite.Group()
saw_blade = obstical(400, 300, 0.1, move_range=(100, 100))
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

    character.update(screen)
    character.draw(screen)

    saw_blade_group.update(screen)
    saw_blade_group.draw(screen)

    pygame.display.update()
    cloak.tick(60)