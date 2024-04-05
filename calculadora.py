from tkinter import *

raiz = Tk()

Frame = Frame(raiz)

Frame.pack()

operacion = ""
resultado = 0


#Pantalla---------------------------------------------------
numeroPantalla = StringVar()
pantalla = Entry(Frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#Pulsacioanes teclado----------------------------------------
def numeroPulsado(num):

    global operacion

    if operacion == "suma" and operacion == "resta":
        numeroPantalla.set(num)


    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#Funcion suma-------------------------------------------------

def suma(num):
     global operacion
     global resultado

     operacion = "suma"
     resultado += float(num)
     numeroPantalla.set(resultado)

#Resta--------------------------------------------------------
def resta(num):
    global operacion
    global resultado

    operacion = "resta"
    resultado = float(num)
    numeroPantalla.set("")

#Division-----------------------------------------------------
def divi(num):
    global operacion
    global resultado

    operacion = "divi"
    resultado = float(num) 
    numeroPantalla.set("")

#Multiplicación-------------------------------------------------

def mult(num):
    global resultado
    global operacion

    operacion = "mult"
    resultado = float(num)
    numeroPantalla.set("")

     
#Resultado----------------------------------------------------

def el_resultado():

    global operacion
    global resultado

    if operacion == "suma":
        numeroPantalla.set(resultado + float(numeroPantalla.get()))
        operacion = ""
        resultado = 0

    elif operacion == "resta":
        numeroPantalla.set(resultado - float(numeroPantalla.get()))
        operacion = ""
        resultado = 0

    elif operacion == "divi":
        numeroPantalla.set(resultado / float(numeroPantalla.get()))
        operacion = ""
        resultado = 0

    elif operacion == "mult":
        numeroPantalla.set(resultado * float(numeroPantalla.get()))

#Fila 1------------------------------------
Button7 = Button(Frame, text="7", width=3, command=lambda:numeroPulsado("7"))
Button7.grid(row=2, column=1)
Button8 = Button(Frame, text="8", width=3, command=lambda:numeroPulsado("8"))
Button8.grid(row=2, column=2)
Button9 = Button(Frame, text="9", width=3, command=lambda:numeroPulsado("9"))
Button9.grid(row=2, column=3)
ButtonX = Button(Frame, text="X", width=3, command=lambda:mult(numeroPantalla.get()))
ButtonX.grid(row=2, column=4)

#Fila 2------------------------------------
Button4 = Button(Frame, text="4", width=3, command=lambda:numeroPulsado("4"))
Button4.grid(row=3, column=1)
Button5 = Button(Frame, text="5", width=3, command=lambda:numeroPulsado("5"))
Button5.grid(row=3, column=2)
Button6 = Button(Frame, text="6", width=3, command=lambda:numeroPulsado("6"))
Button6.grid(row=3, column=3)
Button_ = Button(Frame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
Button_.grid(row=3, column=4)

#Fila 3------------------------------------
Button1 = Button(Frame, text="1", width=3, command=lambda:numeroPulsado("1"))
Button1.grid(row=4, column=1)
Button2 = Button(Frame, text="2", width=3, command=lambda:numeroPulsado("2"))
Button2.grid(row=4, column=2)
Button3 = Button(Frame, text="3", width=3, command=lambda:numeroPulsado("3"))
Button3.grid(row=4, column=3)
ButtonPlus = Button(Frame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
ButtonPlus.grid(row=4, column=4)

#Fila 4------------------------------------
ButtonEqual = Button(Frame, text="=", width=3, command=lambda:el_resultado())
ButtonEqual.grid(row=5, column=1)
Button0 = Button(Frame, text="0", width=3, command=lambda:numeroPulsado("0"))
Button0.grid(row=5, column=2)
ButtonComa = Button(Frame, text=".", width=3, command=lambda:numeroPulsado("."))
ButtonComa.grid(row=5, column=3)
ButtonDiv = Button(Frame, text="/", width=3, command=lambda:divi(numeroPantalla.get()))
ButtonDiv.grid(row=5, column=4)

#Fila 5------------------------------------
ButtonClear = Button(Frame, text="Clear", width=3, command=lambda:numeroPantalla.set(""))
ButtonClear.grid(row=6, column=1)
ButtonClear1 = Button(Frame, text="Clear1", width=5, command=lambda:numeroPulsado("Clear1"))
ButtonClear1.grid(row=6, column=4)
ButtonLast = Button(Frame, text="Last", width=3, command=lambda:numeroPulsado("Last"))
ButtonLast.grid(row=6, column=2)
ButtonSqrt = Button(Frame, text="Sqrt", width=3, command=lambda:numeroPulsado("Sqrt"))
ButtonSqrt.grid(row=6, column=3)


#Main---------------------------------------
raiz.mainloop()
