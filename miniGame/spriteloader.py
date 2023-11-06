import pygame
counts = [7,7,7,7,8,8,8,8,9,9,9,9,6,6,6,6,13,13,13,13,6]
shape = (10,15,50,50)
x_spacing = 65
y_spacing = 65

class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except (pygame.error, message):
            print('Unable to load spritesheet image:'+ filename)
        self.i = 0
        self.f = 0
        self.frames = 0.5
        self.images = []
    # Load a specific image from a specific rectangle
    def image_at(self, x_offset, y_offset, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        #rectangle = (shape[0]+x_offset,shape[1]+y_offset,shape[2],shape[3])
        rectangle = (shape[0]+x_offset,shape[1]+y_offset,shape[2],shape[3])
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, offsets, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(offset[0],offset[1], colorkey) for offset in offsets]
    # Load a whole strip of images
    def load_strip(self, row, colorkey = None):
        "Loads a strip of images and returns them as a list"
        image_count = counts[row]
        tups = [(x_spacing*x,y_spacing*row)
                for x in range(image_count)]
        self.images = self.images_at(tups, colorkey)
        return self.images
    def iter(self):
        self.i = 0
        return self
    def next(self,dt):
        if self.i >= len(self.images):
                self.i = 0
        image = self.images[self.i]
        self.f -= dt
        if self.f <= 0:
            self.i += 1
            self.f = self.frames
        return image