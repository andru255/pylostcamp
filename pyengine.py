import abc

# abstract component like interface
class AbstractComponent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, surface, asset, (x, y)):
        raise NotImplementedError('subclass needs init')
    
    @abc.abstractmethod
    def listen_mouse(self):
        raise NotImplementedError('subclass needs listen_mouse event')

    @abc.abstractmethod
    def listen_keyboard(self):
        raise NotImplementedError('subclass needs listen_key event')

    @abc.abstractmethod
    def update(self, surface):
        raise NotImplementedError('subclass needs init')

#class ComponentManager(object):
#
#    def __init__(self):
#        self.components = []
#        self.instances = []
#        
#
#    def register(self, component):
#        self.components.append(component)
#
#    def init_all(self):
#        self.instances = list(map(lambda x: x(), self.components))
#
#    def run_all(self):
#        for instance in self.instances:
#            instance.update()

#class Game(object):
#    def __init__(self, title, screen_size=(500, 500)):
#        """
#            init the game
#        """
#        self.screen_size = screen_size
#        self.title = title
#    
#    def register(component):
#        self.components = 
#
#    def remove(component):
#        self.components = 
#
#    def loop(self, fps=60):
#        """
#            loop here
#        """