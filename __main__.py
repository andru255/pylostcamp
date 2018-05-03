from __future__ import print_function, division
from datetime import datetime
import math, pygame, sys, abc
from pygame.locals import *
from pyengine import ComponentManager

# fixtures
from fixture_square import FixtureSquare
#components
from component_player import ComponentPlayer

#init
pygame.init()

##constants
FPS = 30
FPS_CLOCK = pygame.time.Clock()
WINDOW_COLOR = (132, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TITLE = "pyLostCamp"

#only when starts
pygame.display.set_caption(TITLE)
background = pygame.Surface(WINDOW.get_size())
background.fill(WINDOW_COLOR)
background = background.convert()

#setting players
components = [
    ComponentPlayer(WINDOW, FixtureSquare, (WINDOW.get_rect().centerx, WINDOW.get_rect().centery))
]
component_manager = ComponentManager()
for item in components:
    component_manager.register(item)
component_manager.init_all()

# Listen if press quit controls
def is_quit(event_instance, (quit, keydown, escape)):
    if event_instance.type == quit:
        return False
    elif event_instance.type == keydown:
        if event_instance.key == escape:
            return False
    return True

# loop
def loop():
    is_run = True
    while is_run:
        # clean the screen
        WINDOW.blit(background, (0, 0))
        # listen events
        for event in pygame.event.get():
            is_run = is_quit(event, (pygame.QUIT, pygame.KEYDOWN, pygame.K_ESCAPE))
            if event.type == pygame.MOUSEMOTION:
                component_manager.listen_mouse(event, pygame.mouse)
            elif event.type == pygame.K_DOWN or event.type == pygame.KEYUP:
                component_manager.listen_keyboard(event)
        # looping ever
        #instance.update(WINDOW)
        component_manager.run_all(WINDOW)
        ## to RENDER SOME DRAW/GRAPHIC!-> pygame.display.flip()
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)

loop()