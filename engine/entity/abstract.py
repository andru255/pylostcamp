import abc

class AbstractEntity(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, fixture, ):
        raise NotImplementedError('needs init method')

    @abc.abstractmethod
    def set_color(self, color):
        raise NotImplementedError('needs set_color method')

    @abc.abstractmethod
    def get_color(self):
        raise NotImplementedError('needs get_position method')

    @abc.abstractmethod
    def set_position(self, position):
        raise NotImplementedError('needs set_position method')

    @abc.abstractmethod
    def get_position(self):
        raise NotImplementedError('needs get_position method')

    @abc.abstractmethod
    def render(self):
        raise NotImplementedError('needs render method')

    @abc.abstractmethod
    def __call__(self):
        raise NotImplementedError('subclass needs __call__ method')