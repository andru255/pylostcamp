import abstract

class Entity(object):
    def __init__(self, fixture, position, color):
        self.fixture = fixture
        self.type = type
        self.position = position
        self.color = color
    
    def render(self):
        return self

    def update_color(self, color):
        self.color = color
        return self

    def get_color(self):
        return self.color
    
    def update_position(self, position):
        self.position = position
        return self

    def get_position(self):
        return self.position