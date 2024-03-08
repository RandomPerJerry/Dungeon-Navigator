# Jerry Zhang
# Feb 27
# Dungeon Navigator 

# imports
import pygame, random, sys
from obstical import obstical
from player import player
from coin import coin
import instance_perm
import configs

screen = pygame.display.set_mode(configs.SCREEN_DIMENTION)
pygame.display.set_caption("pygame review")
cloak = pygame.time.Clock()
pygame.init()

character = pygame.sprite.GroupSingle()
bobby = player()
character.add(bobby)

coin_group = pygame.sprite.Group()
saw_blade_group = pygame.sprite.Group()

background = pygame.image.load("assets/image/Background.jfif")
background = pygame.transform.scale(background, configs.SCREEN_DIMENTION)
Rungame = True

while Rungame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Rungame = False
            pygame.quit()
            sys.exit()

    # fill or image
    screen.blit(background, (0, 0))


    character.update(screen)
    character.draw(screen)

    if pygame.sprite.spritecollide(character.sprite, saw_blade_group, False, pygame.sprite.collide_mask):
        print('collide')

    if bobby.reset_level():
        saw_blade_group.empty()
        coin_group.empty()

        static_num = 4
        moving_num = 2

        static_saw, moving_saw = instance_perm.generate_unique_positions(static_num, moving_num)
        for position in static_saw:
            saw_blade_group.add(obstical(position[0], position[1], 0.09))

        for position in moving_saw:
            saw_blade_group.add(obstical(position[0][0], position[0][1], 0.09, move_range=(position[1][0], position[1][1])))

        coin_group.add(coin(100, 100))


    saw_blade_group.update(screen)
    saw_blade_group.draw(screen)

    pygame.display.update()
    cloak.tick(configs.FPS)