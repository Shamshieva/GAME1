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
main_img = pygame.image.load('img/game-bg.jpg').convert()
# Wolf
wolf1_img = pygame.image.load('img/wolf/wolf-p-0.png').convert_alpha()
wolf2_img = pygame.image.load('img/wolf/wolf-p-1.png').convert_alpha()
wolf1_rect = wolf1_img.get_rect(topleft=(178, 167))
wolf2_rect = wolf2_img.get_rect(topleft=(298, 167))
wolf1_x = 125
wolf1_y = 155
score = 0
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

# Egg properties
egg_img = pygame.image.load('img/egg/egg.png').convert_alpha()
egg_positions = [[50,120], [50,200], [500,120], [500,200]]
egg_speed = 3
random_egg = random.choice(egg_positions)
egg_x_position = random_egg[0]
egg_y_position = random_egg[1]

egg_rect = egg_img.get_rect(topleft = (100, 100))

player_gravity = 0

game_over = False


def check_collision():
    global score, egg_x_position, egg_y_position, random_egg

    if egg_x_position == 130 and egg_y_position == 200:
        score += 1
    elif egg_x_position == 130 and egg_y_position == 280:
        score += 1
    elif egg_x_position == 420 and egg_y_position == 200:
        score += 1
    elif egg_x_position == 420 and egg_y_position == 280:
        score += 1

    random_egg = random.choice(egg_positions)
    egg_x_position = random_egg[0]
    egg_y_position = random_egg[1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Background
    screen.blit(main_img, (0,0))
    if random_egg[0] == 50:
        egg_x_position += 1
        egg_y_position += 1
    if random_egg[0] == 500:
        egg_x_position -= 1
        egg_y_position += 1

    if egg_x_position == 130 and egg_y_position == 200:
        egg_x_position = random_egg[0]
        egg_y_position = random_egg[1]
        check_collision()
    if egg_x_position == 130 and egg_y_position == 280:
        egg_x_position = random_egg[0]
        egg_y_position = random_egg[1]
        check_collision()
    if egg_x_position == 420 and egg_y_position == 200:
        egg_x_position = random_egg[0]
        egg_y_position = random_egg[1]
        check_collision()
    if egg_x_position == 420 and egg_y_position == 280:
        egg_x_position = random_egg[0]
        egg_y_position = random_egg[1]
        check_collision()

    screen.blit(egg_img, (egg_x_position,egg_y_position))

    if egg_x_position==wolf1_x:
        score += 1
    # Wolf keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(wolf1_img, wolf1_rect)
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        screen.blit(wolf1_img, wolf1_rect)
        screen.blit(basket1d, (125, 155))
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        screen.blit(wolf1_img, wolf1_rect)
        screen.blit(basket1u, (125, 235))
    if keys[pygame.K_RIGHT]:
        screen.blit(wolf2_img, wolf2_rect)
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        screen.blit(wolf2_img, wolf2_rect)
        screen.blit(basket2d, (367, 162))
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        screen.blit(wolf2_img, wolf2_rect)
        screen.blit(basket2u, (362, 240))

    # Display the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(50)


