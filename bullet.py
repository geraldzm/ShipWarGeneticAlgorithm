
import pygame
from pygame.transform import rotate
from gameObject import GameObject

class Bullet(GameObject):

    def __init__(self, x, y, ship_owner, rotate=False):
        GameObject.__init__(self, 'imgs/bullet.png', x, y, rotate)

        self._vel_y = -1

        if rotate:
            self._vel_y *= -1    


    def isOutSideOfWindow(self):
        return self._hit_box.y + self._hit_box.height < 0 or self._hit_box.y > 600