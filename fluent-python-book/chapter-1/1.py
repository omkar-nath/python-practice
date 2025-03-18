colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
styles = ["casual", "formal"]

combination2 = []

for color in colors:
    for size in sizes:
        for style in styles:
            combination2.append((color, size, style))

# Short-hand syntax for above
combinations = [
    (color, size, style) for color in colors for size in sizes for style in styles
]

for combo in combinations:
    print(combo)
for combo in combination2:
    print(combo)
