from machine import Pin
import neopixel

# number of pixels
n = 12

#  control pin 
p = 26 # D1 til pin 26

#oprette et NeoPixel-objekt
np = neopixel.NeoPixel(Pin(p),n)

# set every pixel (1st pixel = index [0]) to red color
def red_color():
    np[0] = (255, 0, 0)
    np[1] = (255, 0, 0)
    np[2] = (255, 0, 0)
    np[3] = (255, 0, 0)
    np[4] = (255, 0, 0)
    np[5] = (255, 0, 0)
    np[6] = (255, 0, 0)
    np[7] = (255, 0, 0)
    np[8] = (255, 0, 0)
    np[9] = (255, 0, 0)
    np[10] = (255, 0, 0)
    np[11] = (255, 0, 0)
    np.write()
    

def Green_color():
    np[0] = (0, 255, 0)
    np[1] = (0, 255, 0)
    np[2] = (0, 255, 0)
    np[3] = (0, 255, 0)
    np[4] = (0, 255, 0)
    np[5] = (0, 255, 0)
    np[6] = (0, 255, 0)
    np[7] = (0, 255, 0)
    np[8] = (0, 255, 0)
    np[9] = (0, 255, 0)
    np[10] = (0, 255, 0)
    np[11] = (0, 255, 0)
    np.write()



