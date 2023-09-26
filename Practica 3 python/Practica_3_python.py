
import tkinter as tk
def convertir_a_celsius():
    Farenheit = float(entry1.get()) #entry es el text box para poder escribir un valor en pantalla
    #Celsius = (Farenheit - 32) *5.0/9.0
    Celsius = (Farenheit - 32) *5/9
    entry2.delete(0, tk.END) # tx.END sirve para poder borrar el contenido  que se haya escrito en la pantalla
    entry2.insert(0,f"{Celsius:.2f}") #sirve para que el programa escriba el resultado de la operacion como en c# que aparezca un comentario con su resultado
   
def convertir_a_farenheit():
    Celsius = float(entry2.get()) #entry es el text box para poder escribir un valor en pantalla
    #Celsius = (Farenheit - 32) *5.0/9.0
    Fahrenheit = (Celsius*9/5) *32
    entry1.delete(0, tk.END) # tx.END sirve para poder borrar el contenido  que se haya escrito en la pantalla
    entry1.insert(0,f"{Fahrenheit:.2f}") #sirve para que el programa escriba el resultado de la operacion c# que aparezca un comentario con su resultado

def borrar():
    entry1.delete(0, tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0,tk.END)
    entry2.insert(0, "0.0")

app = tk.Tk()
app.title("Conversor de Temperatura")

label1 = tk.Label(app, text= "Fahrenheit: ")
label1.grid(row=0, column=0)

entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

button1 = tk.Button(app, text= "Convertir a celsius", command=convertir_a_celsius)
button1.grid(row=0, column=2)

label2 =tk.Label(app, text= "Celsius")
label2.grid(row=1, column=0)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

button2 = tk.Button(app, text = "Convertir a Farenheit", command=convertir_a_farenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(app, text="Restablecer", command=borrar)
button3.grid(row=2, column=1)

app.mainloop()