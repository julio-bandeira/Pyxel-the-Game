import pygame

class Ground(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('./Blocks/assets/ground.png') #just a image of test
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def draw(self, display, scroll):
        pos = ((self.rect.x - scroll[0]), (self.rect.y - scroll[1]))
        display.blit(self.image, pos)

class Grass(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('./Blocks/assets/grass.png') #just a image of test
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def draw(self, display, scroll):
        pos = ((self.rect.x - scroll[0]), (self.rect.y - scroll[1]))
        display.blit(self.image, pos)

class Plant(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('./Blocks/assets/plant.png') #just a image of test
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def draw(self, display, scroll):
        pos = ((self.rect.x - scroll[0]), (self.rect.y - scroll[1]))
        display.blit(self.image, pos)