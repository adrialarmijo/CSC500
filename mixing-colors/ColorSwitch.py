class ColorSwitch:
    def __init__(self):
        self.primaryColors = {'red'     : 1, 
                              'blue'    : 2,
                              'yellow'  : 4}

        self.mixedColors = {  3 : 'purple',
                              5 : 'orange',
                              6 : 'green'}

    def combine(self, colorSelected_1, colorSelected_2) -> str:
        if(colorSelected_1 == colorSelected_2):
            return colorSelected_1
        k = self.primaryColors[colorSelected_1] + self.primaryColors[colorSelected_2]
        return self.mixedColors[k]