def maximo_de_tres():
    a = int(input("Ingresa el primer  numero : "))
    b = int(input("Ingresa el segundo numero: "))
    c = int(input("Tercer numero : "))

    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c

        print(f"El mayor es {maximo}")


maximo_de_tres()