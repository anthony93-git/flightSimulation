#pip3 install Adafruit_BBIO -U
#pipe install adafruit_circuitpython-lis3dh
#pipe install adafruit-circuitpython-busdevice
#pip3 install adafruit-circuitpython-register
#pip3 install adafruit-circuitpython-bmp3xxx
#pip3 install adafruit-blinka
#
#pip3 install afafruit-circuitpython-ssd1306
#apt-get install python3-pil
#
#arm device
#terminate flight

import sys
import time
import board
import busio
import digitalio
import adafruit_ssd1306
import adafruit_bmp3xx
import Adafruit_BBIO.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
from time import sleep

#Defining objects and variables
WIDTH = 128
HEIGHT = 64
BORDER = 5
buzzer = "P9_11"
recButtonLED = "P8_8"
recButton = "P8_7"
stopButtonLED = "P8_10"
stopButton = "P8_9"
i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
reset_pin = digitalio.DigitalInOut(board.P9_12)
i2c2 = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c2, addr=0x3d, reset=reset_pin)
image = Image.new("1", (oled.width, oled.height))
image2 = Image.new("1", (oled.width, oled.height))
image3 = Image.new("1", (oled.width, oled.height))
image4 = Image.new("1", (oled.width, oled.height))
image5 = Image.new("1", (oled.width, oled.height))
image6 = Image.new("1", (oled.width, oled.height))
image7 = Image.new("1", (oled.width, oled.height))
image8 = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)
draw3 = ImageDraw.Draw(image3)
draw4 = ImageDraw.Draw(image4)
draw5 = ImageDraw.Draw(image5)
draw6 = ImageDraw.Draw(image6)
draw7 = ImageDraw.Draw(image7)
draw8 = ImageDraw.Draw(image8)

#Setting up GPIO and sensor attributes
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(recButtonLED,GPIO.OUT)
GPIO.setup(recButton, GPIO.IN)
GPIO.setup(stopButtonLED, GPIO.OUT)
GPIO.setup(stopButton, GPIO.IN)
bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2
bmp.sea_levelpressure = 1013.25

#Defining attributes and opening csv file for writing 
temperature = bmp.temperature #read in celsius
pressure = bmp.pressure #read in hectopascals or millibars
altitude = bmp.altitude #read in meters
f = open("/root/flightOutput.csv", "a")

#print("\n\n.........Welcome to the MADCOW SUPER DX3 Flight Computer.........")
#print("........................by Anthony Montano...................\n\n")

oled.fill(0)
oled.show()

font = ImageFont.truetype("DejaVuSans-Bold.ttf",13)
font2 = ImageFont.truetype("DejaVuSans.ttf", 8)
font3 = ImageFont.truetype("DejaVuSans-Bold.ttf",10)
font4 = ImageFont.truetype("DejaVuSans-Bold.ttf",12)
font5 = ImageFont.truetype("DejaVuSans-Bold.ttf",11)
text0 = "-----------------------------"
text1 = "MADCOW"
text2 = "SUPER"
text3 = "DX3"
text4 = "---------------------------"
text5 = "WARNING!!"
text6 = " Proceed with extreme caution.\n     Motor contains explosive\n  agents and may cause injury\n     or death. Device must be-" 
text7 = "   Stored in a dry area where\n  temperatures do not exceed\n  100 degrees Fahrenheit and\nsubceed 45 degrees Fahrenheit."
text8 = "Telemetry"
text9 = "_____________________________________"
text10 = "Temp"
text11 = "Pres"
text12 = "Alt"
text13 = "C"
text14 = "hPa"
text15 = "m"
text16 = "  Engage flashing \n       button to \n      ARM DEVICE"
text17 = "     Engage final \n       button to \nTERMINATE FLIGHT"
text18 = "LAUNCHING"
text19 = "INTERFACE..."
text20 = "    FLIGHT"
text21 = "TERMINATED"

draw.text((0,0),text0,font=font,fill=255)
draw.text((30,10),text1,font=font,fill=255)
draw.text((42,25),text2,font=font,fill=255)
draw.text((50,40),text3,font=font,fill=255)
draw.text((0,50),text4,font=font,fill=255)

oled.image(image)
oled.show()

#sleep(1)
sleep(6)

oled.fill(0)
oled.show()

draw2.text((25,0),text5,font=font,fill=255)
draw2.text((0,15),text6,font=font2,fill=255)
oled.image(image2)
oled.show()

#sleep(1)
sleep(9)

oled.fill(0)
oled.show()

draw3.text((25,0),text5,font=font,fill=255)
draw3.text((0,15),text7,font=font2,fill=255)

oled.image(image3)
oled.show()

#sleep(1)
sleep(9)

oled.fill(0)
oled.show()

draw4.text((0,9),text16, font=font4,fill=255)

oled.image(image4)
oled.show()

while(1):
    if GPIO.input(recButton):
        break
    else:
        GPIO.output(recButtonLED, GPIO.HIGH)
        sleep(1)
        GPIO.output(recButtonLED, GPIO.LOW)
        sleep(1)

GPIO.output(recButtonLED, GPIO.HIGH)

oled.fill(0)
oled.show()

draw5.text((0,5),text17,font=font4,fill=255)

oled.image(image5)
oled.show()

sleep(3)

oled.fill(0)
oled.show()

draw6.rectangle((-1,28,150,8), outline=255, fill=255)
draw6.text((20,10),text18,font=font, fill=0)
draw6.rectangle((-1,53,150,33),outline=255, fill=255)
draw6.text((20,35),text19,font=font,fill=0)

oled.image(image6)
oled.show()

sleep(3)

oled.fill(0)
oled.show()

draw7.rectangle((37,70,150,18),outline=255,fill=0)
draw7.text((25,0),text8,font=font,fill=255)
draw7.text((0,3),text9,font=font,fill=255)
draw7.text((2, 20),text10,font=font3,fill=255)
draw7.text((8,35),text11,font=font3,fill=255)
draw7.text((16,50),text12,font=font3,fill=255)
draw7.text((105,20),text13,font=font3,fill=255)
draw7.text((105,35),text14,font=font3,fill=255)
draw7.text((105,50),text15,font=font3,fill=255)

oled.image(image7)
oled.show()

sleep(1)

#while(1):
#    if GPIO.input(recButton):
#        break
#    else:
#        GPIO.output(recButtonLED, GPIO.HIGH)
#        sleep(1)
#        GPIO.output(recButtonLED, GPIO.LOW)
#        sleep(1)

#GPIO.output(recButtonLED, GPIO.HIGH)

for i in range (0,7):
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(.1)
    GPIO.output(buzzer, GPIO.LOW)
    sleep(.1)

sleep(3)


while True:
    if GPIO.input(stopButton):
        break
    else:
#    f.write("Pressure: {:6.4f} hpa\nTemperature: {:5.2f} celsius".format(bmp.pressure,bmp.temperature))

#        print("Pressure: {:6.4f} hPa\nTemperature: {:5.2f} celsius".format(bmp.pressure,bmp.temperature))
    
#        print("Altitude: {:6.4f} meter\n".format(bmp.altitude))
    
        #f.write
        print(time.strftime('%H:%M:%S %d/%m/%Y') + "," + "{:6.4f}".format(bmp.altitude) + "," + " {:6.4f}".format(bmp.temperature) + "," + " {:6.4f}\n".format(bmp.pressure))
    
        #sys.stdout.write(time.strftime('%H:%M:%S %d/%m/%Y') + "," + "(:6.4f)".format(bmp.altitude))
        oled.fill(0)
        oled.show()

    #creating black rectangle to prevent values from writing on top of each other
        draw7.rectangle((37,70,150,18), outline=255, fill=0)

        draw7.text((105,20),text13,font=font3,fill=255)
        draw7.text((47,20),str("{:6.2f} ".format(bmp.temperature)),font=font3,fill=255)
    
        draw7.text((105,35),text14,font=font3,fill=255)
        draw7.text((50,35),str("{:6.2f} ".format(bmp.pressure)),font=font3,fill=255)   
        draw7.text((105,50),text15,font=font3,fill=255)
        draw7.text((50,50),str("{:6.2f} ".format(bmp.altitude)),font=font3,fill=255)
        oled.image(image7)
        oled.show()

#    if GPIO.input(stopButton):
#        break

#    else:
        GPIO.output(buzzer, GPIO.HIGH)
        GPIO.output(stopButtonLED, GPIO.HIGH)
        sleep(.1)
        GPIO.output(buzzer, GPIO.LOW)
        GPIO.output(stopButtonLED, GPIO.LOW)
        sleep(2)

GPIO.output(stopButtonLED, GPIO.HIGH)

oled.fill(0)
oled.show()

draw8.rectangle((-1,28,150,8),outline=255,fill=255)
draw8.text((20,10),text20,font=font,fill=0)
draw8.rectangle((-1,53,150,33),outline=255,fill=255)
draw8.text((20,35),text21,font=font,fill=0)

oled.image(image8)
oled.show()

#    f.close()
#    open("flightOutput.csv", "a")
#    print("Temperature: "),print(temperature),print(" celsius")
#    print("Pressure: " + str(pressure) + " hPa")
#    print("Altitude: " + str(altitude) + " meters\n")


