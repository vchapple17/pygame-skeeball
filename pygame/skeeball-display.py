# learn.adafruit.com/raspberry-pi-pygame-ui-basics/from-gpio-to-screen
import pygame
import os
from time import sleep
from pygame.locals import *
from pygame.time import wait, get_ticks

def main():

    RADIUS = 15
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    lcd = pygame.display.set_mode((200,400))
    font = pygame.font.Font(None, 50)
    font_big = pygame.font.Font(None, 100)
    lcd.fill((100,50,0))

    # holes
    hole_map = {
        10: (100, 350),
        20: (100, 320),
        30: (100, 290),
        40: (100, 260),
        50: (100, 230),
        100: (30, 30),
    }

    displayBoard(lcd, hole_map);
    #
    # for (score, pos) in hole_map.items():
    #     text_surface = font.render('%d'%score, True, (255,255,255))
    #     rect = text_surface.get_rect(center=pos)
    #     lcd.blit(text_surface, rect)

    pygame.display.update()

    total_score = 0;

    scoreShowing = False;
    ballCount = 0;
    MAX_BALL_COUNT = 9;

    while ballCount < MAX_BALL_COUNT:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONUP:
                posX = event.pos[0]
                posY = event.pos[1]
                if scoreShowing == True:
                    displayBoard(lcd, hole_map)
                    scoreShowing = False
                else:
                    ballCount += 1
                    for (score, pos) in hole_map.items():
                        if (scoreShowing == False and posX <= pos[0]+RADIUS and posX >= pos[0]-RADIUS) and (posY <= pos[1]+RADIUS and posY >= pos[1]-RADIUS):
                            total_score += score
                            print('SCORE!')
                            score = font_big.render('%d'%total_score, True, (255,255,255))
                            rect = score.get_rect(center=(100,200))
                            lcd.fill((100,50,0))
                            lcd.blit(score, rect)
                            pygame.display.update()
                            scoreShowing = True;
                            break;
        sleep(0.1)


    gameOver = font_big.render('GAME OVER', True, (30,30,30))
    rect = gameOver.get_rect(center=(100,200))
    lcd.fill((100,50,0))
    lcd.blit(gameOver, rect)
    pygame.display.update()
    sleep(4)

def displayBoard(lcd, hole_map):
    lcd.fill((100,50,0))
    font = pygame.font.Font(None, 50)
    for (score, pos) in hole_map.items():
        text_surface = font.render('%d'%score, True, (255,255,255))
        rect = text_surface.get_rect(center=pos)
        lcd.blit(text_surface, rect)
    pygame.display.update()

if __name__ == '__main__' : main()
