import pygame


class Directory:
    def __init__(self, window):
        self.window = window
        self.rendering_engine = False

        self.objects = []

        self.test_flag = False