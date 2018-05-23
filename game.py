import pygame, sys
from pygame.locals import *


#We need some basic constants for our display boundaries.
#In python, constants don't really exist, but there is a convention for them.
#When defining a constant (a variable who's value shouldn't change), we define
#   its name in all caps
DISPLAY_BOUNDS = (128, 96)
MAX_FPS = 30
MOVEMENT_SPEED = 1
TILE_BOUNDS = (32, 32)
#The variable type of this is a tuple. A tuple is basically a small array.

#First, we create a class for our little boy.
#A class is a template for an object. The parenthesies are there to show that
#   we want everything from the pygame.Sprite class included in our custom class
#NOTE: It is convention to begin all class names with an uppercase letter
class Boy(pygame.sprite.Sprite):
    #This function is called when we first create an instance of our class
    def __init__(self):
        #We need to tell python to initialize the base Sprite class first, before
        #   we do anything, since we'll be needing the stuff from it
        pygame.sprite.Sprite.__init__(self)
        #The convert_alpha is an optimization that optimizes the way the
        #   image stores its pixels to match the screen
        self.image = pygame.image.load("sprite_boy.png").convert_alpha()
        #We need to give the sprite a bounding rectangle
        self.rect = pygame.Rect((0,0), TILE_BOUNDS)
        print self.rect.width
        print self.rect.height
    #The self in this function is passed for every single function of a class.
    #The self is specifically an instance of Boy, which is the caller of the function
    #for example, if I call boy.try_move(), whatever boy is will be passed into the
    #self argument of this function
    def try_move(self, x, y):
        #This update will take a coordinate
        #This coordinate is not the coordinate to which it moves, but instead, an offset
        #   of where we want to move the object (say, we want to move it right one pixel,
        #   we give a coordinate value of (0,1) where the x is added by 1)

        #To move the rectangle, we simply use the move function of the Rect class
        self.rect.move_ip(x, y)

        #So first, we need to make sure the sprite is not off screen
        if self.clip_rect():
            #If it is off screen, we revert whatever changes we made to the rect
            self.rect.move_ip(-x, -y)

    #This function will check if the rectangle is currently off the screen
    def clip_rect(self):
        #We also need to take into consideration the width of the rectangle itself
        #   (since the rectangle's origin is the top left, so the width is not
        #   accounted for in the x coordinate)
        if self.rect.x + self.rect.width > DISPLAY_BOUNDS[0]:
            return True
        #Same with the height in relation to the y coordinate
        if self.rect.y + self.rect.height > DISPLAY_BOUNDS[1]:
            return True
        if self.rect.x < 0:
            return True
        if self.rect.y < 0:
            return True
        #If none of these cases evaluate to true, we just return false
        return False

    #This function will draw the sprite onto whatever surface we pass it
    def draw(self, surface):
        #blit takes two arguments, a source surface (which is our image) and
        # a Rect (which we made at initialization)
        surface.blit(self.image, self.rect)


#We'll just use this function to exit the game in general
def exit_game():
    #When exiting pygame, it will not close its window, you need to
    #do this yourself.
    pygame.display.quit()
    #and now we actually exit python
    sys.exit()

# We just do this to make sure our program isn't being run as a module
if __name__=="__main__":
    #We initialize the pygame engine
    pygame.init()
    #And we create a display
    pygame.display.init() #Initialize the display
    DISPLAY_SURFACE = pygame.display.set_mode(DISPLAY_BOUNDS) #Make the display
    GAME_CLOCK = pygame.time.Clock()

    #And for optimization, we set pygame to only allow the keydown event, this
    #   way, when we are going through all of our events, we don't need to loop
    #   through every single event pygame has, but just the events we need
    pygame.event.set_blocked(None) #Passing None will set all events to blocked
    pygame.event.set_allowed(pygame.KEYDOWN)
    pygame.event.set_allowed(pygame.QUIT)

    #This sets the keyboard repeat rate. This means if you hold down a key, it'll
    #repeat this many times. The delay is 100ms until the repeating starts, and
    #will repeat every 50ms
    pygame.key.set_repeat(100,1)

    #And now we need to make our little boy, so we can move him around and stuff
    #When calling Boy() the __init__ function is called
    littleBoy = Boy()
    while 1:
        for event in pygame.event.get():
            #And here we loop through all our events.
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    littleBoy.try_move(0,MOVEMENT_SPEED)
                if event.key == pygame.K_UP:
                    littleBoy.try_move(0,-MOVEMENT_SPEED)
                if event.key == pygame.K_RIGHT:
                    littleBoy.try_move(MOVEMENT_SPEED,0)
                if event.key == pygame.K_LEFT:
                    littleBoy.try_move(-MOVEMENT_SPEED,0)
                if event.key == pygame.K_ESCAPE:
                    exit_game()
        #At the end of processing all the events, we must draw the sprite and
        #limit our framerate
        #First we fill the display with black every frame, to prevent ghosting
        #   of the boy sprite
        DISPLAY_SURFACE.fill((0,0,0))
        littleBoy.draw(DISPLAY_SURFACE) #Draw the boy
        #If you want me to explain what this does, just ask me in person or
        #   something, but for now I'll use the technical jargon.
        #This function puts the second buffer of the double buffer onto the main
        #   buffer and flushes the second buffer
        pygame.display.flip()
        #And now we limit our framerate
        GAME_CLOCK.tick(MAX_FPS)

else:
    print "This game should not be run as a module"
