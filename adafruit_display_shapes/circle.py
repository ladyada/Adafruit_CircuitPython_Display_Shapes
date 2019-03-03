import displayio
from adafruit_display_shapes.roundrect import RoundRect

class Circle(RoundRect):
    def __init__(self, x0, y0, r, *, fill=None, outline=None):
        super().__init__(x0-r, y0-r, 2*r+1, 2*r+1, r, fill=fill, outline=outline)
