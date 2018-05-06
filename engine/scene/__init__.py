from abstract import AbstractEscene

class Scene(AbstractEscene):
    uientities = {}

    def __init__(self):
        self.next = self

    def add(self, entity, name):
        self.uientities[name] = entity
        return self

    def remove(self, name):
        del self.uientities[name]
        return self

    def get_all(self):
        return self.uientities
    
    def listen_inputs(self, events, pressed_keys):
        print("Needs to override that method")
    
    def update(self):
        print("Needs to override that method")

    def render(self, window):
        for entity in self.get_all():
            if entity.render(window) != None:
                entity.render(window)
    
    def __call__(self):
        pass

    def __exit__(self):
        pass