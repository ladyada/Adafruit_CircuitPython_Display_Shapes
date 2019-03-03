import displayio

class RoundRect(displayio.TileGrid):
    def __init__(self, x, y, width, height, r, *, fill=None, outline=None):
        self._bitmap = displayio.Bitmap(width, height, 3)
        self._palette = displayio.Palette(3)
        self._palette.make_transparent(0)

        """
        if fill is not None:
            #for i in range(x0-r, x0+r):   # draw the center line
            #    self._bitmap[i, r] = 2
            # ask our helper to fill in the circle
            self._helper(x0, y0, r, 0xF, 2, fill=True)
            self._palette[2] = fill
        else:
            self._palette.make_transparent(2)
        """

        if outline is not None:
            self._palette[1] = outline
            # draw flat sides
            for w in range(r, width-r):
                self._bitmap[w, 0] = 1
                self._bitmap[w, height-1] = 1
            for h in range(r, height-r):
                self._bitmap[0, h] = 1
                self._bitmap[width-1, h] = 1
            # draw round corners
            self._helper(r, r, r, x_offset=width-2*r-1, y_offset=height-2*r-1, cornerflags=0xF)

        super().__init__(self._bitmap, pixel_shader=self._palette, position=(x, y))

    def _helper(self, x0, y0, r, *, x_offset=0, y_offset=0, cornerflags=0xF, color=1, fill=False):
        f = 1 - r
        ddF_x = 1
        ddF_y = -2 * r
        x = 0
        y = r

        while x < y:
            if f >= 0:
                y -= 1
                ddF_y += 2
                f += ddF_y
            x += 1
            ddF_x += 2
            f += ddF_x
            if cornerflags & 0x8:
                if fill:
                    for w in range(x0-y, x0+y):
                        self._bitmap[w, y0+x] = color
                    for w in range(x0-x, x0+x):
                        self._bitmap[w, y0+y] = color
                else:
                    self._bitmap[x0-y, y0+x+y_offset] = color
                    self._bitmap[x0-x, y0+y+y_offset] = color
            if cornerflags & 0x1:
                if fill:
                    for w in range(x0-y, x0+y):
                        self._bitmap[w, y0-x] = color
                    for w in range(x0-x, x0+x):
                        self._bitmap[w, y0-y] = color
                else:
                    self._bitmap[x0-y, y0-x] = color
                    self._bitmap[x0-x, y0-y] = color
            if cornerflags & 0x4:
                self._bitmap[x0+x+x_offset, y0+y+y_offset] = color
                self._bitmap[x0+y+x_offset, y0+x+y_offset] = color
            if cornerflags & 0x2:
                self._bitmap[x0+x+x_offset, y0-y] = color
                self._bitmap[x0+y+x_offset, y0-x] = color

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
