# importing module (can also type 'import pygame as py' to abbreviate
# pygame as py
import pygame
import time
import random
import datetime

#initialize pygame module
pygame.init()

display_width = 1366
display_height = 768

block_size = 20
AppleThickness = 60
fps = 9
direction = 'right'
points = 0

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Slither')
icon = pygame.image.load('Apple.png')
pygame.display.set_icon(icon)
img = pygame.image.load('Snake Head.png')
appleimg = pygame.image.load('Apple.png')
pygame.display.update()
clock = pygame.time.Clock()
smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)


direction_list_l = ['left', 'up', 'down']
direction_list_r = ['right', 'up', 'down']
direction_list_u = ['left', 'right', 'up']
direction_list_d = ['left', 'right', 'down']
images = []
b_colour = (255,255,255)

def random_images():
    return random.choice(images)

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

def display_points():
    message_to_screen(str(round(points,1)), (0,0,0), -250, size='small')

def gameLoop():
    global direction
    global points
    global b_colour
    global fps

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = block_size
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    points = 0
    randAppleX, randAppleY = randAppleGen()
    discolight = False
    darkness = False

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
                    direction = random.choice(direction_list_l)
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
                    direction = random.choice(direction_list_r)
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
                    direction = random.choice(direction_list_u)
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
                    direction = random.choice(direction_list_d)
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
                if event.key == pygame.K_x:
                    if discolight == False:
                        discolight = True
                        darkness = False
                        fps = 16
                    else:
                        discolight = False
                        b_colour = (255,255,255)
                        fps = 9
                if event.key == pygame.K_z:
                    if darkness == False:
                        darkness = True
                        discolight = False
                        fps = 9
                    else:
                        darkness = False
                        b_colour = (255,255,255)

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True
        gameDisplay.fill(b_colour)
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
                points += 15

        if discolight:
            points += 3/fps
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            b_colour = (a, b, c)
        if darkness:
            b_colour = (0, 155, 0)

        #score(snakeLength - 1)
        points += 1/fps
        display_points()
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

game_intro()
gameLoop()