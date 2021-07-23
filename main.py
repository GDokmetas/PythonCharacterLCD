from machine import *
from i2clcd import I2cLcd
uart = UART(1, 9600, tx = Pin(8), rx = Pin(9))
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)    
lcd = I2cLcd(i2c, 0x3F, 4, 20) 
lcd.backlight_on()
lcd.display_on()
lcd.move_to(0, 0)
backlight = True
lcd.hide_cursor()
while True:
    rx = bytes()
    while uart.any() > 0:
        ch = uart.read(1).decode('Ascii')
        if(ch == '*'):
            lcd.clear()
            lcd.move_to(0, 0)
        elif(ch == '\\'):
            if(backlight == True):
                lcd.backlight_off()
                backlight = False
            else:
                lcd.backlight_on()
                backlight = True
        elif(ch == '?'):
            lcd.move_to(0,0)
        else:
            lcd.putchar(ch)

