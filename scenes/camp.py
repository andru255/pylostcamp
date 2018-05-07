from engine import Scene
import pygame

class SceneCamp(Scene):
    def __init__(self):
        Scene.__init__(self)
    
    def did_load(self, scenes):
        super

    def listen_inputs(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("Move to other escene")
    
    def update(self):
        pass

    def render(self, window):
        super
        window.fill((255, 0, 255))