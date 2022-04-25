# https://stackoverflow.com/questions/8915113/sort-hex-colors-to-match-rainbow

import colorsys


def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")  # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i + 2], 16) / 255.0 for i in range(0, 5, 2))
    return colorsys.rgb_to_hsv(r, g, b)

color_list = ["#8BC35A", "#00ACEE", "#000000", "#0077b5", "#FD6F31", "#FC561F", "#23364B", "#DBD2BF", "#FC4820", "#0077b5", "#F27F33", "#D7D0BF", "#1CD156", "#BA0200", "#3097E8", "#056467", "#E44734", "#08090A", "#FC6D25", "#19445D", "#FC5205"]
color_list.sort(key=get_hsv)
print(color_list)
# output: ['#000000', '#BA0200', '#E44734', '#FC4820', '#FC561F', '#FD6F31', '#FC5205', '#FC6D25', '#F27F33', '#DBD2BF', '#D7D0BF', '#8BC35A', '#1CD156', '#056467', '#00ACEE', '#0077b5', '#0077b5', '#19445D', '#3097E8', '#08090A', '#23364B']
