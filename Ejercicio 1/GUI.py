import tkinter as tk 
import csv
import pyttsx3

def GUI():

    engine1 = pyttsx3.init()
    engine1.say("¿Que deseas realizar? ")
    engine1.runAndWait()

    preguntar = tk.Tk()
    preguntar.title("CSV")
    preguntar.geometry("240x250+700+280")
    preguntar.resizable(width=False, height=False)
    preguntar.iconbitmap("pregunta.ico")
    preguntar.config(background="khaki1")

    Label=tk.Label(preguntar,
    text="Elija una opción",
    background="khaki1",
    font=("Arial", 18, "bold"),
    foreground="black"
    )
    
    Label.pack(pady=25)

    def entrys_llenar():
        ventana2=tk.Tk()
        ventana2.title("DATOS CSV")
        ventana2.geometry("500x300+500+250")
        ventana2.resizable(width=True, height=True)
        ventana2.iconbitmap("pregunta.ico")
        ventana2.config(background="linen")
               

        Label2=tk.Label(ventana2,
            text="Apellido Paterno:",
            font=("Arial", 16),
            background="linen",
            foreground="black"
        )
        Label2.grid(column=0, row=0, padx=10, pady=10)

        Label3=tk.Label(ventana2,
            text="Apellido Materno:",
            font=("Arial", 16),
            background="linen",
            foreground="black"
        )
        Label3.grid(column=0, row=1, padx=10, pady=10)

        Label4=tk.Label(ventana2,
            text="Nombre: ",
            font=("Arial", 16),
            background="linen",
            foreground="black"
        )
        Label4.grid(column=0, row=2, padx=10, pady=10)

        Entry2=tk.Entry(ventana2,
            font=("Arial", 16),
            foreground="black"
        )
        Entry2.grid(column=1, row=0, padx=10, pady=10,columnspan=2)

        Entry3=tk.Entry(ventana2,
            font=("Arial", 16),
            foreground="black"
        )
        Entry3.grid(column=1, row=1, padx=10, pady=10,columnspan=2)

        Entry4=tk.Entry(ventana2,
            font=("Arial", 16),
            foreground="black"
        )
        Entry4.grid(column=1, row=2, padx=10, pady=10,columnspan=2)

        def llenar():        
            lista=[]

            a=Entry2.get()
            b=Entry3.get()
            c=Entry4.get()

            lista.append(a)
            lista.append(b)
            lista.append(c)

            writer=csv.writer(open("datos.csv", "a", newline=""))
            writer.writerow(lista)

            lista.clear()
            engine2 = pyttsx3.init()
            engine2.say("¿Desea agregar a otra persona? sino, solo cierre la ventana y visualice los datos ")
            engine2.runAndWait()


        botoningresar=tk.Button(ventana2,
            text="INGRESAR DATOS",
            font=("Arial", 16),
            background="honeydew2",
            activebackground="honeydew3",
            command=llenar
        )

        botoningresar.grid(column=2, row=4)

        ventana2.mainloop()


    boton1 = tk.Button(preguntar,
    text = "Registrar mis datos",
    font = ("Times", 14),
    background="orangered2",
    activebackground="orangered4",
    command=entrys_llenar
    )

    boton1.pack(pady=10)

    def consultar():
        
        reader=csv.reader(open("datos.csv", "r"))
        for row in reader:
            print("Apellido Paterno: {0}, Apellido Materno: {1}, Nombre: {2}".format(row[0], row[1], row[2]))
        

    boton2 = tk.Button(preguntar,
    text = "Ver todos los datos",
    font = ("Times", 14),
    background="green2",
    activebackground="green4",
    command=consultar
    )

    boton2.pack(pady=10)


    preguntar.mainloop()