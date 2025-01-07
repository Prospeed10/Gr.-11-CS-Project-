import pygame
from settings import vertical_tile_number, tile_size, screen_width, screen_height

class Background:
    def __init__(self, horizon):
        # Load the background image
        self.background = pygame.image.load('./graphics/decoration/background.png').convert()

        # Load the image to be placed below the background
        self.foreground = pygame.image.load('./graphics/decoration/underground.png').convert()

        # Store the horizon (if needed for other uses, like scroll position)
        self.horizon = horizon

        # Get the original dimensions of both images
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()
        self.foreground_width = self.foreground.get_width()
        self.foreground_height = self.foreground.get_height()

        # Resize the background to fit the screen width (no stretching vertically)
        self.background = pygame.transform.scale(self.background, (screen_width, self.background_height))
        self.foreground = pygame.transform.scale(self.foreground, (screen_width, self.foreground_height))

    def draw(self, surface):
        # Draw the background at the top
        surface.blit(self.background, (0, 0))

        # Draw the foreground directly below the background
        surface.blit(self.foreground, (0, self.background_height))  # Place it directly below the background