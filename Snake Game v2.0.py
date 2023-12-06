"""
Program:    Snake Game
Author:     Sky Good
Date:       1/5/2022
"""

import random
import pygame
import time
SNAKE = [(370,21)]

def snakeHead(x,y):
    """
    Purpose:    Blits the snake head to the window
    Parameters: x, y
    Returns:    None
    """
    screen.blit(snakeHeadImg, (x,y))
 
def snakeBody_NS(snake, previousXChange, previousYChange, going):
    """
    Purpose:    Blits the a snake cell to the window north or south
    Parameters: x, y
    Returns:    None
    """
    #for i in range(1, len(snake)):
    if going == "up":
        screen.blit(snakeBodyNS, (snake[0][0] + previousXChange, snake[0][1] + previousYChange + 34))
    elif going == "down":
        screen.blit(snakeBodyNS, (snake[0][0] + previousXChange, snake[0][1] + previousYChange - 34))

def snakeBody_EW(snake, previousXChange, previousYChange, going):
    """
    Purpose:    Blits the a snake cell to the window east or west
    Parameters: x, y
    Returns:    None
    """
    #for i in range(1, len(snake)):
    if going == "left":
        screen.blit(snakeBodyEW, (snake[0][0] + previousXChange + 34, snake[0][1] + previousYChange))
    elif going == "right":
        screen.blit(snakeBodyEW, (snake[0][0] + previousXChange - 34, snake[0][1] + previousYChange))

def createNewFood():
    """
    Purpose:    Creates random food coordinates
    Parameters: x, y
    Returns:    food
    """
    x = (random.randint(0,10) * 34) + 336
    y = (random.randint(0,10) * 34) + 21

    if x == 676:
        x = 642
    if y == 361:
        y = 327
    
    food = (x,y)

    return food

def checkerBorderCross():
    """
    Purpose:    Checks if the snake position has crossed the border
    Parameters: snake
    Returns:    T/F
    """
    if SNAKE[0][0] < 336:
        return True
    elif SNAKE[0][0] >= 642:
        return True
    if SNAKE[0][1] < 21:
        return True
    elif SNAKE[0][1] >= 327:
        return True

def checkCurrentFood(Food):
    """
    Purpose:    Checks snakes collision with food
    Parameters: snake, Food
    Returns:    T/F
    """
    if Food[0] <= SNAKE[0][0] <= (Food[0] + 34) and Food[1] <= SNAKE[0][1] <= (Food[1] + 34):
        return True
    elif Food[0] <= (SNAKE[0][0] + 34) <= (Food[0] + 34) and Food[1] <= (SNAKE[0][1] + 34) <= (Food[1] + 34):
        return True
    elif Food[0] <= SNAKE[0][0] <= (Food[0] + 34) and Food[1] <= (SNAKE[0][1] + 34) <= (Food[1] + 34):
        return True
    elif Food[0] <= (SNAKE[0][0] + 34) <= (Food[0] + 34) and Food[1] <= SNAKE[0][1] <= (Food[1] + 34):
        return True
    else:
        return False

def showScore():
    """
    Purpose:    Renders the score to the window
    Parameters: x, y
    Returns:    None
    """
    score = font.render(str(score_value), True, (0,0,0))
    screen.blit(score, (160,82))

def smoothMovement(x,y):
    """
    Purpose:    Rounds up or down the snakes positions to snap to the 10x10 grid
    Parameters: snake
    Returns:    (x,y)
    """
    remainderX = (x - 336) % 34
    if 0 <= remainderX < 17:
        xx = x - remainderX
    elif 17 < remainderX <= 34:
        xx = x - remainderX

    remainderY = (y - 21) % 34
    if 0 <= remainderY < 17:
        yy = y - remainderY
    elif 17 < remainderY <= 34:
        yy = y - remainderY
    
    if remainderX == 17:
        xx = x
    if remainderY == 17:
        yy = y

    return (xx,yy)

def generateTailCords(going):
    """
    Purpose:    Creates the coordinates for the next tail piece
    Parameters: snake, going
    Returns:    snake
    """
    if going == "up":
        x = SNAKE[-1][0]
        y = SNAKE[-1][1] - 34
    elif going == "right":
        x = SNAKE[-1][0] - 34
        y = SNAKE[-1][1]
    elif going == "down":
        x = SNAKE[-1][0]
        y = SNAKE[-1][1] + 34
    elif going == "left":
        x = SNAKE[-1][0] + 34
        y = SNAKE[-1][1]
    SNAKE.append((x,y))

def checkKeyDown():
    """
    Purpose:    Checks if a key is pressed and returns the direction
    Parameters: None
    Returns:    direction
    """
    global snakeHeadXChange
    global snakeHeadYChange
    global going

    #Keystroke Down
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snakeHeadXChange = -1
            snakeHeadYChange = 0
            going = "left"
            
        if event.key == pygame.K_RIGHT:
            snakeHeadXChange = 1
            snakeHeadYChange = 0
            going = "right"               

        if event.key == pygame.K_UP:
            snakeHeadYChange = 1
            snakeHeadXChange = 0
            going = "up"                

        if event.key == pygame.K_DOWN:
            snakeHeadYChange = -1
            snakeHeadXChange = 0
            going = "down"
    return going

def blitSnake(going):
    """
    Purpose:    Blits the snake head to the window
    Parameters: going
    Returns:    None
    """
    if going == 'right':
        screen.blit(snakeHeadRight, (snakeHeadX,snakeHeadY))
    elif going == 'down':
        screen.blit(snakeHeadDown, (snakeHeadX,snakeHeadY))
    elif going == 'left':
        screen.blit(snakeHeadLeft, (snakeHeadX,snakeHeadY))
    elif going == 'up':
        screen.blit(snakeHeadUp, (snakeHeadX,snakeHeadY))

    for cell in SNAKE:
        if going == "up" or going == "down":
            snakeBody_NS(SNAKE, snakeHeadXChange, snakeHeadYChange, going)
        elif going == "left" or going == "right":
            snakeBody_EW(SNAKE, snakeHeadXChange, snakeHeadYChange, going)
        

def blitSnakeHeadHurt(going):
    """
    Purpose:    Blits the snake head to the window
    Parameters: going
    Returns:    None
    """
    if going == 'right':
        screen.blit(snakeHurtRight, (snakeHeadX,snakeHeadY))
    elif going == 'down':
        screen.blit(snakeHurtDown, (snakeHeadX,snakeHeadY))
    elif going == 'left':
        screen.blit(snakeHurtLeft, (snakeHeadX,snakeHeadY))
    elif going == 'up':
        screen.blit(snakeHurtUp, (snakeHeadX,snakeHeadY))

def blitFood(food):
    """
    Purpose:    Blits food to the window
    Parameters: food
    Returns:    None
    """
    screen.blit(foodImg, (food[0], food[1]))

def blitBackground():
    """
    Purpose:    Blits the backround to the window
    Parameters: None
    Returns:    None
    """
    screen.blit(pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/Background_images/Background2.png'), (0,0))

def loadImages():
    """
    Purpose:    Loads all images
    Parameters: None
    Returns:    None
    """
    global snakeHeadImg
    global snakeBodyImg
    global snakeHeadHurt
    global foodImg
    global game_over
    global snakeHeadRight
    global snakeHeadLeft
    global snakeHeadDown
    global snakeHeadUp
    global snakeHurtRight
    global snakeHurtLeft
    global snakeHurtDown
    global snakeHurtUp
    global snakeBodyNS
    global snakeBodyEW

    snakeHeadImg  = pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/snake_sprite_images/snake_head2.png')
    snakeBodyImg  = pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/snake_sprite_images/snake_body_NS.png')
    snakeHeadHurt = pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/snake_sprite_images/snake_head_hurt.png')
    foodImg = pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/icon_burger.png')
    game_over = pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/game_over1.png')


    snakeHeadRight = pygame.transform.rotate(snakeHeadImg, -90)
    snakeHeadLeft = pygame.transform.rotate(snakeHeadImg, 90)
    snakeHeadDown = pygame.transform.rotate(snakeHeadImg, 180)
    snakeHeadUp = pygame.transform.rotate(snakeHeadImg, 0)

    snakeHurtRight = pygame.transform.rotate(snakeHeadHurt, -90)
    snakeHurtLeft = pygame.transform.rotate(snakeHeadHurt, 90)
    snakeHurtDown = pygame.transform.rotate(snakeHeadHurt, 180)
    snakeHurtUp = pygame.transform.rotate(snakeHeadHurt, 0)

    snakeBodyNS = pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/snake_sprite_images/snake_body_NS.png')
    snakeBodyEW = pygame.transform.rotate(snakeBodyNS, 90)

pygame.init()
screen = pygame.display.set_mode((700, 500))
running = True
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(pygame.image.load('C:/Users/sky34/Desktop/GITHUB PROJECTS/Snake-Game/images/snake_icon.png'))

# Images
loadImages()

# Cords + Variables
snakeHeadX = 336
snakeHeadY = 21
snakeHeadXChange = 0
snakeHeadYChange = 0
Food = createNewFood()
score_value = 0
gameover = False
ate_food = False
font = pygame.font.Font('freesansbold.ttf', 32)
going = 'right'

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        going = checkKeyDown() # left, right, up, down

    # Handles the change of snake coordinates
    snakeHeadX += snakeHeadXChange # Changes the snakes head X cords
    snakeHeadY -= snakeHeadYChange # Changes the snakes head Y cords

    SNAKE[0] = (snakeHeadX, snakeHeadY)
    blitBackground()
    showScore()

    if checkCurrentFood(Food) == True: # Check if the snake collides with the food
        ate_food = True
        score_value += 1

    if ate_food == False: # Snake did not eat the food
        blitFood(Food)
    elif ate_food == True: # Snake ate the food
        ate_food = False
        Food = createNewFood()
        blitFood(Food)
        generateTailCords(going) # This generates the new tail cords

    # This handles the blit of the snake
    if checkerBorderCross() == True:
        blitSnakeHeadHurt(going)
        screen.blit(game_over, (250, 50))
        running = False
    else:
        blitSnake(going)

    print(SNAKE)
    pygame.display.update()
