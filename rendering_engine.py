import pygame


class RenderingEngine:
    def __init__(self, window):
        self.window = window
    

    def testFunc(self, test_flag):
        if test_flag:
            self.window.blit(pygame.image.load("assets/images/image.png"), (0, 0))
    
    
    def draw(self, test_flag):
        self.window.fill((200, 100, 100))
        self.testFunc(test_flag)
        pygame.display.flip()