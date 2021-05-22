
import pygame
from pygame.transform import rotate
from gameObject import GameObject

class Bullet(GameObject):

    def __init__(self, x, y, enemy_ship, rotate=False):
        GameObject.__init__(self, 'imgs/bullet.png', x, y, rotate)

        self._enemy_ship = enemy_ship
        self._vel_y = -1
        self._dead = False

        if rotate:
            self._vel_y *= -1    

    def tick(self):
        super().tick()

        if self.collides(self._enemy_ship):
            self._enemy_ship.hit()
            self._dead = True

    def isOutSideOfWindow(self):
        return self._hit_box.y + self._hit_box.height < 0 or self._hit_box.y > 600 or self._dead