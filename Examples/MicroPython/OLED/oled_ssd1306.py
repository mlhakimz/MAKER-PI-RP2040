# This code displays pi image & text on I2C OLED display, then repeats forever.
# Also print out the OLED's I2C address on serial at program start.
# ---
# Connection: SCL = GP1, SDA = GP0
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
#    - Any RP2040 boards should work too.
# 2. Grove OLED Display 0.96 inch (www.cytron.io/p-grove-oled-display-0p96-inch-ssd1315)
# ---
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                            # oled display height

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address: "+hex(i2c.scan()[0]).upper()) # Display device address

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

while True:
    # Clear the oled display in case it has junk on it.
    oled.fill(0)

    # Blit the image from the framebuffer to the oled display
    oled.blit(fb, 50, 20)
    oled.show()
    utime.sleep(2)
    
    # Clear the oled display in case it has junk on it.
    oled.fill(0)

    # Add some text
    oled.text(" MAKER PI PICO",0,10)
    oled.text("      ----",0,20)
    oled.text("  Simplifying",0,30)
    oled.text("   RPi Pico",0,40)
    oled.text(" for Beginners",0,50)
    
    # Finally update the oled display so the image & text is displayed
    oled.show()
    utime.sleep(3)