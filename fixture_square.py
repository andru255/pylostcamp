import pygame

class FixtureSquare(object):
    """
        Single class to display a Square
    """
    def __init__(self, width=0, height=0, x=0, y=0, color=(0,255,255)):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.surface = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA,
            32
        )
        print(self.color)
        self.surface.fill(self.color)
        self.surface = self.surface.convert_alpha()
    
    def get_position(self):
        return self.x, self.y

    def blit(self, screen, (x, y)):
        self.x = x
        self.y = y
        screen.blit(self.surface, (x, y))