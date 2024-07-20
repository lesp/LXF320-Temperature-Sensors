import machine
import onewire
import ds18x20
import time

ds_pin = machine.Pin(17)
ds18b20_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds18b20_sensor.scan()

while True:
  ds18b20_sensor.convert_temp()
  time.sleep(1)
  for rom in roms:
    tempC = ds18b20_sensor.read_temp(rom)
    print('The temperature is:', "{:.2f}ºC".format(tempC))
  time.sleep(5)