from abstract import AbstractEngine

import pygame
import sys
from scene_director import SceneDirector

from scene import *
from entity import *
from debugger import *

class Engine(AbstractEngine):
    def __init__(self, caption="PyMicroEngine2D", fps=30, size=(800, 600)):
        self.fps = fps
        self.size = size
        self.window = pygame.display.set_mode(self.size)
        self.scene_director = SceneDirector.getInstance() 

        #creating the default background
        background = pygame.Surface(size) 
        background.fill((132, 0, 0))
        self.default_background = background.convert()

        #start pygame
        pygame.init()

        #debugger instance
        self.debug_bar = Debugger(self.window)

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
    
    def add_scene(self, name, scene_self):
        self.scene_director.add_scene(name, scene_self)

    def loop(self):
        clock = pygame.time.Clock()
        current_scene = self.scene_director.show_default_scene()
        while self.scene_director.exists_current_scene():
            self.window.blit(self.default_background, (0, 0))
            current_scene.did_load(self.window, self.scene_director)
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
            # update the current scene only it's different scene
            if self.scene_director.get_current_scene() != current_scene:
                current_scene = self.scene_director.get_current_scene()
            self.debug_bar.draw(self.window, pygame.mouse, clock.get_fps()) 
            pygame.display.flip()
            clock.tick(self.fps)