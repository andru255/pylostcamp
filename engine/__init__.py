from abstract import AbstractEngine

import pygame
import sys
from scene import *
from entity import *

class Engine(AbstractEngine):
    def __init__(self, caption="PyMicroEngine2D", fps=30, size=(800, 600)):
        self.fps = fps
        self.size = size
        self.scenes = {}
        self.window = pygame.display.set_mode(self.size)

        #creating the default background
        background = pygame.Surface(size) 
        background.fill((132, 0, 0))
        self.default_background = background.convert()

        #start pygame
        pygame.init()

    def add_scene(self, name, scene_self):
        self.scenes[name] = scene_self

    def show_escene(self, name):
        pass
    
    def quit_attempt(self, event, pressed_keys):
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or \
                          pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_ESCAPE:
                return True
            elif event.key == pygame.K_F4 and alt_pressed:
                return True

    def loop(self):
        clock = pygame.time.Clock()
        if len(self.scenes) > 0:
            scene_name = list(self.scenes.keys())[0]
            current_scene = self.scenes[scene_name]
        else:
            sys.exit("Needs an scene. Ex: loop({'my_scene': my_scene})")
    
        self.window.blit(self.default_background, (0, 0))
        while current_scene != None:
            pressed_keys = pygame.key.get_pressed()
            filtered_events = []
            #event filtering
            for event in pygame.event.get():
                if self.quit_attempt(event, pressed_keys):
                    pygame.quit()
                    sys.exit()
                else:
                    filtered_events.append(event)
            current_scene.listen_inputs(filtered_events, pressed_keys)
            current_scene.update()
            current_scene.render(self.window)
            current_scene = current_scene.next
            pygame.display.flip()
            clock.tick(self.fps)