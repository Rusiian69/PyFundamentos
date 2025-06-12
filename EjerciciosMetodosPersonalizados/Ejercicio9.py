def suma_digitos():
    num = int(input("Ingresa un numero entero positov.: "))
    suma = 0

    while num > 0:
        digito = num % 10
        suma += digito
        num = num // 10

    print(f"La suma de los digitos es {suma}")


suma_digitos()