#! /usr/bin/env python
# this script will display colors for individual pixels on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.set_pixel(6, 4, (0, 0, 255))
sense.set_pixel(2, 4, (0, 255, 255))
sense.set_pixel(3, 5, (255, 0, 0))
sense.set_pixel(1, 0, (0, 0, 255))
sense.set_pixel(2, 5, (255, 0, 125))
sense.set_pixel(6, 7, (0, 0, 255))
sense.set_pixel(4, 3, (255, 255, 255))
sense.set_pixel(7, 6, (0, 255, 0))

time.sleep(1)
sense.clear()
