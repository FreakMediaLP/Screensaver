import ssd1306

import machine
import time


i2c = machine.SoftI2C(scl=machine.Pin(32), sda=machine.Pin(33))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

text = "Python"

x, y = 0, 0
xdir, ydir = True, True
xlim, ylim = 128 - (len(text[:15]) * 8), 55
corners = [[0, 0], [xlim, 0], [0, ylim], [xlim, ylim]]
cornercount = 0
print(xlim, ylim)
while True:
    if not (x < 15 and y < 15):
        oled.text(str(cornercount), 3, 3)
    oled.text(text[:15], x, y)
    oled.show()
    oled.fill(0)
    
    if x == xlim:
        xdir = False
    elif x == 0:
        xdir = True

    if y == ylim:
        ydir = False
    elif y == 0:
        ydir = True

    x = x + 1 if xdir else x - 1
    y = y + 1 if ydir else y - 1
    
    if [x, y] in corners:
        cornercount += 1
        for i in range(5):
            oled.invert(True)
            time.sleep(0.1)
            oled.invert(False)
            time.sleep(0.1)
