import pygame
from sys import exit

pygame.init() #initialize
# screen = pygame.display.set_mode((800, 400)) # to create window
screen = pygame.display.set_mode((800, 400)) # to create window
pygame.display.set_caption('Runner') # set name
clock = pygame.time.Clock()
test_fount = pygame.font.Font(None, 50)

test_surface = pygame.image.load('img/game-bg.jpg') # 800, 500
ground_surface = pygame.image.load('img/arrow-keys.png')
text_surface = test_fount.render('Wolf game', False, 'Black')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0,0)) # x, y
    screen.blit(ground_surface, (650,250))
    screen.blit(text_surface, (200,20))

    pygame.display.update()
    clock.tick(60)


