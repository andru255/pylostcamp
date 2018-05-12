from engine import Scene
from ui_entities import UIButton
import pygame

class SceneHome(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.all_sprites_list = pygame.sprite.Group()

    def did_load(self, window, scenes):
        Scene.did_load(self, window, scenes)
        self.btnPlay = UIButton()
        self.btnConfig = UIButton()
        centerX = window.get_rect().centerx
        # settings
        self.btnPlay.fixture(color=(100, 100, 100), position=(centerX, 100)).foreground(text="Play")
        self.btnConfig.fixture(position=(centerX, 180)).foreground(text="Config")
        dir(self.btnPlay)

    def listen_inputs(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("Move to camp escene")
                self.next = self.scenes['camp']

        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            if self.btnConfig.is_over(mouse_position):
                print("config!")
            if self.btnPlay.is_over(mouse_position):
                print("lets play!")
    
    def update(self):
        self.all_sprites_list.update()
        pass

    def render(self, window):
        Scene.render(self, window)
        window.fill((255, 255, 255))
        self.btnPlay.draw(window)
        self.btnConfig.draw(window)