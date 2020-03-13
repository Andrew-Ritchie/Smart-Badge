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


class Container():

    def __init__(self, parent):
        self.lv_obj = lv.cont(parent)
        self._set_custom_style()
        self.lv_obj.set_auto_realign(True)
        self.lv_obj.set_fit(lv.FIT.FLOOD)
        self.lv_obj.set_layout(lv.LAYOUT.PRETTY)
        self.width = self.lv_obj.get_width()
        self.half_width = self.width//2 - 13
        self.third_width = self.width//3 - 10

    def half(self):
        return self.half_width

    def third(self):
        return self.third_width

    def set_center(self):
        self.lv_obj.set_layout(lv.LAYOUT.CENTER)

    def get_width(self):
        return self.lv_obj.get_width()

    def _set_custom_style(self):
        style = lv.style_t()
        lv.style_copy(style, self.lv_obj.get_style(lv.cont.STYLE.MAIN))
        style.body.main_color = lv.color_make(0xC0, 0xC0, 0xC0)
        style.body.grad_color = lv.color_make(0x4F, 0x52, 0x57)
        style.body.radius = 0
        self.lv_obj.set_style(lv.cont.STYLE.MAIN, style)


class Label():

    def __init__(self, parent, text, width=None, font_size=None):
        self.lv_obj = lv.label(parent)
        if font_size:
            self._set_font_size(font_size)
        self.text = text
        # Default to scrolling text if long
        self.lv_obj.set_long_mode(lv.label.LONG.SROLL_CIRC)
        self.lv_obj.set_width(width if width else parent.get_width()-10)
        self.lv_obj.set_text(self.text)
        self.lv_obj.set_align(lv.label.ALIGN.CENTER)

    def update_text(self, text):
        self.lv_obj.set_text(text)

    def _set_font_size(self, font_size):
        style = lv.style_t()
        lv.style_copy(style, self.lv_obj.get_style(lv.label.STYLE.MAIN))
        if font_size == 28:
            style.text.font = lv.font_roboto_28
        self.lv_obj.set_style(lv.label.STYLE.MAIN, style)


class Button():

    def __init__(self, parent, text=None, font_size=None, x=0, y=0, width=None, height=None, app=None, subject=None):
        self.lv_obj = lv.btn(parent)
        self.parent = parent
        self.x = x
        self.y = y
        self.width = width if width else parent.get_width()-10
        self.height = height if height else 25
        self.lv_obj.set_size(self.width, self.height)
        self.lv_obj.set_pos(x, y)
        self.label = None
        if subject:
            self.subject = subject

        if text:
            self.set_text(text, font_size)
        if app:
            self.app_name = app

    def set_text(self, text, font_size):
        if self.label:
            self.label.lv_obj.set_text(text)
        else:
            self.label = Label(self.lv_obj, text, self.width-10, font_size)

    def click(self):
        self.toggle()


class TextArea():

    def __init__(self, parent, x, y, width, height):
        self.lv_obj = lv.ta(parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lv_obj.set_size(self.width, self.height)
        self.lv_obj.set_pos(x, y)
        self.lv_obj.set_cursor_type(lv.CURSOR.NONE)

    def set_text_content(self, text):
        self.lv_obj.set_text_align(lv.label.ALIGN.CENTER)
        self.lv_obj.set_text(text)


class Line():

    def __init__(self, parent, points=None):
        # Pass in points as a list of tuples in the form:
        #       points = [(x1,y1),(x2,y2),(x3,y3)...]
        self.lv_obj = lv.line(parent)
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
        self.lv_obj.set_style(lv.line.STYLE.MAIN, style)

    def set_line_points(self, points):
        formatted = self.format(points)
        self.lv_obj.set_points(formatted, len(formatted))


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
        self.lv_obj = self.line.lv_obj

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


class Circle(lv.obj):

    def __init__(self, parent, width, height, x, y):
        super().__init__(parent)
        self.set_size(width, height)
        self.set_pos(x, y)

        self.circle_style = lv.style_t()
        lv.style_copy(self.circle_style, lv.style_plain)
        self.circle_style.body.radius = lv.RADIUS.CIRCLE
        self.set_style(self.circle_style)

    def move(self, x, y):
        self.set_pos(x, y)

class List():

    def __init__(self,parent):
        self.lv_obj = lv.list(parent)
        self.lv_obj.set_size(160,200)
        self.lv_obj.align(None, lv.ALIGN.CENTER, 0, 0)
        list_btn = list1.add_btn(lv.SYMBOL.FILE, "New")
        self.list_btn.set_event_cb(event_handler)
