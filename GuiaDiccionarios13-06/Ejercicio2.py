poderes = {
    "Volar": ["Superman", "Mujer maravilla", "Ironman"],
    "Rayos": ["Superman", "Ironman", "Ciclope", "Capitana marvel"],
    "Velocidad": ["Flash", "Superman"],
    "Fuerza": ["Hulk", "Mujer maravilla", "Superman"],
    "Inteligencia": ["Ironman", "Profesor-X"]
}




def agregarsuperheroe():
    nombre = input("Ingresa el nombre: ")
    poder = input("Ingresa el poder: ").capitalize()

    if poder not in poderes:
        poderes[poder] = [nombre]
        print("Se creo el poder y se agrego")

    elif nombre not in poderes[poder]:
        poderes[poder].append(nombre)
        print(f"El superheroe fue agreagado a {poder}")
    else:
        print("Ya existe uno con estas caracteristicas")


def EliminarSuperheroe():
    nombre = input("Ingresa el nombre: ")
    eliminado = False

    for lista in poderes.values():
        if nombre in lista:
            lista.remove(nombre)
            eliminado = True

    if eliminado:
        print("Eliminado de los poderes")
    else:
        print("No se encontro")


def ConUnPoder():
    poder1 = input("Ingresa el primer poder: ").capitalize()
    poder2 = input("Ingresa el segundo poder: ").capitalize()


    lista1 = poderes.get(poder1, [])
    lista2 = poderes.get(poder2, [])

    resultado = list(set(lista1 + lista2))
    if resultado:
        print("Con al menos un poder: ")
        for heroe in resultado:
            print(heroe)

    else:
        print("no hay con este poder")


def ConAmbosPOderes():
    poder1 = input("Ingresa el primer poder: ").capitalize()
    poder2 = input("Ingresa el segundo poder: ").capitalize()

    lista1 = poderes.get(poder1, [])
    lista2 = poderes.get(poder2, [])

    resultado = list(set(lista1) & set(lista2))

    if resultado:
        print("Con ambos poderes: ")
        for heroe in resultado:
            print(heroe)
    else:
        print("No hay con estos poderes")


def menu():
    while True:
        print("1- Agregar superheroe a poder")
        print("2- Eliminar superheroe de los poderes")
        print("3- Mostar superheroes con al menos uno de dos poderes")
        print("4-Mostrar los que tengan dos poderes")
        print("5- Salir")


        opcion = input("INGRESA la opcion : ")

        if opcion == "1":
            agregarsuperheroe()
        elif opcion == "2":
            EliminarSuperheroe()
        elif opcion == "3":
            ConUnPoder()
        elif opcion == "4":
            ConAmbosPOderes()
        elif opcion == "5":
            print("adios")
            break
        else:
            print("Opcion invalida")




menu()




