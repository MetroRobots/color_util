
class GenericColorRGBA:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @staticmethod
    def fields():
        return 'rgba'

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b and self.a == other.a

    def __repr__(self):
        return f'(r: {self.r}, g: {self.g}, b: {self.b}, a: {self.a})'


class GenericColorHSVA:
    def __init__(self, h, s, v, a):
        self.h = h
        self.s = s
        self.v = v
        self.a = a

    @staticmethod
    def fields():
        return 'hsva'

    def __eq__(self, other):
        return self.h == other.h and self.s == other.s and self.v == other.v and self.a == other.a

    def __repr__(self):
        return f'(h: {self.h}, s: {self.s}, v: {self.v}, a: {self.a})'


class ColorRGBA(GenericColorRGBA):
    def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0):
        super().__init__(r, g, b, a)


class ColorRGBA24(GenericColorRGBA):
    def __init__(self, r=0, g=0, b=0, a=255):
        super().__init__(r, g, b, a)


class ColorHSVA(GenericColorHSVA):
    def __init__(self, h=0.0, s=0.0, v=0.0, a=1.0):
        super().__init__(h, s, v, a)


class ColorHSVA24(GenericColorHSVA):
    def __init__(self, h=0, s=0, v=0, a=255):
        super().__init__(h, s, v, a)
