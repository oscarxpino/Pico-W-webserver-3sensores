
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network


import gc
gc.collect()

ssid = 'pinoweb'
password = 'pinerus123'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin("LED", Pin.OUT)
led.on()
