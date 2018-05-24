import pygame
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, position=(0, 0), color=(0, 0, 0), size=(50, 50)):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.x, self.y = position
        self.color = color
        self.size = size
        self.width, self.height = self.size

        #surfaces
        self.inner_surface = pygame.Surface(self.size).convert_alpha()
        #self.ref_surface = pygame.Surface(self.size).convert_alpha()

        self.velocity_x = 5
        self.velocity_y = 5
        self.angle = 30

        #pygame.draw.circle(self.ref_surface, (128, 128, 128), (25, 25), 30)
        pygame.draw.rect(self.inner_surface, self.color, (0,0,50,50))
    
    def rotate(self):
        new_surface = pygame.transform.rotate(self.inner_surface, self.angle)
        #new_rect = self.inner_surface.get_rect(center=self.rect.center)
        return new_surface

    def update(self, window_width, window_height):
        self.angle += 0.5 * abs(self.velocity_x)
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.contain_into(window_width, window_height)

    def contain_into(self, window_width, window_height):
        # top <-> bottom
        if self.y <= 0:
            self.y = 0
            self.velocity_y = -self.velocity_y
        elif self.y + self.height > window_height:
            self.y = window_height - self.height
            self.velocity_y = -self.velocity_y
        
        # left <-> right
        if self.x <= 0:
            self.x = 0
            self.velocity_x = -self.velocity_x
        elif self.x + self.width > window_width:
            self.x = window_width - self.width
            self.velocity_x = -self.velocity_x
        
    def draw(self, surface):
        inner_surface = self.rotate()
        center_pos_x = self.x - inner_surface.get_width()/2
        center_pos_y = self.y - inner_surface.get_height()/2
        #inner_surface.fill(self.color)
        #surface.blit(self.ref_surface, self.position)
        surface.blit(inner_surface, (center_pos_x, center_pos_y))