def suma_natural():
    numero = int(input("Ingresa un numero natural: "))
    suma = sum(range(1, numero + 1))
    print(f"La suma del 1 al {numero} es : {suma}")


suma_natural()