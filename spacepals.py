import pygame
import rendering_engine


class SpacePals:
    def __init__(self):
        # Define window
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # Initialize Modules
        self.renderer = rendering_engine.RenderingEngine(self.window)

        # Test Zone
        self.test_flag = False

        # Make sure the game runs properly.
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.running = True
    

    def eventHandler(self):
        for event in pygame.event.get():
            # The Quit Button
            if event.type == pygame.QUIT:
                self.running = False
            
            # On a keypress
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                if event.key == pygame.K_SPACE:
                    self.test_flag = not self.test_flag

            # On a keyrelease
            # if event.type == pygame.KEYUP:
    

    def run(self):
        while self.running:
            # Grab Events
            self.eventHandler()

            # Update

            # Draw
            self.draw()

            # And pause until next frame
            self.clock.tick(self.FPS)
    

    def draw(self):
        # Move this to a rendering object
        self.renderer.draw(self.test_flag)