import pygame

class Debugger(object):
    def __init__(self, window):
        # creating a empty surface
        surface = pygame.Surface(( window.get_width(), window.get_height() - 80), pygame.SRCALPHA, 32)
        self.surface = surface.convert_alpha()
        self.surface.set_alpha(0)

        # defining a position
        self.rect = (0, window.get_height() - 80)

        #screen dimentions
        dimentions = "width: {}, height: {}".format(window.get_width(), window.get_height())
        self.dimentions_logger = Logger(( 10, 10 ), dimentions)

    def draw(self, window, mouse, fps):
        #filling everytime
        self.surface.fill((120, 120, 120, 50))

        #screen dimentions
        self.dimentions_logger.draw(self.surface)

        #screen mouse movement
        x = mouse.get_pos()[0]
        y = mouse.get_pos()[1]
        desc_mouse = "MOUSE: x: {}, y: {}".format(x, y)
        self.mouse_logger = Logger(( 10, 30 ), desc_mouse)
        self.mouse_logger.draw(self.surface)

        #screen fps
        desc_fps = "FPS: {0:.2f}".format(fps)
        self.fps_logger = Logger((10, 50), desc_fps)
        self.fps_logger.draw(self.surface)

        #append to the master window
        window.blit(self.surface, self.rect)

class Logger(pygame.sprite.Sprite):
    def __init__(self, position, text):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.font = pygame.font.SysFont('mono', 14, bold=True)
        self.rect = position
    
    def draw(self, surface):
        self.text_surface = self.font.render(self.text, 1, (0, 0, 0))
        surface.blit(self.text_surface, self.rect)