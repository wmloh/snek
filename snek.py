# importing module (can also type 'import pygame as py' to abbreviate
# pygame as py
import pygame
import time
import random

#initialize pygame module
pygame.init()

display_width = 800
display_height = 600

block_size = 20
AppleThickness = 30
fps = 15
direction = 'right'

# setting the resolution of the program, where parameter must be a tuple
gameDisplay = pygame.display.set_mode((display_width,display_height))
# setting the title of the program (shown on top)
pygame.display.set_caption('Slither')
icon = pygame.image.load('Apple.png')
pygame.display.set_icon(icon)
img = pygame.image.load('Snake Head.png')
appleimg = pygame.image.load('Apple.png')
# refresh the screen (the parameter is empty -> update all)
pygame.display.update()
# introduces the time (frames per second) element into the program
clock = pygame.time.Clock()
smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)

list_of_directions = ['left', 'right', 'up', 'down']

def game_intro():
    intro = True
    while intro:
        gameDisplay.fill((255,255,255))
        message_to_screen('Welcome to Slither!', (0,155,0), -100, 'large')
        message_to_screen('The objective of the game is to eat the red apples.', (0,0,0), -30)
        message_to_screen('The more apples you eat, the longer you get.', (0,0,0), 10)
        message_to_screen('If you run into yourself or the edges, you die.', (0,0,0), 50)
        message_to_screen('Press C to play, P to pause or Q to quit', (0, 0, 0), 180)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False
        clock.tick(5)

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))
    randAppleY = round(random.randrange(0, display_height - AppleThickness))

    return randAppleX, randAppleY

def score(score):
    text = smallfont.render('Score: '+str(score), True, (0,0,0))
    gameDisplay.blit(text,[0,0])

def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill((255,255,255))
        message_to_screen('Game Paused', (0,0,0), -100, 'large')
        message_to_screen('Press C to continue or Q to quit', (0,0,0), 25,)
        pygame.display.update()
        clock.tick(5)

def snake(block_size, snakelist):
    if direction == 'right':
        head = pygame.transform.rotate(img,270)
    if direction == 'left':
        head = pygame.transform.rotate(img,90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img,180)
    gameDisplay.blit(head, (snakelist[-1][0], (snakelist[-1][1])))
    for XnY in snakelist[:-1]:
        gameDisplay.fill((0, 155, 0), rect=[XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color,size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurface = medfont.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace = 0,size = 'small'):
    textSurf, textRect = text_objects(msg, color,size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

# Category: Game Loop
# pygame.event.get() refers to event that occurring due to the user's
# actions in real-time.
# event.type refers to a specific event from an array of possible types
# refer to Pygame manual for more types.
def gameLoop():
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False

    # int variables for the initial position of the head of the snake
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = block_size
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill((255,255,255))
            message_to_screen("GAME OVER", (255,0,0), -50, 'large')
            message_to_screen('Press C to play again or Q to quit.', (255,0,0), 50,'small' )
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = random.choice(list_of_directions)
                    if direction == 'left':
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif direction == 'right':
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif direction == 'up':
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif direction == 'down':
                        lead_y_change = block_size
                        lead_x_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = random.choice(list_of_directions)
                    if direction == 'left':
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif direction == 'right':
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif direction == 'up':
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif direction == 'down':
                        lead_y_change = block_size
                        lead_x_change = 0
                elif event.key == pygame.K_UP:
                    direction = random.choice(list_of_directions)
                    if direction == 'left':
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif direction == 'right':
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif direction == 'up':
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif direction == 'down':
                        lead_y_change = block_size
                        lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = random.choice(list_of_directions)
                    if direction == 'left':
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif direction == 'right':
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif direction == 'up':
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif direction == 'down':
                        lead_y_change = block_size
                        lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True
        # f(object, (R,G,B), [x-coordinate,y-coordinate,x-length,y-length])
        # x and y -coordinates refer to the coordinate of the top left corner
        # alt: pygame.draw.rect(gameDisplay, (0,0,0), [400,300,10,10])
        # the function below can be graphics accelerated so it is preferred
        gameDisplay.fill((255,255,255))
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        score(snakeLength - 1)

        pygame.display.update()
        # defining the number of frames per second; refresh rate
        # higher values indicate faster game speed
        clock.tick(fps)

    pygame.quit()
    quit()

game_intro()
gameLoop()