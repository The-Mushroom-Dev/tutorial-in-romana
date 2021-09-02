import pygame, sys # import pygame and sys
framerate = pygame.time.Clock() # set up the clock
from pygame.locals import *
pygame.init() 
pygame.display.set_caption('Mushroom') 

screen = pygame.display.set_mode((900,500)) 

playerIMG = pygame.image.load('player.png') 
playerLOC = [50,50]

moving_right = False
moving_left = False



while True: 
    screen.fill((146,244,255)) 
    screen.blit(playerIMG,playerLOC) 


    
	# movement
    if moving_right == True:
        playerLOC[0] += 4
    if moving_left == True:
        playerLOC[0] -= 4


    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update() 
    framerate.tick(60) 