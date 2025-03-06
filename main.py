import machine
import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
button = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP)


def greeting():
    
    lcd.clear()
    lcd.move_to(5,0)
    lcd.putstr("Vojtech")
    lcd.move_to(5,1)
    lcd.putstr("Bezdek")
    lcd.move_to(11,1)
    lcd.putchar(chr(2))
    lcd.putchar(chr(3))
    utime.sleep(2)

    


def customcharacter():
    
  #character      
  lcd.custom_char(0, bytearray([
  0x0E,
  0x0E,
  0x04,
  0x1F,
  0x04,
  0x0E,
  0x0A,
  0x0A
        
        ]))
  
    #character2      
  lcd.custom_char(1, bytearray([
    0x1F,
  0x15,
  0x1F,
  0x1F,
  0x1F,
  0x0A,
  0x0A,
  0x1B
        
        ]))
  
  
  
  
  #smiley
  lcd.custom_char(2, bytearray([
  0x00,
  0x00,
  0x0A,
  0x00,
  0x15,
  0x11,
  0x0E,
  0x00
        
        ]))
  
  #heart
  lcd.custom_char(3, bytearray([
   0x00,
  0x00,
  0x0A,
  0x15,
  0x11,
  0x0A,
  0x04,
  0x00
        
        ]))
  
      #note
  lcd.custom_char(4, bytearray([
   0x01,
  0x03,
  0x05,
  0x09,
  0x09,
  0x0B,
  0x1B,
  0x18
        
        ]))
    #celcius
  lcd.custom_char(5, bytearray([
  0x07,
  0x05,
  0x07,
  0x00,
  0x00,
  0x00,
  0x00,
  0x00
        
        ]))
  

    
while True:
    if button.value() == 1:
        greeting()
    if button.value() == 0:
        lcd.clear()