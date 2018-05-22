import pygame
from pygame.locals import *
pygame.init()

display_width = 500
display_height = 500

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

boy_width = 30
boy_hieght = 30

gDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Just a Game')
clock = pygame.time.Clock()

charSprite = pygame.image.load('sprite_boy.PNG')

def boy(x,y):
    gDisplay.blit(charSprite,(x,y))

def game_loop():

    x = (display_width * 0.5)
    y = (display_height * 0.5)

    x_change = 0
    y_change = 0

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

           

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -2
                elif event.key == pygame.K_RIGHT:
                    x_change = 2
                elif event.key == pygame.K_UP:
                    y_change = -2
                elif event.key == pygame.K_DOWN:
                    y_change = 2
                

            '''if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == K_DOWN:
                    y_change = 0'''


         if event.type.key == pygame.KEYDOWN and (x > display_width - boy_width or x < 2):
            if event.key == pygame.K_LEFT:
                    x_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 0
                    
            if event.type.key == pygame.KEYDOWN and (y > display_height - boy_hieght or y < 2):
                if event.key == pygame.K_UP:
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 0
     

        x += x_change
        y += y_change
                
        gDisplay.fill(white)
        boy(x,y)
        
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
