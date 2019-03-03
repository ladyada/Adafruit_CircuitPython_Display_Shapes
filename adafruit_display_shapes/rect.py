import displayio

class Rect(displayio.TileGrid):
    def __init__(self, x, y, width, height, *, stroke=1, fill=None, outline=None):
        self._bitmap = displayio.Bitmap(width, height, 2)
        self._palette = displayio.Palette(2)

        if outline is not None:
            for w in range(width):
                for line in range(stroke):
                    self._bitmap[w, line] = 1
                    self._bitmap[w, height-1-line] = 1
            for h in range(height):
                for line in range(stroke):
                    self._bitmap[line, h] = 1
                    self._bitmap[width-1-line, h] = 1
            self._palette[1] = outline
        if fill is not None:
            self._palette[0] = fill
        else:
            self._palette.make_transparent(0)
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
