import random
import math 

def leer_numero(ini,fini,mensaje):   
    while True:
        try:
            n1 = int(input(mensaje))  

        except:
            print("Error: número no válido")
        
        else:
            if n1 >= ini and n1 <= fini: 
                break 
    
    return n1 


def generador():
    numeros = leer_numero(1,20," ¿Cuantos números quieres generar? [1-20]")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal")

    list = []
    for n in range(numeros):
        i = random.uniform(0,101)
        if modo == 1:
            i_alza =  math.floor(i)
            list.append(i_alza)
            print("Número normal:",i,"Número redondeado:",i_alza)
        elif modo == 2:
            i_baja = math.ceil(i)
            list.append(i_baja)
            print("Número normal:",i, "Número redondeado a la baja:",i_baja)
        elif modo == 3:
            i_normal = round(i)
            list.append(i_normal)
            print("Número normal:",i,"Número redondeado de forma normal:",i_normal)
        else:
            print("Modo solo puede valer 1, 2 ó 3")
    return list 

generador()