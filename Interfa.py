from tkinter import *
import serial, time, sys

arduino=serial.Serial('COM1', 9600)


def orden(numero):
    dato = str(numero)
    dato2=tiempo.get()
    if int(dato2) <= 9:
        arduino.write(dato.encode() + dato2.encode() )
        lectu=str(arduino.readline())##
        nivelactual.delete(0,END)
        nivelactual.insert(0,lectu)##
    else:
        nivelactual.delete(0,END)
        nivelactual.insert(0,"Tiempo incorrecto")
    time.sleep(1)
    print(dato.encode() + dato2.encode() )

def lectura():
    lectu=str(arduino.readline())
    print (lectu)
    time.sleep(1)
    return lectu


root = Tk()
root.title("Reto #2")
root.config(width=500,height=500)

#Encabezado
Label(root,text="Reto#2 Lenguajes Tecnicos 2021-2",bg="blue").grid(row=0,column=0,columnspan=5,sticky=W+E)
Label(root,text="Escoja el piso al cual desplazarse").grid(row=2,column=0,columnspan=5,sticky=W+E)

#Botones
Button(root,text="4",command=lambda:orden(4)).grid(row=4,column=1,sticky=W+E)
Button(root,text="3",command=lambda:orden(3)).grid(row=5,column=1,sticky=W+E)
Button(root,text="2",command=lambda:orden(2)).grid(row=6,column=1,sticky=W+E)
Button(root,text="1",command=lambda:orden(1)).grid(row=7,column=1,sticky=W+E)

#Label
Label(root,text="Piso actual").grid(row=4,column=3,columnspan=1,sticky=W+E)
nivelactual=Entry(root)
nivelactual.grid(row=5,column=3,columnspan=1,sticky=W+E)
Label(root,text="Tiempo puerta (0-9)s").grid(row=6,column=3,columnspan=1,sticky=W+E)
tiempo=Entry(root)
tiempo.grid(row=7,column=3,columnspan=1,sticky=W+E)
#print(tiempo)

root.mainloop()