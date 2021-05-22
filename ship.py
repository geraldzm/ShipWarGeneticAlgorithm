import pygame
from gameObject import GameObject
from bullet import Bullet


class Ship(GameObject):

    def __init__(self, x, y, rotate=False):
        GameObject.__init__(self, 'imgs/ship.png', x, y, rotate)
        
        self._bullets = []
        self._enemy_ship = None
        self._helth = 3
        self._dead = False


    def render(self, screen):
        super().render(screen)

        if not self._dead:
            self.render_alive(screen)
        else:
            self.render_dead(screen)
        

    def render_alive(self, screen):
        for bullet in self._bullets:
            bullet.render(screen)

    def render_dead(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self._hit_box.x, self._hit_box.y, self._hit_box.width, self._hit_box.height))

    def tick(self):
        super().tick()        

        for bullet in self._bullets:
            
            bullet.tick()

            if bullet.isOutSideOfWindow():
                self._bullets.remove(bullet)


    def fier(self):
        self._bullets.append(Bullet(self._hit_box.x, self._hit_box.y, self._enemy_ship, self._rotate))

    def hit(self):
        self._helth -= 1

        if self._helth <= 0:
            self._dead = True
