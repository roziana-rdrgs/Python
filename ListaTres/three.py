
element = int(input("Primeiro elemento da progressão: "))
ratio = int(input("Razão: "))

print("Progressão Aritmética: ")
for i in range(0, 10):
    element += ratio
    print(element)
