'''Ler e armazenar 30 elementos inteiros em uma estrutura composta. Encontre e mostre o menor
elemento e a sua posição.'''

list_one = []
for i in range(0, 30):
    list_one.append(i+3)

list_one[0] = 12
print(list_one)

position = 0
minimum = 0

for i in range(0, 30):
    minimum = min(list_one)
    position = list_one.index(minimum)

print("Menor elemento: ", minimum)
print("Posição: ", position)
