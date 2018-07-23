import pygame
import time
from random import *
pygame.init()

blue = (113,177,227)
white = (255,255,255)
width = 1280
height = 720

speedEasy =1.25
speedMedium = 2
speedHard = 2.5
window = pygame.display.set_mode((width,height))
backGroungImage = pygame.image.load('pic/gameBack.png').convert()
clock = pygame.time.Clock()
pygame.display.set_caption("--FLAPPY RAYNAL--")
character = pygame.image.load('pic/perso.png')
character = pygame.transform.scale(character, (100,159))
pipeHigh = pygame.image.load('pic/pipe.png')

pipeDown = pygame.image.load('pic/pipeReversed.png')

run = True


def getScore(count):
    msgFont = pygame.font.Font('pic/BradBunR.ttf',30)
    txt = msgFont.render("Score: "+str(count),True,white)
    window.blit(txt,[10,0])


def pipeDisplay(x_pipe,y_pipe, space):
    window.blit(pipeDown,(x_pipe,y_pipe))
    window.blit(pipeHigh, (x_pipe,y_pipe+x_pipe+space))


def gameAgain():
    for event in pygame.event.get([pygame.KEYUP,pygame.KEYDOWN,pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None


def createTextObj(txt,Font):
    txtWindow = Font.render(txt,True,white)
    return txtWindow,txtWindow.get_rect()

def message(text):
    bigFont = pygame.font.Font('pic/BradBunR.ttf',150)
    litleFont = pygame.font.Font('pic/BradBunR.ttf',20)

    bigFontWindow , bigFontRect = createTextObj(text,bigFont)
    bigFontRect.center = width/2 , ((height/2)-50)
    window.blit(bigFontWindow,bigFontRect)

    litleFontWindow, litleFontRect = createTextObj("Appuyer sur une touche pour continuer", litleFont)
    litleFontRect.center = width/2 , ((height/2)+50)
    window.blit(litleFontWindow,litleFontRect)
    pygame.display.update()


    while gameAgain() == None:
        clock.tick()

    mainGame()

def gameOver():
    message("Game Over !!!! ")


def position(x,y,img):
    window.blit(img , (x,y))

def mainGame(speed):
    x = 150
    y = 200
    y_move = 0

    widthCharacter , heightCharacter = 164,261
    pipeWidth , pipeHeight = 52 ,320
    x_pipe = width
    y_pipe = randint(-300,20)
    pipe_space = heightCharacter *2
    speed_pipe = speed

    currentScore = 0

    pygame.display.update()

    game_close = False

    while not game_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_move = -2
            if event.type == pygame.KEYUP:
                y_move = 2

        y += y_move
        position(0,0, backGroungImage)
        position(x,y,character)
        pipeDisplay(x_pipe,y_pipe,pipe_space)
        getScore(currentScore)

        x_pipe -= speed_pipe

        if y>height -40 or y< -10:
            gameOver()

        if x + widthCharacter > x_pipe + 40:
            if y < y_pipe +heightCharacter -40:
                if x-widthCharacter < x_pipe + pipeWidth -40:
                    gameOver()

        if x + widthCharacter > x_pipe+40:
            if y + heightCharacter > y_pipe+pipeHeight + pipe_space+40:
                if x - widthCharacter < x_pipe +pipeHeight -40:
                    gameOver()


        if x_pipe < (-1*pipeWidth):
            x_pipe = width
            y_pipe = randint(-300,20)

        if x_pipe < (x-pipeWidth) < x_pipe + speed_pipe:
            currentScore += 1


        pygame.display.flip()


def main():
    while 1:
        runHome = True
        runGame = False

        backHome = pygame.image.load('pic/homeBack.png').convert_alpha()
        backLevel = pygame.image.load('pic/levelBack.png').convert_alpha()
        pygame.display.update()

        # HOME
        while runHome:
            pygame.time.Clock().tick(30)
            window.blit(backHome, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    runHome = False
                    run = False
                    runGame = False
                    print("Quit_On_Home")
                if event.type == pygame.KEYDOWN and event.key != pygame.K_ESCAPE:
                    print("Running_Game")
                    runGame = True
                    runHome = False
            pygame.display.flip()

        # GAME
        while runGame:
            window.blit(backLevel,(0,0))
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    runHome = True
                    runGame = False
                    print("Game_To_Home")

                if event.type == pygame.QUIT:
                    run = False
                    runHome = False
                    runGame = False
                    print("Quit_On_Game")

                if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                    mainGame(speedEasy)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
                    mainGame(speedMedium)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
                    mainGame(speedHard)


#mainGame(speedEasy)
main()
pygame.quit()
quit()
