from __future__ import print_function, division
from datetime import datetime
import math, pygame, sys, abc
from pygame.locals import *

#importing the microengine
from engine import Engine

# importing scenes
from scenes import *

# constants
FPS = 60
FPS_CLOCK = pygame.time.Clock()
WINDOW_COLOR = (132, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TITLE = "pyLostCamp"

# config main gameengine
main = Engine(TITLE, FPS, (WINDOW_WIDTH, WINDOW_HEIGHT))
main.add_scene('home', SceneHome())
main.add_scene('pong', ScenePong())
main.add_scene('camp', SceneCamp())
main.loop()