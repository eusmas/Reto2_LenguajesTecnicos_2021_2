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

    
print ("Ingrese 1 para encender el led y 0 para apaga el led")
dato = str(input())
orden(dato)