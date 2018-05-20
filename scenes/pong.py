from engine import Scene
from ui_entities import UIButton
import pygame

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

class ScenePong(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.cool = 0

    @run_once
    def did_load(self, window, scene_director):
        Scene.did_load(self, window, scene_director)
        self.scene_director = scene_director
        self.btnGoHome = UIButton()
        self.btnGoHome.fixture(color=(100, 100, 100), position=(20, 20)).foreground(text="HOME")
        # paddles
        self.player = Paddle(position=(20, 80))
        print("queeee")
    
    def listen_inputs(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.scene_director.go_scene('home')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.cool += 1
                self.player.to_up()
                print(self.cool)

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
        print("SCENE_COOL", self.cool)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, position=(0, 0), color=(0, 0, 0), size=(50, 150)):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.color = color
        self.size = size
        self.inner_surface = pygame.Surface(self.size).convert()
        self.go_up = False
        self.cool = 0
    
    #movements
    def to_up(self):
        self.cool += 1
        self.go_up = True

    def update(self):
        print(self.position)
        if self.go_up:
            self.position = (self.position[0], self.position[1] + 1)

    def draw(self, surface):
        self.inner_surface.fill(self.color)
        surface.blit(self.inner_surface, self.position)
        print("cool", self.cool)