# learn.adafruit.com/raspberry-pi-pygame-ui-basics/from-gpio-to-screen
import pygame
import os
from time import sleep
from pygame.locals import *
#import RPi.GPIO as GPIO

# key = PIN
# value = points
# sensor_map = (
#     4: 100,
#     17: 50,
#     27: 40,
#     22: 30,
#     23: 20,
#     5: 10
# )

# setup IR beam pins
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(FALSE)
# for k in sensor_map.keys():
#     GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    #setup env - ? let SDL know which frame buffer
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    # pygame.mouse.set_visible(False)
    lcd = pygame.display.set_mode((320,240))

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEMOTION:
                print ('MOUSEMOTION')
            elif event.type == MOUSEBUTTONDOWN:
                print ('MOUSEBUTTONDOWN')
            elif event.type == MOUSEBUTTONUP:
                print ('MOUSEBUTTONUP')
                print(event.__dict__)
                if (event.button == 3):
                    print('right click')
                elif (event.button == 1):
                    print('click')
            elif event.type == KEYDOWN:
                print ('KEYDOWN')
            elif event.type == KEYUP:
                print ('KEYUP')
            elif event.type == 1:
                print ('ENTER')
            else:
                print(event.type)
        font_big = pygame.font.Font(None, 100)
        #RED
        lcd.fill((255,0,0))
        text_surface = font_big.render(str(event.type), True, (255,255,255))

        rect = text_surface.get_rect(center=(160,120))
        lcd.fill((255,0,255))
        lcd.blit(text_surface, rect)
        pygame.display.update()
        sleep(0.1)

    #
    # font_big = pygame.font.Font(None, 100)
    # #RED
    # lcd.fill((255,0,0))
    # text_surface = font_big.render('21', True, (255,255,255))
    #
    # rect = text_surface.get_rect(center=(160,120))
    # lcd.blit(text_surface, rect)
    #
    # pygame.display.update()

    # Loop


if __name__ == '__main__' : main()
