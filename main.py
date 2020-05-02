import pygame
import random
import math
from pygame.locals import *

buffor = random.randint(1, 100)
number = math.sqrt(buffor)
counter = 1
n1 = "_"
n2 = "_"
n3 = "_"
n4 = "_"
n5 = "_"
n6 = "_"
actualText = n1+" "+n2+" "+n3+"  <  sqrt(" + str(buffor) + ")  <  "+n1+" "+n2+" "+n3
k = None
size = x, y = 900, 600

pygame.init()

Screen= pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)

def on_event(Screen, event):
    if event.type == pygame.QUIT:
        Screen._running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
            k = 0
        if event.key == pygame.K_1:
            k = 1
        if event.key == pygame.K_2:
            k = 2
        if event.key == pygame.K_3:
            k = 3
        if event.key == pygame.K_4:
            k = 4
        if event.key == pygame.K_5:
            k = 5
        if event.key == pygame.K_6:
            k = 6
        if event.key == pygame.K_7:
            k = 7
        if event.key == pygame.K_8:
            k = 8
        if event.key == pygame.K_9:
            k = 9
        counter += 1

while (1==1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close the program any way you want, or troll users who want to close your program.
            raise SystemExit


    k = 10

    font = pygame.font.SysFont("Arial", 72)
    text = font.render(actualText, True, (0, 128, 0))

    Screen.fill((255, 255, 255))
    Screen.blit(text,
                ((x - text.get_width())/2, (y - text.get_height())/2))

    pygame.display.flip()

    # print(buffor)
    # print(number)

    if k < 10:
        k = 10

