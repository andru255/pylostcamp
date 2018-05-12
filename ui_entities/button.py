import pygame

class UIButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def fixture(self, color=(200, 200, 0), width=50, height=50, position=(0,0)):
        self.width = width
        self.height = height
        self.inner_surface = pygame.Surface((width, height)).convert()
        self.position = position
        self.color = color
        return self
    
    def foreground(self, color=(0, 0, 200), text="UIbutton text", font='Arial', size=14):
        self.text = text
        self.fore_color = color
        self.font = pygame.font.SysFont('Arial', size)
        return self

    def is_over(self, point):
        point_x, point_y = point
        x, y = self.position
        w, h = self.inner_surface.get_size()
        x -= self.width/2 - w/2
        y -= self.height/2 - h/2

        in_x = point_x >= x and point_x < x + w
        in_y = point_y >= y and point_y < y + h
        return in_x and in_y

    def get_centered_position(self):
        new_width = self.text_surface.get_width()
        new_height = self.text_surface.get_height()
        return (self.width / 2 - new_width/2, self.height/2 - new_height/2)

    def draw(self, surface):
        self.inner_surface.fill(self.color)
        self.text_surface = self.font.render(self.text, 1, self.fore_color)
        self.inner_surface.blit(self.text_surface, self.get_centered_position())
        surface.blit(self.inner_surface, self.position)