import random 



def leer_numero(ini, fini):
    try:
        ini = float(input())
        fini = float(input())
        n = float(input("Ahora genera un número entre", ini, "y", fini))
        
    except  n < = ini or n  = > fini:
        print("El número debe ser entre", ini, "y", fini)

def generador():
    numeros = leer_numero()
    modo = leer_numero()
