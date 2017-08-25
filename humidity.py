import RPi.GPIO as GPIO
import DHT11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
def temp():
    instance = DHT11.DHT11(pin=26)
    result = instance.read()
    return  result.temperature
def hum():
    instance = DHT11.DHT11(pin=26)
    result = instance.read()
    humbool = True
    if(result.humidity == 0):
        humbool = False
    return humbool, 'Humidity: {} %'.format(result.humidity)