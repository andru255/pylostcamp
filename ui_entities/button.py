import pygame

class UIButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def fixture(self, color=(200, 200, 0), width=50, height=50, position=(0,0)):
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.color = color
        return self
    
    def foreground(self, color=(0, 0, 200), text="UIbutton text", font='Arial', size=14):
        self.font = pygame.font.SysFont('Arial', size)
        self.text_surface = self.font.render(text, 1, color)
        return self

    def draw(self):
        new_width = self.text_surface.get_width()
        new_height = self.text_surface.get_height()
        self.image.blit(self.text_surface, [self.width/2 - new_width/2, self.height/2 - new_height/2])
        self.rect = self.image.get_rect()