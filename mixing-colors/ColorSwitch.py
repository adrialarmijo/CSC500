class ColorSwitch:
    def color(self, colorSelected):
        default = "Incorrect color entry"
        return getattr(self, str(colorSelected), lambda: default)()
    
    def red(self):
        return "red"
    
    def blue(self):
        return "blue"
    
    def yellow(self):
        return "yellow"
    
    def purple(self):
        return "purple"
    
    def orange(self):
        return "orange"
    
    def green(self):
        return "green"

    def combine(self, colorSelected_1, colorSelect_2):
        if ((colorSelected_1 or colorSelect_2) is self.ColorSwitch.red()):
            if((colorSelected_1 or colorSelect_2) == ColorSwitch.blue()):
                return ColorSwitch.purple()
            if((colorSelected_1 or colorSelect_2) == ColorSwitch.yellow()):
                return ColorSwitch.orange()
        elif((colorSelected_1 or colorSelect_2) == ColorSwitch.blue()):
            if((colorSelected_1 or colorSelect_2) == ColorSwitch.yellow()):
                return ColorSwitch.green()
        else:
            return ColorSwitch.color()

        