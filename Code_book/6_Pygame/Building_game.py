import pygame
import sys
import random

# Define Game parameters
# screen size
screen_width = 900
screen_height = 900

floor_0_type = 0
floor_1_type = 0
floor_2_type = 0
floor_3_type = 0


# initialise the game window
pygame.init()
pygame.display.set_caption('Building game')

# set the game surface
screen = pygame.display.set_mode((screen_width, screen_height))

# a clock to keep track of the game progress
clock = pygame.time.Clock()

# Any commands that draw the initial state of the game
screen.fill(pygame.Color('red'))
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 100, 300, 200))

# Use existing images
backgrImage = pygame.image.load('floor_all/Buildings_900px.png')
backgrImage = pygame.transform.scale(backgrImage, (screen_width, screen_height))
screen.blit(backgrImage, [0, 0])



# Update before the first frame
pygame.display.update()

# Any pos that might need/use
LR_height = 27
LR_width = 24
x_L = 203
x_R = 701
y_0 = 677
y_1 = 716
y_2 = 755
y_3 = 794

def is_rect(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    if (rx <= x <= rx + rw) and (ry <= y <= ry + rh):
        return True
    return False

# The game loop, in here the behaviour of the game is defined.
# This loop is executed every frame.
while True:
    screen.blit(backgrImage, [0, 0])

    # define any drawings

    floorImage_0 = pygame.image.load('floor_all/0_' + str(floor_0_type) + '.png')
    floorImage_0 = pygame.transform.scale(floorImage_0, (screen_width, screen_height))
    screen.blit(floorImage_0, [0, 0])

    floorImage_1 = pygame.image.load('floor_all/1_' + str(floor_1_type) + '.png')
    floorImage_1 = pygame.transform.scale(floorImage_1, (screen_width, screen_height))
    screen.blit(floorImage_1, [0, 0])

    floorImage_2 = pygame.image.load('floor_all/2_' + str(floor_2_type) + '.png')
    floorImage_2 = pygame.transform.scale(floorImage_2, (screen_width, screen_height))
    screen.blit(floorImage_2, [0, 0])

    floorImage_3 = pygame.image.load('floor_all/3_' + str(floor_3_type) + '.png')
    floorImage_3 = pygame.transform.scale(floorImage_3, (screen_width, screen_height))
    screen.blit(floorImage_3, [0, 0])


    # Get key events to check if something is going on through some form of input.
    events = pygame.event.get()
    for event in events:
        # Check exit through x button window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_rect(event.pos, (x_L, y_0, LR_width, LR_height)):
                if floor_3_type > 0:
                    floor_3_type -= 1

            if is_rect(event.pos, (x_L, y_1, LR_width, LR_height)):
                if floor_2_type > 0:
                    floor_2_type -= 1

            if is_rect(event.pos, (x_L, y_2, LR_width, LR_height)):
                if floor_1_type > 0:
                    floor_1_type -= 1

            if is_rect(event.pos, (x_L, y_3, LR_width, LR_height)):
                if floor_0_type > 0:
                    floor_0_type -= 1

            if is_rect(event.pos, (x_R, y_0, LR_width, LR_height)):
                if floor_3_type < 3:
                    floor_3_type += 1

            if is_rect(event.pos, (x_R, y_1, LR_width, LR_height)):
                if floor_2_type < 3:
                    floor_2_type += 1

            if is_rect(event.pos, (x_R, y_2, LR_width, LR_height)):
                if floor_1_type < 3:
                    floor_1_type += 1

            if is_rect(event.pos, (x_R, y_3, LR_width, LR_height)):
                if floor_0_type < 3:
                    floor_0_type += 1



        # Go through all key presses, which you can use to controll the game.
        elif event.type == pygame.KEYDOWN:
            # Check exit through esc
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    # At the end of the loop update the screen and game time.
    pygame.display.update()
    clock.tick()