def primo():
    num = int(input("Ingresa un numero: "))

    if num <= 2:
        print("no es primo")
        return
    
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("es primo")
    else:
        print("NO ES primo")


primo()