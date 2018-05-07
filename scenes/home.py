from engine import Scene
from ui_entities import UIButton
import pygame

class SceneHome(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.all_sprites_list = pygame.sprite.Group()
        button = UIButton()
        button.fixture().foreground().draw()
        self.all_sprites_list.add(button)

    def did_load(self, scenes):
        Scene.did_load(self, scenes)

    def listen_inputs(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("Move to camp escene")
                self.next = self.scenes['camp']
    
    def update(self):
        self.all_sprites_list.update()
        pass

    def render(self, window):
        Scene.render(self, window)
        window.fill((255, 255, 255))
        self.all_sprites_list.draw(window)