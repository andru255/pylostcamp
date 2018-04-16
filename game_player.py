import player

class GamePlayer(object):
    def __init__(self, surface, asset, (x, y)):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.surface = surface
        self.instance = asset(self.width, self.height, self.x, self.y)
    
    def listen_mouse(self, mouse):
        print("position", mouse.get_pos())
        self.x = mouse.get_pos()[0]
        self.y = mouse.get_pos()[1]

    def listen(self, key, (up, down, left, right)):
        # left & right
        if key == left:
            print("up")
            self.x -= 5
        elif key == right:
            print("down!")
            self.x += 5

        # up & down
        if key == up:
            print("up")
            self.y -= 5
        elif key == down:
            print("down!")
            self.y += 5

    def render(self, surface):
        self.instance.blit(surface, (self.x, self.y))