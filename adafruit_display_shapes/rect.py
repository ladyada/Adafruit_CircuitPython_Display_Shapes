import displayio

class Rect(displayio.TileGrid):
    def __init__(self, x, y, width, height, *, fill=None, outline=None):
        self._bitmap = displayio.Bitmap(width, height, 2)
        if outline is not None:
            for w in range(width):
                self._bitmap[w, 0] = 1
                self._bitmap[w, height-1] = 1
            for h in range(height):
                self._bitmap[0, h] = 1
                self._bitmap[width-1, h] = 1

        self._palette = displayio.Palette(2)
        self._palette[0] = fill
        self._palette[1] = outline
        super().__init__(self._bitmap, pixel_shader=self._palette, position=(x, y))


    @property
    def x(self):
        return self.position[0]

    @x.setter
    def x(self, x):
        self.position = (x, self.position[1])

    @property
    def y(self):
        return self.position[1]

    @x.setter
    def y(self, y):
        self.position = (self.position[0], y)
