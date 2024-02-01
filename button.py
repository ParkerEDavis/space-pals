import pygame


# A button needs:
# A Layer for display
# X, Y Coordinates
# Width, Height Sizes
# A Flag that is called when it is pushed
# Color: Temporary, will be replaced with texture later
class Button:
    def __init__(self, directory, x, y, w, h, layer, flag, color):
        # Directory
        self.directory = directory

        # Dimensions
        self.x = x
        self.y = y
        self.width = w
        self.height = h

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Layer
        self.layer = layer

        # What flag is sent to the future flag handler when this is pushed.
        self.flag = flag

        self.color = color
    

    def draw(self):
        pygame.draw.rect(self.directory.rendering_engine.layers[self.layer].surface, self.color, self.rect)