import sys
import pygame
from game import Game



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Ubuntu", 25)
    pygame.display.set_caption("Ships battle")

    game = Game(clock, screen, font)
    game.run()  # run

    pygame.quit()


