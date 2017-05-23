# Copyright 2017 Bernhard Walter
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from colormath.color_objects import sRGBColor, LCHabColor
from colormath.color_conversions import convert_color
from .interpolate import spline


# Source: https://www.w3schools.com/cssref/css_colors.asp

css3Colors = {
    "AliceBlue":         (240, 248, 255), "AntiqueWhite":         (250, 235, 215), "Aqua":            (  0, 255, 255),        # noqa E501,E231,E201
    "Aquamarine":        (127, 255, 212), "Azure":                (240, 255, 255), "Beige":           (245, 245, 220),        # noqa E501,E231,E201
    "Bisque":            (255, 228, 196), "Black":                (  0,   0,   0), "BlanchedAlmond":  (255, 235, 205),        # noqa E501,E231,E201
    "Blue":              (  0,   0, 255), "BlueViolet":           (138,  43, 226), "Brown":           (165,  42,  42),        # noqa E501,E231,E201
    "BurlyWood":         (222, 184, 135), "CadetBlue":            ( 95, 158, 160), "Chartreuse":      (127, 255,   0),        # noqa E501,E231,E201
    "Chocolate":         (210, 105,  30), "Coral":                (255, 127,  80), "CornflowerBlue":  (100, 149, 237),        # noqa E501,E231,E201
    "Cornsilk":          (255, 248, 220), "Crimson":              (220,  20,  60), "Cyan":            (  0, 255, 255),        # noqa E501,E231,E201
    "DarkBlue":          (  0,   0, 139), "DarkCyan":             (  0, 139, 139), "DarkGoldenRod":   (184, 134,  11),        # noqa E501,E231,E201
    "DarkGray":          (169, 169, 169), "DarkGreen":            (  0, 100,   0), "DarkGrey":        (169, 169, 169),        # noqa E501,E231,E201
    "DarkKhaki":         (189, 183, 107), "DarkMagenta":          (139,   0, 139), "DarkOliveGreen":  ( 85, 107,  47),        # noqa E501,E231,E201
    "DarkOrange":        (255, 140,   0), "DarkOrchid":           (153,  50, 204), "DarkRed":         (139,   0,   0),        # noqa E501,E231,E201
    "DarkSalmon":        (233, 150, 122), "DarkSeaGreen":         (143, 188, 143), "DarkSlateBlue":   ( 72,  61, 139),        # noqa E501,E231,E201
    "DarkSlateGray":     ( 47,  79,  79), "DarkSlateGrey":        ( 47,  79,  79), "DarkTurquoise":   (  0, 206, 209),        # noqa E501,E231,E201
    "DarkViolet":        (148,   0, 211), "DeepPink":             (255,  20, 147), "DeepSkyBlue":     (  0, 191, 255),        # noqa E501,E231,E201
    "DimGray":           (105, 105, 105), "DimGrey":              (105, 105, 105), "DodgerBlue":      ( 30, 144, 255),        # noqa E501,E231,E201
    "FireBrick":         (178,  34,  34), "FloralWhite":          (255, 250, 240), "ForestGreen":     ( 34, 139,  34),        # noqa E501,E231,E201
    "Fuchsia":           (255,   0, 255), "Gainsboro":            (220, 220, 220), "GhostWhite":      (248, 248, 255),        # noqa E501,E231,E201
    "Gold":              (255, 215,   0), "GoldenRod":            (218, 165,  32), "Gray":            (128, 128, 128),        # noqa E501,E231,E201
    "Green":             (  0, 128,   0), "GreenYellow":          (173, 255,  47), "Grey":            (128, 128, 128),        # noqa E501,E231,E201
    "HoneyDew":          (240, 255, 240), "HotPink":              (255, 105, 180), "IndianRed":       (205,  92,  92),        # noqa E501,E231,E201
    "Indigo":            ( 75,   0, 130), "Ivory":                (255, 255, 240), "Khaki":           (240, 230, 140),        # noqa E501,E231,E201
    "Lavender":          (230, 230, 250), "LavenderBlush":        (255, 240, 245), "LawnGreen":       (124, 252,   0),        # noqa E501,E231,E201
    "LemonChiffon":      (255, 250, 205), "LightBlue":            (173, 216, 230), "LightCoral":      (240, 128, 128),        # noqa E501,E231,E201
    "LightCyan":         (224, 255, 255), "LightGoldenRodYellow": (250, 250, 210), "LightGray":       (211, 211, 211),        # noqa E501,E231,E201
    "LightGreen":        (144, 238, 144), "LightGrey":            (211, 211, 211), "LightPink":       (255, 182, 193),        # noqa E501,E231,E201
    "LightSalmon":       (255, 160, 122), "LightSeaGreen":        ( 32, 178, 170), "LightSkyBlue":    (135, 206, 250),        # noqa E501,E231,E201
    "LightSlateGray":    (119, 136, 153), "LightSlateGrey":       (119, 136, 153), "LightSteelBlue":  (176, 196, 222),        # noqa E501,E231,E201
    "LightYellow":       (255, 255, 224), "Lime":                 (  0, 255,   0), "LimeGreen":       ( 50, 205,  50),        # noqa E501,E231,E201
    "Linen":             (250, 240, 230), "Magenta":              (255,   0, 255), "Maroon":          (128,   0,   0),        # noqa E501,E231,E201
    "MediumAquaMarine":  (102, 205, 170), "MediumBlue":           (  0,   0, 205), "MediumOrchid":    (186,  85, 211),        # noqa E501,E231,E201
    "MediumPurple":      (147, 112, 219), "MediumSeaGreen":       ( 60, 179, 113), "MediumSlateBlue": (123, 104, 238),        # noqa E501,E231,E201
    "MediumSpringGreen": (  0, 250, 154), "MediumTurquoise":      ( 72, 209, 204), "MediumVioletRed": (199,  21, 133),        # noqa E501,E231,E201
    "MidnightBlue":      ( 25,  25, 112), "MintCream":            (245, 255, 250), "MistyRose":       (255, 228, 225),        # noqa E501,E231,E201
    "Moccasin":          (255, 228, 181), "NavajoWhite":          (255, 222, 173), "Navy":            (  0,   0, 128),        # noqa E501,E231,E201
    "OldLace":           (253, 245, 230), "Olive":                (128, 128,   0), "OliveDrab":       (107, 142,  35),        # noqa E501,E231,E201
    "Orange":            (255, 165,   0), "OrangeRed":            (255,  69,   0), "Orchid":          (218, 112, 214),        # noqa E501,E231,E201
    "PaleGoldenRod":     (238, 232, 170), "PaleGreen":            (152, 251, 152), "PaleTurquoise":   (175, 238, 238),        # noqa E501,E231,E201
    "PaleVioletRed":     (219, 112, 147), "PapayaWhip":           (255, 239, 213), "PeachPuff":       (255, 218, 185),        # noqa E501,E231,E201
    "Peru":              (205, 133,  63), "Pink":                 (255, 192, 203), "Plum":            (221, 160, 221),        # noqa E501,E231,E201
    "PowderBlue":        (176, 224, 230), "Purple":               (128,   0, 128), "RebeccaPurple":   (102,  51, 153),        # noqa E501,E231,E201
    "Red":               (255,   0,   0), "RosyBrown":            (188, 143, 143), "RoyalBlue":       ( 65, 105, 225),        # noqa E501,E231,E201
    "SaddleBrown":       (139,  69,  19), "Salmon":               (250, 128, 114), "SandyBrown":      (244, 164,  96),        # noqa E501,E231,E201
    "SeaGreen":          ( 46, 139,  87), "SeaShell":             (255, 245, 238), "Sienna":          (160,  82,  45),        # noqa E501,E231,E201
    "Silver":            (192, 192, 192), "SkyBlue":              (135, 206, 235), "SlateBlue":       (106,  90, 205),        # noqa E501,E231,E201
    "SlateGray":         (112, 128, 144), "SlateGrey":            (112, 128, 144), "Snow":            (255, 250, 250),        # noqa E501,E231,E201
    "SpringGreen":       (  0, 255, 127), "SteelBlue":            ( 70, 130, 180), "Tan":             (210, 180, 140),        # noqa E501,E231,E201
    "Teal":              (  0, 128, 128), "Thistle":              (216, 191, 216), "Tomato":          (255,  99,  71),        # noqa E501,E231,E201
    "Turquoise":         ( 64, 224, 208), "Violet":               (238, 130, 238), "Wheat":           (245, 222, 179),        # noqa E501,E231,E201
    "White":             (255, 255, 255), "WhiteSmoke":           (245, 245, 245), "Yellow":          (255, 255,   0),        # noqa E501,E231,E201
    "YellowGreen":       (154, 205,  50)
}


def rgb2hcl(r, g, b):
    rgb = sRGBColor(r, g, b, True)
    return list(reversed(convert_color(rgb, LCHabColor, sRGBColor).get_value_tuple()))


def hcl2rgb(h, c, l):
    lch = LCHabColor(l, c, h)
    return convert_color(lch, sRGBColor).get_upscaled_value_tuple()


def rgb2web(rgbs):
    def conv(color):
        return "rgb(%d,%d,%d)" % color

    if isinstance(rgbs[0], (list, tuple)):
        return [conv(rgb) for rgb in rgbs]
    else:
        return conv(rgbs)


def rgba2web(rgbs):
    def conv(color):
        return "rgba(%d,%d,%d,%f)" % color

    if isinstance(rgbs[0], (list, tuple)):
        return [conv(rgb) for rgb in rgbs]
    else:
        return conv(rgbs)


def rgb2str(rgbs):
    def conv(color):
        return "%d,%d,%d" % color

    if isinstance(rgbs[0], (list, tuple)):
        return [conv(rgb) for rgb in rgbs]
    else:
        return conv(rgbs)


def web2rgba(colors):

    def conv(color, ignoreAlpha=False):
        if color[0] == "#":
            if len(color) == 4:
                rgba = (int(color[1:2] * 2, 16),
                        int(color[2:3] * 2, 16),
                        int(color[3:4] * 2, 16), 1.0)
            else:
                rgba = (int(color[1:3], 16),
                        int(color[3:5], 16),
                        int(color[5:7], 16), 1.0)

        elif color.startswith("rgba"):
            r, g, b, a = color.replace(" ", "")[5:-1].split(",")
            rgba = (int(r), int(g), int(b), float(a))

        elif color.startswith("rgb"):
            r, g, b = color.replace(" ", "")[4:-1].split(",")
            rgba = (int(r), int(g), int(b), 1.0)

        elif css3Colors.get(color) is not None:
            rgba = css3Colors[color] + (1.0,)

        if ignoreAlpha:
            return rgba[:3]
        else:
            return rgba

    if isinstance(colors, (list, tuple)):
        return [conv(color) for color in colors]
    else:
        return conv(colors)


def rgbSpline():
    def f(colors):
        r, g, b = [[c[i] for c in colors] for i in range(3)]
        f_r = spline(r)
        f_g = spline(g)
        f_b = spline(b)

        return lambda t: (int(f_r(t)), int(f_g(t)), int(f_b(t)))
    return f
