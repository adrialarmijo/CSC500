class ColorSwitch:
    def __init__(self):
        self.primaryColors = {1: 'red', 
                              2: 'blue',
                              4: 'yellow'}

        self.mixedColors = {  3: 'purple',
                              5: 'orange',
                              6: 'green'}

    def combine(self, colorSelected_1, colorSelected_2) -> str:
        if(colorSelected_1 == colorSelected_2):
            return colorSelected_1
        for key_1, color_1 in self.primaryColors.items():
            if colorSelected_1 == color_1:
                for key_2, color_2 in self.primaryColors.items():
                    if colorSelected_2 == color_2:
                        k = key_2 + key_1
                        return self.mixedColors[k]