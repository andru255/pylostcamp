import abc

class AbstractEngine(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, fps, size):
        raise NotImplementedError('needs init method')

    @abc.abstractmethod
    def add_scene(self, name, scene_self):
        raise NotImplementedError('needs add method')

    @abc.abstractmethod
    def show_escene(self, name):
        raise NotImplementedError('needs remove method')