import pygame

class Debugger(object):
    def __init__(self, window):
        surface = pygame.Surface(( window.get_width(), window.get_height() - 80))
        self.surface = surface.convert()
        self.rect = (0, window.get_height() - 80)

        #screen dimentions
        dimentions = "width: {}, height: {}".format(window.get_width(), window.get_height())
        self.dimentions_logger = Logger(( 0, 0 ), dimentions)

    def draw(self, window, mouse):
        self.surface.fill((120, 120, 120))
        #render screen dimentions
        self.dimentions_logger.draw(self.surface)

        #screen mouse movement
        x = mouse.get_pos()[0]
        y = mouse.get_pos()[1]
        desc_mouse = "MOUSE: x: {}, y: {}, event:".format(x, y)
        self.mouse_logger = Logger(( 0, 20 ), desc_mouse)
        self.mouse_logger.draw(self.surface)

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