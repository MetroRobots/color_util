from color_util import ColorHSVA24, ColorRGBA24
from color_util import convert_color_to_float, convert_color_to_int


def test_full_color():
    inc = 1  # can increase this to speed up tests

    for i in range(0, 256, inc):
        for j in range(0, 256, inc):
            for k in range(0, 256, inc):
                for a in range(0, 256, 50):  # don't test all alpha values
                    rgba24 = ColorRGBA24(i, j, k, a)
                    hsva24 = ColorHSVA24(i, j, k, a)

                    rgba = convert_color_to_float(rgba24)
                    hsva = convert_color_to_float(hsva24)

                    assert rgba24 == convert_color_to_int(rgba)
                    assert hsva24 == convert_color_to_int(hsva)
