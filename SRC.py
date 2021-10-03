#Codigo full

import serial
import time


ser=serial.Serial("COM1",9600)
time.sleep(1)
#ser.flushInput()
#ser.setDTR(True)


while True:
    dato=ser.readline().decode()
    print("El dato es: ", dato)
ser.close()