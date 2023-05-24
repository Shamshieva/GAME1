import pygame
from sys import exit

pygame.init() #initialize
# screen = pygame.display.set_mode((800, 400)) # to create window
screen = pygame.display.set_mode((800, 400)) # to create window
pygame.display.set_caption('Runner') # set name
clock = pygame.time.Clock()
test_fount = pygame.font.Font(None, 50)

main_surface = pygame.image.load('img/game-bg.jpg') # 800, 500
key_surface = pygame.image.load('img/arrow-keys.png')
text_surface = test_fount.render('Wolf game', False, 'Black')

wolf_L_surface = pygame.image.load('img/wolf/wolf-p-0.png')
wolf_R_surface = pygame.image.load('img/wolf/wolf-p-1.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(main_surface, (0,0)) # x, y
    screen.blit(key_surface, (650,250))
    screen.blit(text_surface, (200,20))

    pygame.display.update()
    clock.tick(60)


