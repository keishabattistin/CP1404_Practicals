

COLOUR_NAMES = {"DEEP PINK": "#ff1493", "DARK ORCHID": "#9932cc", "CYAN": "#00ffff", "CORAL": "#ff7f50",
               "GOLD": "#ffd700", "LAWN GREEN": "#7cfc00", "ORANGE RED": "ff4500", "RED": "#ff0000", "SLATE BLUE": "#6a5acd", "TOMATO": "#ff6347"}

for colour in COLOUR_NAMES:
    print("{} is {}".format(colour,COLOUR_NAMES[colour]))

colour = input("Enter colour choice: ").upper()

while colour != "":

    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])

    else:
        print("Invalid colour choice")
    colour = input("Enter colour choice: ").upper()