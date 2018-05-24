from engine import Scene
from ui_entities import UIButton
import pygame

from paddle import Paddle
from ball import Ball

class ScenePong(Scene):
    def __init__(self):
        Scene.__init__(self)

    def did_load(self, window, scene_director):
        self.window_width, self.window_height = window.get_size()
        self.scene_director = scene_director
        self.btnGoHome = UIButton()
        self.btnGoHome.fixture(color=(100, 100, 100), position=(20, 20)).foreground(text="HOME")
        # paddles
        self.player = Paddle(position=(20, window.get_rect().centery - 100))
        self.player_ia = Paddle(position=(window.get_width() - 70, window.get_rect().centery - 100))

        #ball
        center = (window.get_rect().centerx, window.get_rect().centery)
        self.ball = Ball(position=center, color=(20, 120, 125))

    def listen_inputs(self, event, pressed_keys):
        # go home
        if pressed_keys[pygame.K_BACKSPACE]:
            self.scene_director.go_scene('home')

        if event.type == pygame.KEYDOWN:
            # step up
            if event.key == pygame.K_UP:
                self.player.step_up()
            # step down
            elif event.key == pygame.K_DOWN:
                self.player.step_down()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.player.stop()
            elif event.key == pygame.K_DOWN:
                self.player.stop()

        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            if self.btnGoHome.is_over(mouse_position):
                self.scene_director.go_scene('home')
    
    def update(self):
        self.player.update(self.window_height)
        self.ball.update(self.window_width, self.window_height)
    
    def render(self, window):
        Scene.render(self, window)
        window.fill((255, 255, 0))
        self.player.draw(window)
        self.player_ia.draw(window)
        self.ball.draw(window)
        self.btnGoHome.draw(window)