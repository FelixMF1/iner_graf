#JEYZON MAURILIO BARRAGAN ESPINO
#FELIX MORALES FLORES
#RICARDO VAZQUEZ MURILLO

import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk 
from tkinter import * 
import tkinter as tk 
import numpy as np 
import sympy as sp 

#Pantalla
root = Tk() 
root.geometry("800x750") 
root.config(bg="beige")
fig, ax = plt.subplots() 
ax.grid(True) 

frame = Frame(root,bg="beige") 
titulo = Label(frame, text="Localización de raíz mediante Newton-Raphson",bg="white")
titulo.config(font=("Roboto",22))
titulo.pack(padx=10, pady=10, side=TOP)

izq = Frame(frame,bg="beige")
izq.pack(side=LEFT)

#GRAFICA
def calcular(): #función calcular - permite hacer la gráfica de la función
    ax.clear() #borra la gráfica anterior
    funcion_e = funcion.get() #recibe la función ingresada
    funcionE = eval('lambda x: ' + funcion_e) #la combierte en función anónima
    x = np.linspace(int(funcionI.get()), int(funcionF.get())) #crea los valores de x tomando los valores iniciales y finales introducidos
    y = funcionE(x) #evalua la función
    ax.plot(x, y) #crea el gráfico
    canvas.draw()   #dibuja el gráfico 

#CALCULA RAIZ CON METODO DE NEWTHON-RAPHSON
def raiz(): 
    x = sp.Symbol('x') 
    f_str = funcion.get() 
    f = sp.sympify(f_str) 
    df = sp.diff(f, x) 
    derivada_text = str(df) 

    tolerancia = 1e-6 
    max_iter = 100 
    x0 = float(VI.get()) 

    for i in range(max_iter): 
        derivada = df 
        derivada_value = derivada.subs(x, x0) 
    
        if abs(derivada_value) < tolerancia: 
            print("La derivada es cercana a cero en el punto x = ", x0)
            break
    
        x1 = float(x0) - float(f.subs(x, x0)) / float(derivada_value) #se calcula la raíz
    
        if abs(x1 - x0) < tolerancia: 
            mostrar_raiz.config(text=x1) 
            break
    
        x0 = x1 
    plt.scatter(x1,0) 

#ETIQUETA Y ENTRADA DE FUNCION
etiqueta_funcion = Label(izq, text="Función f(x):", font=("Roboto",12, "bold"),bg="beige")#.place(relx=0.1,rely=0.1)
etiqueta_funcion.pack(padx=4, pady=4)
funcion = StringVar()
entrada_funcion = Entry(izq, textvariable=funcion)#.place(relx=0.1,rely=0.15) #se guarda en la variable funcion
entrada_funcion.pack(padx=4, pady=4)

#ETIQUETA Y ENTRADA DEL VALOR INICIAL
etiqueta_valorInicial = Label(izq, text="Valor inicial:", font=("Roboto",12, "bold"),bg="beige")#.place(relx=0.1,rely=0.2)
etiqueta_valorInicial.pack(padx=4, pady=4)
funcionI = StringVar()
entrada_funcionInicial = Entry(izq, textvariable=funcionI)#.place(relx=0.1,rely=0.25) #se guarda el valor inicial de la gráfica en funcionI
entrada_funcionInicial.pack(padx=4, pady=5)

#ETIQUETA Y ENTRADA DEL VALOR FINAL
etiqueta_valorFinal = Label(izq, text="Valor final:", font=("Roboto",12, "bold"),bg="beige")#.place(relx=0.4,rely=0.1)
etiqueta_valorFinal.pack(padx=4, pady=5)
funcionF = StringVar()
entrada_valorFinal = Entry(izq, textvariable=funcionF)#.place(relx=0.4,rely=0.15) #se guarda el valor final en funcionF
entrada_valorFinal.pack(padx=4, pady=6)

#ETIQUETA DEL VALOR INICIAL PARA ENCONTRAR LA RAIZ
etiqueta_VI = Label(izq, text="Valor inicial para obtener la raíz", font=("Roboto",12, "bold"),bg="beige")#.place(relx=0.4,rely=0.20)
etiqueta_VI.pack(padx=4, pady=6)
VI = StringVar()
entrada_VI = Entry(izq, textvariable=VI)#.place(relx=0.4,rely=0.25) #se guarda en VI
entrada_VI.pack(padx=4, pady=7)

#BOTON DE GRAFICA
boton_calcular = Button(izq, text="Graficar", command=calcular,bg="green",width=9, height=2).place(relx=0.8,rely=0.2) #contiene el comando calcular que llama la función para graficar
#boton_calcular.pack(padx=4, pady=8)

#BOTON DE RAIZ
boton_raiz = Button(izq, text="Raiz", command=raiz,bg="green",width=9, height=2).place(relx=0.8,rely=0.3) #contiene el comando raiz que llama la función para obtener la raiz
#boton_raiz.pack(padx=4, pady=8)

#RAIZ
mostrar_raiz = Label(izq, text=" ",bg="white")
mostrar_raiz.pack(padx=4, pady=4)

canvas = FigureCanvasTkAgg(fig, master=izq)
canvas.get_tk_widget().pack()

frame.pack()
root.mainloop()