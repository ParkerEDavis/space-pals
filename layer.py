import pygame


class Layer:
    def __init__(self, width, height, weight):
        self.width = width
        self.height = height
        self.weight = weight

        self.surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))