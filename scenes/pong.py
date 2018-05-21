from engine import Scene
from ui_entities import UIButton
import pygame

class ScenePong(Scene):
    def __init__(self):
        Scene.__init__(self)

    def did_load(self, window, scene_director):
        self.scene_director = scene_director
        self.btnGoHome = UIButton()
        self.btnGoHome.fixture(color=(100, 100, 100), position=(20, 20)).foreground(text="HOME")
        # paddles
        print("center", window.get_rect().centerx)
        self.player = Paddle(position=(20, window.get_rect().centery - 100))
    
    def listen_inputs(self, events, pressed_keys):
        for event in events:
            # go home
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.scene_director.go_scene('home')

            # step up
            if event.key == pygame.K_UP:
                if event.type == pygame.KEYDOWN:
                    self.player.step_up()
                elif event.type == pygame.KEYUP:
                    self.player.stop()
            
            # step down
            if event.key == pygame.K_DOWN:
                if event.type == pygame.KEYDOWN:
                    self.player.step_down()
                elif event.type == pygame.KEYUP:
                    self.player.stop()

        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            if self.btnGoHome.is_over(mouse_position):
                self.scene_director.go_scene('home')
    
    def update(self):
        self.player.update()
    
    def render(self, window):
        Scene.render(self, window)
        window.fill((255, 255, 0))
        self.btnGoHome.draw(window)
        self.player.draw(window)

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

    def update(self):
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

    def draw(self, surface):
        self.inner_surface.fill(self.color)
        surface.blit(self.inner_surface, self.position)