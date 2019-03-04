# The MIT License (MIT)
#
# Copyright (c) 2019 Limor Fried for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`rect`
================================================================================

Various common shapes for use with displayio - Rectangle shape!


* Author(s): Limor Fried

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import displayio

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Display_Shapes.git"


class Rect(displayio.TileGrid):
    """A rectangle, top left corner is (x, y) and size of width, height.
    Stroke is used for the outline, and will not change outer bound size set
    by width and height. Fill can be a hex value for the color or None for
    transparent. Outline can be a hex value for the color or None for no
    outline."""
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
        """The x coordinate of the position"""
        return self.position[0]

    @x.setter
    def x(self, x):
        self.position = (x, self.position[1])

    @property
    def y(self):
        """The y coordinate of the position"""
        return self.position[1]

    @x.setter
    def y(self, y):
        self.position = (self.position[0], y)
