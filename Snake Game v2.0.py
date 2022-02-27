"""
Program:    Snake Game
Author:     Sky Good
Date:       1/5/2022
"""

import random
import pygame
import time

def background():
    """
    Purpose:    Blits the backround to the window
    Parameters: None
    Returns:    None
    """
    screen.blit(pygame.image.load('snake-in-python-repo\images\Background_images\Background2.png'), (0,0))

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


def food(food):
    """
    Purpose:    Blits food to the window
    Parameters: food
    Returns:    None
    """
    screen.blit(foodImg, (food[0], food[1]))

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

def checkerBorderCross(snake):
    """
    Purpose:    Checks if the snake position has crossed the border
    Parameters: snake
    Returns:    T/F
    """
    if snake[0][0] < 336:
        return True
    elif snake[0][0] >= 642:
        return True
    if snake[0][1] < 21:
        return True
    elif snake[0][1] >= 327:
        return True

def checkCurrentFood(snake, Food):
    """
    Purpose:    Checks snakes collision with food
    Parameters: snake, Food
    Returns:    T/F
    """
    if Food[0] <= snake[0][0] <= (Food[0] + 34) and Food[1] <= snake[0][1] <= (Food[1] + 34):
        return True
    elif Food[0] <= (snake[0][0] + 34) <= (Food[0] + 34) and Food[1] <= (snake[0][1] + 34) <= (Food[1] + 34):
        return True
    elif Food[0] <= snake[0][0] <= (Food[0] + 34) and Food[1] <= (snake[0][1] + 34) <= (Food[1] + 34):
        return True
    elif Food[0] <= (snake[0][0] + 34) <= (Food[0] + 34) and Food[1] <= snake[0][1] <= (Food[1] + 34):
        return True
    else:
        return False

def showScore(x,y):
    """
    Purpose:    Renders the score to the window
    Parameters: x, y
    Returns:    None
    """
    score = font.render(str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))

def smoothMovement(x,y): #Still not working completely correctly...
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

def generateTailCords(snake, going):
    """
    Purpose:    Creates the coordinates for the next tail piece
    Parameters: snake, going
    Returns:    snake
    """
    if going == "up":
        x = snake[-1][0]
        y = snake[-1][1] - 34
    elif going == "right":
        x = snake[-1][0] - 34
        y = snake[-1][1]
    elif going == "down":
        x = snake[-1][0]
        y = snake[-1][1] + 34
    elif going == "left":
        x = snake[-1][0] + 34
        y = snake[-1][1]
    snake.append((x,y))

    return snake

#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         Window          #=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
pygame.init()
screen = pygame.display.set_mode((700, 500))
running = True
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load('snake-in-python-repo\images\snake_icon.png'))


#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#         Images          #=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
snakeHeadImg  = pygame.image.load('snake-in-python-repo\images\snake_sprite_images\snake_head2.png')
snakeBodyImg  = pygame.image.load('snake-in-python-repo\images\snake_sprite_images\snake_body_NS.png')
snakeHeadHurt = pygame.image.load('snake-in-python-repo\images\snake_sprite_images\snake_head_hurt.png')
foodImg = pygame.image.load("""snake-in-python-repo\images\icon_burger.png""")
game_over = pygame.image.load('snake-in-python-repo\images\game_over1.png')


snakeHeadRight = pygame.transform.rotate(snakeHeadImg, -90)
snakeHeadLeft = pygame.transform.rotate(snakeHeadImg, 90)
snakeHeadDown = pygame.transform.rotate(snakeHeadImg, 180)
snakeHeadUp = pygame.transform.rotate(snakeHeadImg, 0)

snakeHurtRight = pygame.transform.rotate(snakeHeadHurt, -90)
snakeHurtLeft = pygame.transform.rotate(snakeHeadHurt, 90)
snakeHurtDown = pygame.transform.rotate(snakeHeadHurt, 180)
snakeHurtUp = pygame.transform.rotate(snakeHeadHurt, 0)

snakeBodyNS = pygame.image.load('snake-in-python-repo\images\snake_sprite_images\snake_body_NS.png')
snakeBodyEW = pygame.transform.rotate(snakeBodyNS, 90)


#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#    Cords + Variables    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
snakeHeadX = 336
snakeHeadY = 21
snake = [(370,21),(336,21)]
snakeHeadXChange = 0
snakeHeadYChange = 0
Food = createNewFood()
score_value = 0
gameover = False
ate_food = False
font = pygame.font.Font('freesansbold.ttf', 32)
going = 'right'


#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#        Game Loop        #=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=##=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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


    #Movement
    snakeHeadX += snakeHeadXChange
    snakeHeadY -= snakeHeadYChange
    snake[0] = (snakeHeadX, snakeHeadY)
    background() #Displays the backround
    if checkCurrentFood(snake, Food) == True:
        ate_food = True
        score_value += 1
    if ate_food == False:
        food(Food)
    elif ate_food == True:
        ate_food = False
        Food = createNewFood()
        food(Food)
        snake = generateTailCords(snake, going)




    if checkerBorderCross(snake) == True:
        snakeHeadX -= snakeHeadXChange
        snakeHeadY += snakeHeadYChange
        if going == 'right':
            screen.blit(snakeHurtRight, (snakeHeadX,snakeHeadY))
        elif going == 'down':
            screen.blit(snakeHurtDown, (snakeHeadX,snakeHeadY))
        elif going == 'left':
            screen.blit(snakeHurtLeft, (snakeHeadX,snakeHeadY))
        elif going == 'up':
            screen.blit(snakeHurtUp, (snakeHeadX,snakeHeadY))
        screen.blit(game_over, (250, 50))
        #running = False
    else:
        if going == 'right':
            screen.blit(snakeHeadRight, (snakeHeadX,snakeHeadY))
            snakeBody_EW(snake, snakeHeadXChange, snakeHeadYChange, going)
        elif going == 'down':
            screen.blit(snakeHeadDown, (snakeHeadX,snakeHeadY))
            snakeBody_NS(snake, snakeHeadXChange, snakeHeadYChange, going)
        elif going == 'left':
            screen.blit(snakeHeadLeft, (snakeHeadX,snakeHeadY))
            snakeBody_EW(snake, snakeHeadXChange, snakeHeadYChange, going)
        elif going == 'up':
            screen.blit(snakeHeadUp, (snakeHeadX,snakeHeadY))
            snakeBody_NS(snake, snakeHeadXChange, snakeHeadYChange, going)
    showScore(160,82)
    #print("X = " + str(snake[0][0]) + " Y = " + str(snake[0][1]) + " Score: " + str(score_value)) #Prints info to the console
    pygame.display.update()

