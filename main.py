import pygame
from sys import exit
import random

# Initialize the game
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Wolf')
clock = pygame.time.Clock()
test_fount = pygame.font.Font(None, 50)


# Background
main_surface = pygame.image.load('img/game-bg.jpg').convert()

# Wolf
wolf1_img = pygame.image.load('img/wolf/wolf-p-0.png').convert_alpha()
wolf2_img = pygame.image.load('img/wolf/wolf-p-1.png').convert_alpha()
wolf1_rect = wolf1_img.get_rect(topleft=(178, 167))
wolf2_rect = wolf2_img.get_rect(topleft=(298, 167))


# Button
button_img = pygame.image.load('img/arrow-keys.png').convert() #  (650,250)

# Text
score_surf = test_fount.render('Wolf game', False, 'Black').convert()
score_rect = score_surf.get_rect(center=(400,50))

# Logo image
logo_img = pygame.image.load('img/logo.png').convert()

# Font
font = pygame.font.Font(None, 36)

# Button
nav_button = pygame.image.load('img/nav-button.png').convert_alpha()
restart_icon = pygame.image.load('img/restart-icon.png')

# Basket
basket1u = pygame.image.load('img/basket/basket-p-0-0.png').convert_alpha()
basket1d = pygame.image.load('img/basket/basket-p-0-1.png')
basket2u = pygame.image.load('img/basket/basket-p-1-0.png')
basket2d = pygame.image.load('img/basket/basket-p-1-1.png')

# Eggs
egg_img = pygame.image.load('img/egg/egg.png').convert_alpha()
egg_x_position = 50
egg_y_position = 120

# Egg properties
egg_x = random.randint(0, 800 - egg_img.get_width())
egg_y = -egg_img.get_height()
egg_speed = 3

egg_rect = egg_img.get_rect(topleft = (100, 100))

player_gravity = 0

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    # Background
    screen.blit(main_surface, (0,0))

    # Wolf left
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        screen.blit(wolf1_img, wolf1_rect)
        screen.blit(basket1d, (125, 155))
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        screen.blit(wolf1_img, wolf1_rect)
        screen.blit(basket1u, (125, 235))
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        screen.blit(wolf2_img, wolf2_rect)
        screen.blit(basket2u, (362, 240))
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        screen.blit(wolf2_img, wolf2_rect)
        screen.blit(basket2d, (367, 162))


    egg_x_position+=1
    egg_y_position+=1

    if egg_x_position == 140 and egg_y_position == 210:
        egg_x_position = 50
        egg_y_position = 120

    screen.blit(egg_img, (egg_x_position, egg_y_position))



    # Player
    # player_gravity += 1
    # player_L_rect.y += player_gravity
    # if player_L_rect.bottom >= 178:
    #     player_L_rect.bottom = 178

    # mouse_pos = pygame.mouse.get_pos()
    # if player_L_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())
    #     print('hi')
    #
    # keys = pygame.key.get_pressed()
    # keys[pygame.K_SPACE]


    pygame.display.update()
    clock.tick(50)


