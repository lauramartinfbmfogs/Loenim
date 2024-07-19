def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    h_len = len(hex_color)
    return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))

colors = ["#FF0000", "#00FF00", "#0000FF"]  # An array of hex colors
for i, color in enumerate(colors):
    rgb_color = hex_to_rgb(color)
    print(f"Color {i}: {rgb_color}")  # Output: (255, 0, 0), etc.
