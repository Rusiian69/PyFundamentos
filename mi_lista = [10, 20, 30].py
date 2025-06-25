estudiantes = {
    "Ana": [6.5, 7.0, 5.8],
    "Carlos": [4.0, 5.5],
    "Javiera": [3.2, 6.0, 6.5, 5.0]
}


def agregar_estudiante():
    nombre = input("Ingresa tu nombre: ")
    if nombre in estudiantes:
        print("Ya esta registrado")
        return
    else:
        lista = []
        cantidad = int(input("Cuantas notas ingresaras: "))
        for i in range(cantidad):
            nota = input("Ingresa la nota: ")
            lista.append(nota)
            
    
    estudiantes[nombre] = lista

agregar_estudiante()
print(estudiantes)
    