from machine import Pin
import time
import dht 

sensor = dht.DHT11(Pin(17))

while True:
    time.sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    print('The temperature is:', "{:.2f}ºC".format(temp))
    print('The humdity is:', "{:.1f}%".format(humidity))
