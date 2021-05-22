import pygame
from gameObject import GameObject
from bullet import Bullet


class Ship(GameObject):

    def __init__(self, x, y, rotate=False):
        GameObject.__init__(self, 'imgs/ship.png', x, y, rotate)
        
        self._bullets = []


    def render(self, screen):
        super().render(screen)

        for bullet in self._bullets:
            bullet.render(screen)

    def tick(self):
        super().tick()        

        for bullet in self._bullets:
            
            bullet.tick()

            if bullet.isOutSideOfWindow():
                self._bullets.remove(bullet)


    def fier(self):
        self._bullets.append(Bullet(self._hit_box.x, self._hit_box.y, self, self._rotate))
