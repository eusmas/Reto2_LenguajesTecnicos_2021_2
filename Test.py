import serial, time, sys

arduino=serial.Serial('COM1', 9600)


def orden(numero):
    dato = str(numero)
    arduino.write(dato.encode())
    time.sleep(1)

def lectura():
    lectu=str(arduino.readline())
    print (lectu)
    time.sleep(1)

    
print ("Ingrese un numero del 1 al 4")
dato = str(input())
orden(dato)


