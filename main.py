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

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 940, 800

    def on_init(self):
        pygame.init()

        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or2 event.key == pygame.K_9:
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

            font = pygame.font.SysFont("Arial", 72)
            text = font.render(actualText, True, (0, 128, 0))

            self._display_surf.fill((255, 255, 255))
            self._display_surf.blit(text,
                        ((self.width - text.get_width())/2, (self.height - text.get_height())/2))

            pygame.display.flip()

            # print(buffor)
            # print(number)

            if k < 10:
                k = 10


            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":

    theApp = App()
    theApp.on_execute()


