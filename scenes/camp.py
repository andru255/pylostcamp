from engine import Scene
from ui_entities import UIButton
import pygame

class SceneCamp(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def did_load(self, window, scene_director):
        Scene.did_load(self, window, scene_director)
        self.scene_director = scene_director
        self.btnGoHome = UIButton()
        self.btnGoHome.fixture(color=(100, 100, 100), position=(20, 20)).foreground(text="HOME")
        super

    def listen_inputs(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.scene_director.go_scene('home')
    
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            if self.btnGoHome.is_over(mouse_position):
                self.scene_director.go_scene('home')

    def update(self):
        pass

    def render(self, window):
        Scene.render(self, window)
        window.fill((255, 0, 255))
        self.btnGoHome.draw(window)