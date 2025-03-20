import dht
import machine
import time
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

tlacitko = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)

meric = machine.Pin(2)

sensor = dht.DHT11(meric)

stav= 0
minulý_stav = 0  

while True:
    
    aktuální_stav = tlacitko.value()
 
    if aktuální_stav == 1 and minulý_stav == 0:
        stav = (stav + 1) % 2
        print(f"Stav: {stav}")
    
    sensor.measure() 
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    

    if stav == 0:
        lcd.clear()
        lcd.move_to(5,0)
        lcd.putstr('Teplota:')
        lcd.move_to(5,1)
        lcd.putstr('%3.1f C' %temp)
    if stav == 1:
        lcd.clear()
        lcd.move_to(5,0)
        lcd.putstr('Vlhkost:')
        lcd.move_to(5,1)
        lcd.putstr('%3.1f %%' %hum)
    minulý_stav = aktuální_stav
    time.sleep(0.1)