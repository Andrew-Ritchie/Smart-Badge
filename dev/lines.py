class Line(lv.line):
    
    def __init__(self, parent, x, y, align=lv.ALIGN_CENTER)):
        super().__init__(parent)
        self.x = x
        self.y = y
        line1 = lv.line(parent)
        line1.align(None, lv.ALIGN.CENTER, self.x, self.y)

    def create_style(colour = (0x00, 0x3b, 0x75), width = 3, rounded=1):
        style_line = lv.style_t()
        lv.style_copy(style_line, lv.style_plain)
        style_line.line.color = lv.color_make(colour[0], colour[1], colour[2])
        style_line.line.width = 3
        style_line.line.rounded = 1
        return style_line


    def set_style(style):
         self.set_style(lv.line.STYLE.MAIN, style)

    def set_points(self, points):
        self.set_points(points, len(points))

        
