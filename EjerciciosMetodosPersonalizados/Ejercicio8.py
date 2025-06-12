def filtar_multiplos(lista, base):
    lista = list(map(int, input("ingresa la lista: ").split()))
    base = int(input("Ingresa el numero base para filtrar: "))


    resultado = []
    for numero in lista:
        if numero % base == 0:
            resultado.append(numero)

    print(f"Los multiplos en la lista son {resultado}")


filtar_multiplos(2, 5)