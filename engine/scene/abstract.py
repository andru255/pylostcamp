import abc

class AbstractEscene(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, surface):
        raise NotImplementedError('needs init method')

    @abc.abstractmethod
    def add(self, entity, name):
        raise NotImplementedError('needs add method')

    @abc.abstractmethod
    def remove(self, name):
        raise NotImplementedError('needs remove method')

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError('needs get_all method')

    @abc.abstractmethod
    def __exit__(self):
        raise NotImplementedError('needs __exit__ method')

    @abc.abstractmethod
    def __call__(self):
        raise NotImplementedError('subclass needs __call__ method')