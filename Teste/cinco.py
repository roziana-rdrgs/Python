altura = float(input("Altura: "))
peso = float(input("Peso: "))
sexo = input("Sexo: ")
peso_ideal = 0

if sexo == "F":
    peso_ideal = (62.1 * altura)-44.7
elif sexo == "M":
    peso_ideal = (72.7 * altura)-58
else:
    print("Informação inválida.")

if peso > peso_ideal:
    dif = peso - peso_ideal
    print("Você está %.2f kg acima do peso ideal, que é de %.2f :" %(dif, peso_ideal))
elif peso_ideal > peso:
    dif = peso_ideal - peso
    print("Você está %.2f kg abaixo do peso ideal, que é de %.2f :" %(dif, peso_ideal))
else:
    print("Parabéns, você está no seu peso ideal, %.2f kg" %peso_ideal)