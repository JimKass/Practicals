COLOURS = {"cyan1": "#00ffff", "DarkOrchid": "#9932cc", "DeepPink1": "#ff1493",
           "gold1": "#ffd700", "IndianRed1": "#ff6a6a", "LightSlateBlue": "#8470ff",
           "aquamarine1": "#7fffd4", "BlueViolet": "8a2be2", "coral": "ff7256",
           "DarkTurquoise": "#9400d3"}


def main():
    colour = input("Enter a colour: ")
    while colour != "":
        if colour in COLOURS:
            print(colour, "is", COLOURS[colour])
        else:
            print("Invalid Colour")
        colour = input("Enter a colour: ")


main()
