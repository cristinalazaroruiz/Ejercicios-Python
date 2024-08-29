import sqlite3
conexion = sqlite3.connect("restaurante.db") #inicio conexión a la base de datos
cursor = conexion.cursor() #a partri de aquí se usa lenguaje sqlite 

#Funciones que podemos ejectuar para hacer cosas sobre nuestra base de datos restaurante.db:

def crear_bd(): #función para crear las tablas (o indicar que ya existen)
    try:
        cursor.execute("CREATE TABLE categoria (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR (100) UNIQUE NOT NULL)")
        print("Tabla categoría creada")
        cursor.execute("CREATE TABLE plato (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR (100) NOT NULL, categoria_id INTEGER NOT NULL, FOREIGN KEY (categoria_id) REFERENCES categoria (id))") #uso del foreign key 
        print("Tabla plato creada")
        conexion.commit() #importante para guardar cambios tras cada acción (execute)

    except Exception as e: 
        print(e)
        print("Las tablas ya se han creado previamente, no se pueden volver a crear")


def agregar_categoria(): #Agregar categorías a la tabla "categoria"
    conexion = sqlite3.connect("restaurante.db") #inicio conexión a la base de datos
    cursor = conexion.cursor() #a partir de aquí se usa lenguaje sqlite 
    query = input("Elige una nueva categoría (si quieres volver atrás escribe 'Cancelar'): ")
    
    if query == "Cancelar": #Medida de seguridad por si realmente no quermos añadir ninguna categoría 
        print("Se ha cancelado la función agregar_categoría")
    
    else:
        try:
            cursor.execute("INSERT into categoria (nombre) VALUES (?)",(query,)) #recordar que el registro debe ir en forma de tupla, sino no va 
            print("Se ha añadido la categoría", query)
            conexion.commit() #importante para guardar cambios tras cada acción (execute)

        except Exception as e:
            print(e)
            print("Aglo ha ido mal, probablmente la cateogría ya existe y no se puede duplicar")
        


def agregar_plato(): #Añadir un plato a la tabla platos, seleccionando el id de la tabla categoria  
    cursor.execute("SELECT * FROM categoria")
    nombre_categorias = cursor.fetchall()
    for categoria in nombre_categorias:
        print("[{}] {}".format(categoria[0],categoria[1])) #mostrar todas las categorías al usuario 
    seleccion = int(input("Elige el id de la cateogría que desea escoger: ")) #id de la tabla categorías 
    seleccion_plato =input("Elige el nombre del plato que desa añadir a la base de datos: ") #nombre del plato que tendrá el id de la tabla categorías 
    tupla = (seleccion_plato, seleccion) #los valores se introducen con INSERT en forma de tupla 
    try:
        cursor.execute("INSERT into plato VALUES (null,?,?)",tupla)
        conexion.commit() 
    except Exception as e: 
        print(e)

def mostrar_menu():
    cursor.execute("SELECT nombre FROM plato WHERE categoria_id=1") #mostramos los primeros 
    primeros = cursor.fetchall()
    print("Los primeros a elegir son:")
    for elemento in primeros:
        print("- ",elemento[0])
    
    cursor.execute("SELECT nombre FROM plato WHERE categoria_id=2") #mostramos los segundos 
    segundos = cursor.fetchall()
    print("Los segundos a elegir son:")
    for elemento in segundos:
        print("- ",elemento[0])

    cursor.execute("SELECT nombre FROM plato WHERE categoria_id=3") #mostramos los postres 
    postres = cursor.fetchall()
    print("Los postres son:")
    for elemento in postres:
        print("- ",elemento[0])

    conexion.commit()
   
#Menú de opciones 
if __name__=="__main__": #para que  al importar y hacer la interfaz en menu.py, no se ejecute  este bloque de código
    while(True):
        eleccion = int(input("Bienvenido a este menú interactivo, qué quieres hacer\n 1)Crear una tabla \n 2)Agregar una nueva categoría\n 3)Agregar Plato \n 4) Mostrar menú \n 5)Salir del programa\n Opción: "))
        if eleccion == 1: #opción para crear la base de datos (si ya existe, se indicará)
            crear_bd()

        elif eleccion == 2: #para agregar  una categoría  (primeros, segundos, postres, entrantes etc )
            agregar_categoria()

        elif eleccion == 3: #añadir diferentes platos a las diferentes categorías 
            agregar_plato()

        elif eleccion == 4: #enseñar los menús generados 
            mostrar_menu()

        elif eleccion == 5: #salir del sistema 
            print("Saliendo del sistema...")
            conexion.commit() #guardar todos los cambis 
            cursor.close() #cerramos cursor 
            conexion.close() #cerramos conexión 
            break 

        else:
            print("Intoduce tu elección en forma de número, las opciones son 1, 2,3,4 ó 5")

