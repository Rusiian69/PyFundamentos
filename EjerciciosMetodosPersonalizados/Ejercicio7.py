def producto_escalar():
    lista1 = list(map(int, input("Ingresa la primrer lista: ").split()))
    lista2 = list(map(int, input("Ingresa la segunda lista del mismo porte").split()))

    if len(lista1) != len(lista2):
        print("deben ser del mismo largo")
        return
    
    resultado = 0
    for  i in range(len(lista1)):
        resultado += lista1[i] * lista2[i]

    print(f"El producot escalar de las dos es {resultado}")


producto_escalar()