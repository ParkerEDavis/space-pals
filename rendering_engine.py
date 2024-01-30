import pygame
import layer


class RenderingEngine:
    def __init__(self, directory, window, width, height):
        # Initial Variables
        self.directory = directory

        self.window_width = width
        self.window_height = height
        self.window = window
        
        # Layer Holders
        # The dictionary is for other objects to access, through the key
        # The Array is for sorting the layers by weight, and is only used in the draw function.
        self.layers = {}
        self.sorted_layers = []

        # Create Initial Layers
        self.createLayer("background", 100)

        # Sort layers
        self.sorted_layers.sort(key=lambda x: x.weight, reverse=True)
    

    def createLayer(self, key, weight):
        # Create Layer
        temp_layer = layer.Layer(self.window_width, self.window_height, weight)

        # Put it into layer holders
        self.layers[key] = temp_layer
        self.sorted_layers.append(temp_layer)

        # Sort layers
        self.sorted_layers.sort(key=lambda x: x.weight, reverse=True)



    def changeWeight(self, key, new_weight):
        # Change desired weight
        self.layers[key].weight = new_weight

        # Sort layers
        self.sorted_layers.sort(key=lambda x: x.weight, reverse=True)
        print(self.layers)
    
    
    def draw(self):
        self.window.fill((200, 100, 100))

        for layer in self.sorted_layers:
            self.window.blit(layer.surface, (0, 0))
        
        pygame.display.flip()