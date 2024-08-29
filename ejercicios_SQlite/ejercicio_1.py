import sqlite3

conexion = sqlite3.connect("prueba.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE prueba ()")











conexion.commit()
conexion.close()













