for numero in range(1000,9999):

    parte_um = numero // 100
    parte_dois = numero % 100
    
    soma = parte_um + parte_dois
    quadrado = soma * soma

    if numero == quadrado:
        print(str(numero) + " -> dividindo: " + str(parte_um) + ", " + str(parte_dois) + " -> somando: " + str(soma) + " -> ao quadrado: " + str(quadrado))

    numero += 1