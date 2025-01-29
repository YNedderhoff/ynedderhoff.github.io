# https://stackoverflow.com/questions/8915113/sort-hex-colors-to-match-rainbow

import colorsys


def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")  # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i + 2], 16) / 255.0 for i in range(0, 5, 2))
    return colorsys.rgb_to_hsv(r, g, b)

# just add invisible links
color_list = ["#BA0200", "#E44734", "#FC4820", "#FC4820", "#FC561F", "#FD6F31", "#FC5205", "#F27F33", "#DBD2BF", "#1CD156", "#056467", "#00ACEE", "#0077b5", "#19445D", "#3097E8", "#08090A", "#23364B", "#FE2C55"]
color_list.sort(key=get_hsv)
print("Invisible links: " + str(color_list))
# output: ['#BA0200', '#E44734', '#FC4820', '#FC4820', '#FC561F', '#FD6F31', '#FC5205', '#F27F33', '#DBD2BF', '#1CD156', '#056467', '#00ACEE', '#0077b5', '#19445D', '#3097E8', '#08090A', '#23364B', '#FE2C55']
