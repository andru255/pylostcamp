import pygame

class Debugger(pygame.sprite.Sprite):
    def __init__(self, width=100, height=100):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.font = pygame.font.SysFont('mono', 14, bold=True)
        self.text_surface = self.font.render(text, 1, color)
    
    def render(self, window):
        self.image.blit()