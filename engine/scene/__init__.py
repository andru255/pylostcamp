from abstract import AbstractEscene

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

class Scene(AbstractEscene):
    uientities = {}
    is_did_load_once = False

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

    @run_once
    def did_load(self, window, scene_director):
        print("Needs to override that method did_load")

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