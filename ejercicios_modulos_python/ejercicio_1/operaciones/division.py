def division(a,b):
    try:
        return a/b 
    
    except TypeError: 
        print("Los valores introducidos deben ser numéricos, no cadenas")

    except ZeroDivisionError: 
        print("No se puede dividir entre  0")

