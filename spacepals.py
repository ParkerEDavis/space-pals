import pygame
import rendering_engine
import directory
import button

class SpacePals:
    def __init__(self):
        # Define window
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # Generate directory first
        self.directory = directory.Directory(self.window)

        # Initialize Modules
        self.rendering_engine = rendering_engine.RenderingEngine(self.directory, self.window, self.window_width, self.window_height)

        # Link Modules to Directory
        self.directory.rendering_engine = self.rendering_engine

        # Test Zone
        self.test_flag = False

        self.rendering_engine.createLayer('A', 3)
        self.rendering_engine.createLayer('B', 2)
        self.rendering_engine.createLayer('C', 1)

        self.rendering_engine.layers['A'].surface.blit(pygame.transform.scale(pygame.image.load("assets/images/A.png"), (200, 200)), (100, 100))
        #self.rendering_engine.layers['B'].surface.blit(pygame.transform.scale(pygame.image.load("assets/images/B.png"), (200, 200)), (200, 200))
        self.rendering_engine.layers['C'].surface.blit(pygame.transform.scale(pygame.image.load("assets/images/C.png"), (200, 200)), (300, 300))

        self.butttest = button.Button(self.directory, 200, 200, 200, 200, "B", "testFunc", (100, 100, 255))
        self.directory.objects.append(self.butttest)

        # Make sure the game runs properly.
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.running = True
    

    def inputHandler(self):
        for event in pygame.event.get():
            # The Quit Button
            if event.type == pygame.QUIT:
                self.running = False
            
            # On a keypress
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                if event.key == pygame.K_SPACE:
                    #self.directory.rendering_engine.layers["background"].surface.blit(pygame.image.load("assets/images/image.png"), (100, 100))
                    for layer in self.rendering_engine.sorted_layers:
                        print(layer.weight)

            # On a keyrelease
            # if event.type == pygame.KEYUP:
    

    def run(self):
        while self.running:
            # Grab Events
            self.inputHandler()

            # Update

            # Draw
            self.draw()

            # And pause until next frame
            self.clock.tick(self.FPS)
    

    def draw(self):
        # Move this to a rendering object
        self.rendering_engine.draw()