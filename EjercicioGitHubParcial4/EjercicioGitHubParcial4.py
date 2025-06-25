estudiantes = {}

def agregar_estudiante():
    nombre = input("Nombre: ")
    if nombre in estudiantes:
        print("Estudiante ya agregado")
        return
    else:
        estudiantes[nombre] = []

def registrar_nota():
    nombre = input("Nombre: ")
    if nombre in estudiantes:
        nota = float(input("Ingresa la nota(1.0-7.0): "))
        if nota < 1.0 or nota > 7.0:
            print("Nota fuera de rango")
            return
        else:
            estudiantes[nombre].append(nota)
    else:
        print("No esta registrado")


def mostar_notas():
    nombre = input("Nombre: ")
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        if notas:
            print("Notas:", notas)
        else:
            print("No hay notas registradas")
    else:
        print("No hay estudiante con ese nombre")



def promedio_general():
    total = 0
    cantidad = 0
    for notas in estudiantes.values():
        total += sum(notas)
        cantidad += len(notas)
    if cantidad == 0:
        print("No hay notas para promediar")
    else:
        promedio =total / cantidad
        print(f"EL PRomedio es {round(promedio, 1)}")



while True:
    print("---Menu---")
    print("1-Agregar estudiante")
    print("2-Registrar nota")
    print("3-Mostar notas de un estudiante")
    print("4-Mostrar promedio general")
    print("5-Salir")

    opcion = input("Ingresa la opcion: ").lower()

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        registrar_nota()
    elif opcion == "3":
        mostar_notas()
    elif opcion == "4":
        promedio_general()
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("Opcion invalida")





