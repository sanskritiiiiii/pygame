
import pygame
from pygame_functions import *
import random

# Defining the Functions that are Used

# Out

playerImg = pygame.image.load('Images/out.jpg')


def playerout():
    screen.blit(playerImg, (10, 200))


# 1

playerImg1 = pygame.image.load('Images/one.png')


def playerone():
    screen.blit(playerImg1, (10, 200))


# 2

playerImg2 = pygame.image.load('Images/two.jpg')


def playertwo():
    screen.blit(playerImg2, (10, 200))


# 3

playerImg3 = pygame.image.load('Images/three.png')


def playerthree():
    screen.blit(playerImg3, (10, 200))


# 4

playerImg4 = pygame.image.load('Images/four.jpg')


def playerfour():
    screen.blit(playerImg4, (10, 200))


# 5

playerImg5 = pygame.image.load('Images/five.jpg')


def playerfive():
    screen.blit(playerImg5, (10, 200))


# 6

playerImg6 = pygame.image.load('Images/six.jpg')


def playersix():
    screen.blit(playerImg6, (10, 200))


# won

playerImg7 = pygame.image.load('Images/won.jpg')


def won():
    screen.blit(playerImg7, (10, 200))


# Loss

playerImg8 = pygame.image.load('Images/lost.jpg')


def loss():
    screen.blit(playerImg8, (10, 200))


# Initialising pygame

pygame.init()

# Window creation

screen = pygame.display.set_mode((800, 600))

# Screen Creation

screenSize(800, 800)

# Setting Window Icon and Title

pygame.display.set_caption('CrickPlay')
icon = pygame.image.load('Images/game.png')
pygame.display.set_icon(icon)

# Displaying Text

instructionLabel = makeLabel(
    'Welcome to Virtual Cricket Game',
    40,
    10,
    10,
    'blue',
    'Agency FB',
    'yellow',
    )
showLabel(instructionLabel)

# Displaying Text

instructionLabel1 = makeLabel(
    'What you wanna do?(Bowling/Batting):-',
    40,
    10,
    55,
    'blue',
    'Agency FB',
    'green',
    )
showLabel(instructionLabel1)

# Creating text Box

wordBox = makeTextBox(
    508,
    55,
    200,
    0,
    'Enter Text here',
    7,
    24,
    )
showTextBox(wordBox)
entry = textBoxInput(wordBox)

# Hiding Labels

hideLabel(instructionLabel1)
hideLabel(wordBox)

# Displaying Text

instructionLabel2 = makeLabel(
    'Good that you decided to do:-',
    40,
    10,
    55,
    'blue',
    'Agency FB',
    'green',
    )
showLabel(instructionLabel2)

# Displaying Text

instructionLabel3 = makeLabel(
    entry,
    40,
    376,
    55,
    'blue',
    'Agency FB',
    'green',
    )
showLabel(instructionLabel3)

# Displaying Text

instructionLabel4 = makeLabel(
    'From here you go:- ',
    40,
    10,
    100,
    'blue',
    'Agency FB',
    'green',
    )
showLabel(instructionLabel4)

# Taking User Inputs and Checking and Calculations

x = True
Runs = 0
while x == True:

    instructionLabel5 = makeLabel(
        'Enter number for the ball:-',
        40,
        10,
        146.5,
        'blue',
        'Agency FB',
        'green',
        )
    showLabel(instructionLabel5)

    wordBox1 = makeTextBox(
        345,
        146.5,
        60,
        0,
        'Enter ',
        7,
        24,
        )
    showTextBox(wordBox1)
    Run = textBoxInput(wordBox1)
    run = int(Run)

    hideLabel(instructionLabel5)
    hideLabel(wordBox1)

    run1 = random.randint(1, 7)  # Creating second value

    if run == run1:  # Comparing both the inputs
        playerout()

        instructionLabel6 = makeLabel(
            "It's Out!",
            30,
            10,
            100,
            'Red',
            'Agency FB',
            'Black',
            )
        showLabel(instructionLabel6)
        instructionLabel7 = makeLabel(
            'Runs Scored:-',
            30,
            10,
            130,
            'Red',
            'Agency FB',
            'Black',
            )
        showLabel(instructionLabel7)
        Runs = str(Runs)
        instructionLabel8 = makeLabel(
            Runs,
            30,
            140,
            130,
            'red',
            'Agency FB',
            'Black',
            )
        showLabel(instructionLabel8)
        Runs = int(Runs)

        break
    else:

                                          # printing repective images and some calculations

        Runs = Runs + run
        if run == 1:
            playerone()
        elif run == 2:
            playertwo()
        elif run == 3:
            playerthree()
        elif run == 4:
            playerfour()
        elif run == 5:
            playerfive()
        elif run == 6:
            playersix()

# Some important labels according to respective situations

if entry == 'Bowling':
    hideLabel(instructionLabel4)
    instructionLabel9 = makeLabel(
        'Target is :-',
        40,
        10,
        160,
        'red',
        'Agency FB',
        'black',
        )
    showLabel(instructionLabel9)
    Target = Runs + 1
    Target = str(Target)
    instructionLabel10 = makeLabel(
        Target,
        40,
        150,
        160,
        'red',
        'Agency FB',
        'black',
        )
    showLabel(instructionLabel10)
else:

    hideLabel(instructionLabel4)
    instructionLabel9 = makeLabel(
        'Runs to defend:-',
        40,
        10,
        160,
        'Red',
        'Agency FB',
        'Black',
        )
    showLabel(instructionLabel9)
    Target = Runs + 1
    Target = str(Target)
    instructionLabel10 = makeLabel(
        Target,
        40,
        220,
        160,
        'red',
        'Agency FB',
        'black',
        )
    showLabel(instructionLabel10)

pause(5000)  # Time Labels will stay(in milliseconds)

# 2 innings

Runs1 = 0
while x == True:
    hideLabel(instructionLabel6)
    hideLabel(instructionLabel7)
    hideLabel(instructionLabel8)
    hideLabel(instructionLabel9)
    hideLabel(instructionLabel10)
    hideLabel(instructionLabel2)
    hideLabel(instructionLabel3)

    instructionLabel2 = makeLabel(
        'Now you have to:-',
        40,
        10,
        55,
        'blue',
        'Agency FB',
        'green',
        )
    showLabel(instructionLabel2)

    if entry == 'Bowling':
        instructionLabel3 = makeLabel(
            'Bat',
            40,
            230,
            55,
            'blue',
            'Agency FB',
            'green',
            )
        showLabel(instructionLabel3)
    else:
        instructionLabel3 = makeLabel(
            'Bowl',
            40,
            230,
            55,
            'blue',
            'Agency FB',
            'green',
            )
        showLabel(instructionLabel3)

    instructionLabel5 = makeLabel(
        'Enter number for the ball:-',
        40,
        10,
        100,
        'blue',
        'Agency FB',
        'green',
        )
    showLabel(instructionLabel5)

    run1 = random.randint(1, 7)

    wordBox1 = makeTextBox(
        345,
        100,
        60,
        0,
        'Enter ',
        1,
        24,
        )
    showTextBox(wordBox1)
    Run = textBoxInput(wordBox1)
    run = int(Run)

    hideLabel(instructionLabel5)
    hideLabel(wordBox1)

    if Run == run1:
        if entry == 'Bowling':
            loss()

            instructionLabel6 = makeLabel(
                "It's Out!",
                30,
                10,
                100,
                'Red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel6)
            instructionLabel7 = makeLabel(
                'Runs Scored:-',
                30,
                10,
                130,
                'Red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel7)
            Runs1 = str(Runs1)
            instructionLabel8 = makeLabel(
                Runs1,
                30,
                140,
                130,
                'red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel8)
            Runs1 = int(Runs1)

            instructionLabel9 = makeLabel(
                'You Lost',
                30,
                140,
                130,
                'red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel9)

            break
        else:

            won()
            hideLabel(instructionLabel2)
            hideLabel(instructionLabel3)
            hideLabel(instructionLabel5)
            hideLabel(wordBox1)

            instructionLabel11 = makeLabel(
                'You Won',
                30,
                10,
                60,
                'red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel11)
            won()
            break

    Runs1 = Runs1 + run

    if Runs1 > Runs:
        if entry == 'Bowling':
            won()
            hideLabel(instructionLabel2)
            hideLabel(instructionLabel3)
            hideLabel(instructionLabel5)
            hideLabel(wordBox1)

            instructionLabel11 = makeLabel(
                'You Won',
                30,
                10,
                60,
                'red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel11)
            won()
            break
        else:
            loss()

            hideLabel(instructionLabel2)
            hideLabel(instructionLabel3)

            instructionLabel7 = makeLabel(
                'Runs Scored:-',
                30,
                10,
                130,
                'Red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel7)
            Runs1 = str(Runs1)
            instructionLabel8 = makeLabel(
                Runs1,
                30,
                140,
                130,
                'red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel8)
            Runs1 = int(Runs1)
            instructionLabel9 = makeLabel(
                'You Lost',
                30,
                10,
                160,
                'red',
                'Agency FB',
                'Black',
                )
            showLabel(instructionLabel9)

            break
    else:

        if run == 1:
            playerone()
        elif run == 2:
            playertwo()
        elif run == 3:
            playerthree()
        elif run == 4:
            playerfour()
        elif run == 5:
            playerfive()
        elif run == 6:
            playersix()

# Event exiting and stuff

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False