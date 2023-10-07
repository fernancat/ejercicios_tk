import tkinter as tk

def convertir():
    try:
        kilometros = float(entrada_kilometros.get())
        millas = kilometros * 0.621371
        etiqueta_resultado.config(text=f"{kilometros} Kilometros son {millas} millas")
    except ValueError:
        etiqueta_resultado.config(text="Ingresa un valor númerico valido")

ventana = tk.Tk()#frame
ventana.title("Conversor de kilometros a millas")
ventana.geometry("300x150")

#labels instruccion

etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distancia en kilometros: ")
etiqueta_instruccion.grid(row=0,column=0,columnspan=2,padx=10, pady=10)

#crear campo de entrada y colocarlo en una cuadricula
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
#crear boton de conversion y ponerlo en cuadricula
boton_convertir = tk.Button(ventana,text="Convertir",command=convertir)

boton_convertir.grid(row=1,column=1,padx=10,pady=10)

#crear etiqueta de resultado y colocarlo en la pantalla
etiqueta_resultado = tk.Label(ventana,text="")
etiqueta_resultado.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

ventana.mainloop()