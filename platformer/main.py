import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')


#load imgs
bg_img = pygame.image.load('images/bg1.jpg')



run = True

while run:

    #blit loads things into game
    screen.blit(bg_img, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    pygame.display.update()




pygame.quit()