from engine import Scene
from ui_entities import UIButton
import pygame

class SceneHome(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.all_sprites_list = pygame.sprite.Group()

    def did_load(self, window, scene_director):
        self.scene_director = scene_director
        self.btnGoPong = UIButton()
        self.btnGoCamp = UIButton()
        centerX = window.get_rect().centerx
        # settings
        self.btnGoPong.fixture(color=(100, 100, 100), position=(centerX, 100)).foreground(text="Go Pong")
        self.btnGoCamp.fixture(position=(centerX, 180)).foreground(text="Go Camp")
        print("renice!")

    def listen_inputs(self, event, pressed_keys):
        if pressed_keys[pygame.K_1]:
            print("Move to pong escene")
            self.scene_director.go_scene('pong')
        if pressed_keys[pygame.K_2]:
            print("Move to camp escene")
            self.scene_director.go_scene('camp')

        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            if self.btnGoPong.is_over(mouse_position):
                self.scene_director.go_scene('pong')
            if self.btnGoCamp.is_over(mouse_position):
                self.scene_director.go_scene('camp')

    def update(self):
        pass

    def render(self, window):
        Scene.render(self, window)
        window.fill((255, 255, 255))
        self.btnGoPong.draw(window)
        self.btnGoCamp.draw(window)