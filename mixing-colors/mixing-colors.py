import ColorSwitch

print("Welcome to Color Combiner!")
print("We can combine the following colors: red, blue, yellow")

colorInputList = [color for color in input("Please enter two colors from above: ").split()]
color = ColorSwitch

colorCombination = color.ColorSwitch.combine(ColorSwitch, colorInputList[0], colorInputList[1])

print("Your combined color is: " + str(colorCombination))