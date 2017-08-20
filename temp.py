# -*- coding: utf-8 -*-

import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()
def temp():
    try:
        return 'Temperature: {0:0.2f} °C'.format(sensor.read_temperature())
    except:
        pass
def pressure():
    try:
        return 'Pressure: {0:0.2f} Pa'.format(sensor.read_pressure())
    except:
        pass

#print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
#print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))