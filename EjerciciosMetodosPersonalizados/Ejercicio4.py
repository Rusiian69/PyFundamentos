def cuadrados_lista():
    numero = int(input("Cuantas cuadrados querras: "))
    lita = []
    for i in range(1, numero + 1):
        lita.append(i ** 2)
    
    print(f"los cuadrados de los numeros naturales primeros son {lita}")


cuadrados_lista()