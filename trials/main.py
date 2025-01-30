import sys, pygame
import RPi.GPIO as GPIO

pygame.init()

screen = pygame.display.set_mode()
info = pygame.display.Info()

width = info.current_w
height = info.current_h
size = width, height
speed = [20, 20]
black = 0, 0, 0

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
