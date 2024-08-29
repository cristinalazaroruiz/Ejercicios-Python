import sqlite3
from tkinter import *
from restaurante import * 

auxiliar_1 = False

def mostrar_primeros():
    global auxiliar_1
    if auxiliar_1 == False:
        cursor.execute("SELECT nombre FROM plato WHERE categoria_id=1")  
        primeros = cursor.fetchall()
        texto = "Los primeros a elegir son:\n"
        for elemento in primeros:
            texto += "- "+ elemento[0] + "\n" 
        
        label_primeros.config(text=texto)
        label_primeros.config(bg="lightgreen", fg="grey")
        auxiliar_1 = True

    else:
        label_primeros.config(text="")
        auxiliar_1 = False
    

auxiliar_2 = False 
    
def mostrar_segundos():
    global auxiliar_2
    if auxiliar_2 == False:
            cursor.execute("SELECT nombre FROM plato WHERE categoria_id=2")  
            segundos = cursor.fetchall()
            texto = "Los segundos a elegir son:\n"
            for elemento in segundos:
                texto += "- "+ elemento[0] + "\n" 
            
            label_segundos.config(text=texto)
            label_segundos.config(bg="violet", fg="grey")
            auxiliar_2 = True

    else:
        label_segundos.config(text="")
        auxiliar_2 = False


auxiliar_3 = False 
def mostrar_postres():
    global auxiliar_3
    if auxiliar_3 == False:
        postres =  cursor.execute("SELECT nombre FROM plato WHERE categoria_id=3").fetchall() 
        texto = "Los postres a elegir son\n"
        for elemento in postres:
            texto += "-"+ elemento[0] + "\n"
        
        label_postres.config(text=texto)
        label_postres.config(bg="lightblue")
        auxiliar_3 = True
    
    else:
        label_postres.config(text="")
        auxiliar_3 = False 




root = Tk() #inicio de la interfaz gráfica
root.title("Menú del restaurante Cristina's")
root.resizable(False,False)
root.config(bd=25, relief="sunken")
label1 = Label(root,text="Restaurante Cristina's")
label1.config(bg="pink", fg="white", font=("Verdana",20,"bold italic"))
label1.pack()

label2 = Label(root, text="Menú del día")
label2.config(bg="aqua", fg ="white",font=("Verdana",15, " bold italic"))
label2.pack()

frame_primeros = Frame(root)
frame_primeros.config(cursor="pirate")
frame_primeros.pack()
boton_primeros = Button(frame_primeros, text="primeros", command=mostrar_primeros)
boton_primeros.pack()
label_primeros = Label(frame_primeros, text="" )
label_primeros.pack()


frame_segundos = Frame(root)
frame_segundos.config(cursor="pirate")
frame_segundos.pack()
boton_segundos = Button(frame_segundos, text = "segundos", command= mostrar_segundos)
boton_segundos.pack()
label_segundos = Label(frame_segundos, text = "")
label_segundos.pack()


frame_postres = Frame(root)
frame_postres.config(cursor="pirate")
frame_postres.pack()
boton_postres = Button(frame_postres, text="postres", command=mostrar_postres)
boton_postres.pack()
label_postres = Label(frame_postres, text="")
label_postres.pack()

label_espacio = Label(root, text="\n")
label_espacio.pack()
label_precio = Label(root, text="15,95$")
label_precio.config(bg="lightpink",fg="white",font=("Verdana",15, "bold"))
label_precio.pack(side=RIGHT)





root.mainloop() #fin de la interfaz gráffica 