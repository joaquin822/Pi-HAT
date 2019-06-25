#! /usr/bin/env python
# this script will display colors for individual pixels on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
r = (255, 0, 0)
y = (255, 255, 0)
b = (0, 0, 255)
bk = (0, 0, 0)
w = (255, 255, 255)
gy = (155, 155, 155)
g = (0, 255, 0)
c = (0, 255, 255)
rb = (255, 0, 125)

pixels = [
    b, b, b, b, r, r, r, r,
    b, b, b, b, w, w, w, w,
    b, b, b, b, r, r, r, r,
    b, b, b, b, w, w, w, w,
    r, r, r, r, r, r, r, r,
    w, w, w, w, w, w, w, w,
    r, r, r, r, r, r, r, r, 
    w, w, w, w, w, w, w, w,
]

sense.set_pixels(pixels)

pixels = [
    b, b, b, b, w, w, w, w,
    b, b, b, b, w, w, w, w,
    b, w, w, b, w, w, w, w,
    b, w, w, b, w, w, w, w,
    b, w, w, b, r, r, r, r,
    b, w, w, b, r, r, r, r,
    b, b, b, b, r, r, r, r, 
    b, b, b, b, r, r, r, r,
]

sense.set_pixels(pixels)
