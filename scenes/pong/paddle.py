import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, position=(0, 0), color=(0, 0, 0), size=(50, 150)):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.color = color
        self.size = size
        self.inner_surface = pygame.Surface(self.size).convert()
        self.position_y = position[1]
        #behavior
        self.velocity_y = 0
        self.velocity_y_max = 10
        self.acceleration = 2
        self.angle = 0
        self.friction = 0.85
        # events
        self.up = False
        self.down = False
        self.do_stop = False
    
    #movements
    def stop(self):
        self.do_stop = True
        self.up = False
        self.down = False

    def step_up(self):
        self.do_stop = False
        self.up = True

    def step_down(self):
        self.do_stop = False
        self.down = True

    def update(self, window_height):
        if not self.do_stop:
            if self.up:
                self.velocity_y -= self.acceleration
            elif self.down:
                self.velocity_y += self.acceleration

        if self.velocity_y < -self.velocity_y_max:
            self.velocity_y = -self.velocity_y_max

        if self.velocity_y > self.velocity_y_max:
            self.velocity_y = self.velocity_y_max

        self.velocity_y *= self.friction
        self.position_y += self.velocity_y
        self.position = (self.position[0],  self.position_y)
        self.contain_into(window_height)

    def contain_into(self, height):
        max_y = max(0, self.position[1])
        self.position = (self.position[0],  max_y)

        min_y = min(height - self.size[1], self.position[1])
        self.position = (self.position[0],  min_y)

    def draw(self, surface):
        self.inner_surface.fill(self.color)
        surface.blit(self.inner_surface, self.position)