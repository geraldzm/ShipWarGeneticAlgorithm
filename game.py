import pygame
from ship import Ship
from ship import Ship
from geneticAlgorithm import GA

class Game:

    # E: objeto clock, screen y front de pygame
    # constructor del juego
    def __init__(self, clock, screen, font):
        self._clock = clock
        self._screen = screen  # 840, 630 window size
        self._font = font
        self._game_on = True
        self._background = pygame.image.load('imgs/background.png')  # 800 x 600

        ship0 = Ship(380, 100, True)
        ship1 = Ship(380, 500)

        ship0_ga = GA(ship0, ship1)
        ship1_ga = GA(ship1, ship0)

        self._game_objects = [ship0, ship1, ship0_ga, ship1_ga]


    # S: un objeto de tipo pygame.Surface
    # retorna un objeto que se puede mostrar en pantalla
    # con el numero de fps
    def fps(self):
        frameRate = str(int(self._clock.get_fps()))
        frameRateText = self._font.render(frameRate, 1, pygame.Color('coral'))
        return frameRateText



    def render(self):
        
        self._screen.blit(self._background, (0, 0))

        for object in self._game_objects:
            object.render(self._screen)

        #fps
        self._screen.blit(self.fps(), (10, 0))


    def manageEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_on = False

    def tick(self):        
        self.manageEvents()

        for object in self._game_objects:
            object.tick()
                



    def run(self):

        while self._game_on:
            self.render()
            self.tick()
            self._clock.tick(30)
            pygame.display.update()