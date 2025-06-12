def contar_mayores():
    lista = list(map(int, input("ingresa un lista de numeros: ").split()))
    valor = int(input("Ingresa un numero comparar: "))

    contador = 0
    for numero in lista:
        if numero > valor:
            contador += 1


    print(f"La cantidad mayores al numero son {contador}")


contar_mayores()