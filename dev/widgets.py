import lvgl as lv

# TODO: Figure out best way to use constants for this
# Alignment options:
# CENTER = lv.ALIGN.CENTER
# BOTTOM_L = lv.ALIGN.IN_BOTTOM_LEFT
# BOTTOM_M = lv.ALIGN.IN_BOTTOM_MID
# BOTTOM_R = lv.ALIGN.IN_BOTTOM_RIGHT
# TOP_L = lv.ALIGN.IN_TOP_LEFT
# TOP_M = lv.ALIGN.IN_TOP_MID
# TOP_R = lv.ALIGN.IN_TOP_RIGHT
# LEFT_M = lv.ALIGN.IN_LEFT_MID
# RIGHT_M = lv.ALIGN.IN_RIGHT_MID


class Container(lv.cont):

    def __init__(self, parent):
        super().__init__(parent)
        self.set_auto_realign(True)
        self.set_fit(lv.FIT.FLOOD)
        self.set_layout(lv.LAYOUT.PRETTY)


class Label(lv.label):

    def __init__(self, parent, text, width=None):
        super().__init__(parent)
        self.text = text
        # Default to scrolling text if long
        self.set_long_mode(lv.label.LONG.SROLL_CIRC)
        self.set_width(width if width else parent.get_width()-10)
        self.set_text(text)
        self.set_align(lv.label.ALIGN.CENTER)


class Button(lv.btn):

    def __init__(self, parent, x, y, width=None, height=None):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if width and height:
            self.set_size(self.width, self.height)
        self.set_pos(x, y)

    def set_text(self, text):
        self.label = Label(self, text, self.width-10)

    def click(self):
        self.toggle()


class TextArea(lv.ta):

    def __init__(self, parent, x, y, width, height):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.set_size(self.width, self.height)
        self.set_pos(x, y)
        self.set_cursor_type(lv.CURSOR.NONE)

    def set_text_content(self, text):
        self.set_text_align(lv.label.ALIGN.CENTER)
        self.set_text(text)


class Line(lv.line):

    def __init__(self, parent, points=None):
        # Pass in points as a list of tuples in the form:
        #       points = [(x1,y1),(x2,y2),(x3,y3)...]
        super().__init__(parent)
        if points:
            self.set_line_points(points)

    def format(self, points):
        """ Reformats an array
            Takes:
                points = [(x1,y1),(x2,y2),(x3,y3)...]
            Returns:
                points = [{"x": x1, "y": y1},
                            {"x": x2, "y": y2},
                            {"x": x3, "y": y3} ... ]
        """
        return [{"x": x, "y": y} for (x, y) in points]

    def create_style(self, colour=(0x00, 0x3b, 0x75), width=3, rounded=1):
        style_line = lv.style_t()
        lv.style_copy(style_line, lv.style_plain)
        style_line.line.color = lv.color_make(colour[0], colour[1], colour[2])
        style_line.line.width = width
        style_line.line.rounded = rounded
        return style_line

    def set_custom_style(self, style):
        self.set_style(lv.line.STYLE.MAIN, style)

    def set_line_points(self, points):
        formatted = self.format(points)
        self.set_points(formatted, len(formatted))


class Bar(lv.bar):

    def __init__(self, parent, x, y, width=None, height=None):
        # Note that for the 1.8" display, height must be a minimum of 11
        super().__init__(parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height if height >= 11 else 11
        self.set_size(self.width, self.height)
        self.set_pos(x, y)

    def set_animation_time(self, time):
        self.set_anim_time(time)

    def set_value_animation(self, value, anim):
        """ Set anim=True to have an animation and False for static
        """
        self.set_value(value, lv.ANIM.ON if anim else lv.ANIM.OFF)


class Rectangle():

    def __init__(self, parent, tl_x, tl_y, br_x, br_y):
        # tl = Top Left, br = Bottom right
        self.tl_x = tl_x
        self.tl_y = tl_y
        self.br_x = br_x
        self.br_y = br_y
        self.points = self.create_array(tl_x, tl_y, br_x, br_y)
        self.line = Line(parent, self.points)

    def create_array(self, tl_x, tl_y, br_x, br_y):
        return [(tl_x, tl_y),
                (tl_x, br_y),
                (br_x, br_y),
                (br_x, tl_y),
                (tl_x, tl_y)]

    def change_points(self, tl_x, tl_y, br_x, br_y):
        self.line.set_line_points(self.create_array(tl_x, tl_y, br_x, br_y))


class Triangle():

    def __init__(self, parent, l_x, l_y, m_x, m_y, r_x, r_y):
        # l = Left point, m = Middle point, r = Right point
        self.l_x = l_x
        self.l_y = l_y
        self.r_x = r_x
        self.r_y = r_y
        self.m_x = m_x
        self.m_y = m_y
        self.points = self.create_array(l_x, l_y, m_x, m_y, r_x, r_y)
        self.line = Line(parent, self.points)

    def create_array(self, l_x, l_y, m_x, m_y, r_x, r_y):
        return [(l_x, l_y),
                (m_x, m_y),
                (r_x, r_y),
                (l_x, l_y)]

    def change_points(self, l_x, l_y, m_x, m_y, r_x, r_y):
        self.line.set_line_points(
            self.create_array(l_x, l_y, m_x, m_y, r_x, r_y))


class Image(lv.img):

    # To use images, the image must be converted to a binary using the converter
    # at https://littlevgl.com/image-converter
    # Choose "True Color" format and "Binary RGB565"
    # It is also likely that the image will need to be resized. Note the dimensions
    # of the **image file** in PIXELS and use these as width and height

    def __init__(self, parent, filename, x, y, width=None, height=None):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.set_pos(x, y)
        self.filename = filename

        with open(filename, 'rb') as f:
            img_data = f.read()

        img_dsc = lv.img_dsc_t({
            'header': {
                'always_zero': 0,
                'w': self.width,
                'h': self.height,
                'cf': lv.img.CF.TRUE_COLOR
            },
            'data_size': len(img_data),
            'data': img_data
        })

        self.set_src(img_dsc)

    def centralise(self):
        self.align(None, lv.ALIGN.CENTER, 0, 0)
