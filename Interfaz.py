from tkinter import *
import serial, time, sys

arduino=serial.Serial('COM1', 9600)

def orden(numero):
    dato = str(numero)
    arduino.write(dato.encode())
    time.sleep(1)

root = Tk()
root.title("Reto #2")
root.config(width=500,height=500)

Label(root,text="Reto#2 Lenguajes Tecnicos 2021-2",bg="blue").grid(row=0,column=0,columnspan=5,sticky=W+E)
Label(root,text="Escoja el piso al cual desplazarse").grid(row=2,column=0,columnspan=5,sticky=W+E)

Button(root,text="4",command=orden(4)).grid(row=4,column=1,sticky=W+E)
Button(root,text="3",command=orden(3)).grid(row=5,column=1,sticky=W+E)
Button(root,text="2",command=orden(2)).grid(row=6,column=1,sticky=W+E)
Button(root,text="1",command=orden(1)).grid(row=7,column=1,sticky=W+E)


print ("Ingrese 1 para encender el led y 0 para apaga el led")
dato = str(input())
arduino.write(dato.encode())

root.mainloop()

