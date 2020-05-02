import pygame
import random
import math
from pygame.locals import *


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 940, 800

    def on_init(self):
        pygame.init()

        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
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

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            k = 10
            for event in pygame.event.get():
                self.on_event(event)

            buffor = random.randint(1, 100)

            number = math.sqrt(buffor)
            myfont = pygame.font.SysFont("monospace", 15)
            label = myfont.render("Some text!", 1, (255, 255, 0))
            screen.blit(label, (100, 100))

            print(buffor)
            print(number)

            if k < 10:
                k = 10


            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()