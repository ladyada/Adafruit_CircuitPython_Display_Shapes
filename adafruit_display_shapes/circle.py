import displayio

class Circle(displayio.TileGrid):
    def __init__(self, x0, y0, r, *, fill=None, outline=None):
        self._bitmap = displayio.Bitmap(r*2+1, r*2+1, 3)
        self._palette = displayio.Palette(3)
        self._palette.make_transparent(0)

        # set position to top left corner
        position = (x0-r, y0-r)
        # and now set that position to be (0,0)
        x0 = y0 = r

        if fill is not None:
            for i in range(x0-r, x0+r):   # draw the center line
                self._bitmap[i, r] = 2
            # ask our helper to fill in the circle
            self._helper(x0, y0, r, 0xF, 2, fill=True)
            self._palette[2] = fill
        else:
            self._palette.make_transparent(2)

        if outline is not None:
            self._palette[1] = outline
            # draw outline
            self._bitmap[x0, y0+r] = 1
            self._bitmap[x0, y0-r] = 1
            self._bitmap[x0+r, y0] = 1
            self._bitmap[x0-r, y0] = 1

        self._helper(x0, y0, r, 0xF, 1)





        super().__init__(self._bitmap, pixel_shader=self._palette, position=position)

    def _helper(self, x0, y0, r, cornerflags, color, *, fill=False):
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
                    self._bitmap[x0-y, y0+x] = color
                    self._bitmap[x0-x, y0+y] = color
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
                self._bitmap[x0+x, y0+y] = color
                self._bitmap[x0+y, y0+x] = color
            if cornerflags & 0x2:
                self._bitmap[x0+x, y0-y] = color
                self._bitmap[x0+y, y0-x] = color

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
