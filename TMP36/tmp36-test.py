from machine import ADC
import time

adc_pin = 26
tmp36 = ADC(adc_pin)

while True:
    adc_value = tmp36.read_u16()
    v = (3.3/65535)*adc_value
    tempC = (100*v)-50
    print('The temperature is:', "{:.2f}ºC".format(tempC))
    time.sleep(5)