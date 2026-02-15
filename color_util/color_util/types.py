from dataclasses import dataclass


@dataclass
class ColorRGBA:
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0


@dataclass
class ColorRGBA24:
    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 255


@dataclass
class ColorHSVA:
    h: float = 0.0
    s: float = 0.0
    v: float = 0.0
    a: float = 1.0


@dataclass
class ColorHSVA24:
    h: int = 0
    s: int = 0
    v: int = 0
    a: int = 255
