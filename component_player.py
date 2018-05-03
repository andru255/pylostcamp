from pyengine import AbstractComponent

class ComponentPlayer(AbstractComponent):
    def __init__(self, surface, asset, (x, y)):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.surface = surface
        self.instance = asset(self.width, self.height, self.x, self.y)
    
    def listen_mouse(self, event, mouse):
        print("position", mouse.get_pos())
        #self.x = mouse.get_pos()[0]
        #self.y = mouse.get_pos()[1]

    def listen_keyboard(self, event):
        print("keyboard...")
        # left & right
        #if key == left:
        #    print("up")
        #    self.x -= 5
        #elif key == right:
        #    print("down!")
        #    self.x += 5

        ## up & down
        #if key == up:
        #    print("up")
        #    self.y -= 5
        #elif key == down:
        #    print("down!")
        #    self.y += 5

    def update(self, surface):
        self.instance.blit(surface, (self.x, self.y))
    
    def __call__(self):
        return self