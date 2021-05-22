import pygame
from pygame import Rect

class GameObject:

    def __init__(self, image_path, x, y, rotate=False):

        self._rotate = rotate
        self._img = pygame.image.load(image_path)

        if rotate:
            self._img = pygame.transform.rotate(self._img, 180)


        self._hit_box = Rect(x, y, self._img.get_width(), self._img.get_height())

        self._vel_x = 0
        self._vel_y = 0
        


    def render(self, screen):
        screen.blit(self._img, (self._hit_box.x, self._hit_box.y))

        #hit box
        pygame.draw.rect(screen, (255, 0, 0), (self._hit_box.x, self._hit_box.y, self._hit_box.width, self._hit_box.height), 1)
        

    def tick(self):
        self._hit_box.x += self._vel_x
        self._hit_box.y += self._vel_y

    def collides(self, other_Game_object):
        return other_Game_object._hit_box.colliderect(self._hit_box)