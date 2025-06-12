def esta_ordenada():
    lista = list(map(int, input("Ingresa la lista: ").split()))

    ordenada = True
    for  i in range(len(lista) - 1):
        if lista [i] > lista[i + 1]:
            ordenada = False
            break


    if ordenada:
        print("La lista esta ordenada")
    else:
        print("La lista no esta ordenad")

esta_ordenada()