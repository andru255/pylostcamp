import pygame
import abc

# abstract component like interface
class AbstractComponent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, surface, asset, (x, y)):
        raise NotImplementedError('subclass needs init method')
    
    @abc.abstractmethod
    def listen_mouse(self, event, mouse):
        raise NotImplementedError('subclass needs listen_mouse method')

    @abc.abstractmethod
    def listen_keyboard(self, event):
        raise NotImplementedError('subclass needs listen_keyboard method')

    @abc.abstractmethod
    def update(self, surface):
        raise NotImplementedError('subclass needs update method')
    
    @abc.abstractmethod
    def __call__(self):
        raise NotImplementedError('subclass needs __call__ method')

# component manager
class ComponentManager(object):
    def __init__(self):
        self.components = []
        self.instances = []
        
    def register(self, component):
        self.components.append(component)

    def init_all(self):
        self.instances = list(map(lambda x: x(), self.components))

    def listen_mouse(self, event, mouse):
        for instance in self.instances:
            instance.listen_mouse(event, mouse)

    def listen_keyboard(self, event):
        for instance in self.instances:
            instance.listen_keyboard(event)

    def run_all(self, window):
        for instance in self.instances:
            instance.update(window)