diccionario = [
    { "id": 1, "valor": "Cristina", "novio": True, "carrera": "biotec" },
    { "id": 2, "valor": "Lucia", "novio": False, "carrera": "turismo" },
    { "id": 3, "valor": "Maria", "novio": False, "carrera": "sin futuro" },
    { "id": 4, "valor": "Marta", "novio": True, "carrera": "quimica" },
    { "id": 5, "valor": "Julia", "novio": True, "carrera": "sin futuro" },
    { "id": 6, "valor": "Paula", "novio": True, "carrera": "administracion" }
    ] 

registros = []
campos = []

""" for d in diccionario:
        for k in d.keys():
        if k not in campos:
            campos.append(k) """

for d in diccionario:
    sublista = []
    for i, v in d.items():
        sublista.append(v)

    registros.append(sublista)

print(*registros, sep="\n")