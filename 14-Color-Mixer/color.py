print("COLOR MIXER 🎨")
color_mixes = {
    ("red", "blue"): "purple",
    ("red", "green"): "brown",
    ("red", "yellow"): "orange",
    ("red", "white"): "light red",
    ("blue", "green"): "cyan",
    ("blue", "yellow"): "greenish",
    ("blue", "white"): "light blue",
    ("green", "yellow"): "lime",
    ("green", "white"): "light green",
    ("yellow", "white"): "light yellow"
}

while True:
    color1 = input("Enter first color (red/blue/green/yellow/white): ").lower()
    color2 = input("Enter second color (red/blue/green/yellow/white): ").lower()

    if color1 == color2:
        print("You have entered both same color: " + color1)
    else:
        mix_result = color_mixes.get((color1, color2)) or color_mixes.get((color2, color1))
        if mix_result:
            print(f"When you mix {color1} and {color2}, you get: {mix_result}")
        else:
            print("Sorry!!! I don't know what color that makes.")

    mix = input("Mix more colors? (y/n): ").lower()
    if mix == 'n':
        print("GoodByeeee")
        break
