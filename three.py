'''Escreva um programa que leia duas estruturas (A e B) de 10 posições e faça a multiplicação dos
elementos de mesmo índice, colocando o resultado em uma terceira estrutura (C). Mostre os
elementos de C.'''

list_one = []
list_two = []
list_three = []

for i in range(0, 10):
    list_one.append(i * 2)
    list_two.append(i * 3)

print(list_one)
print(list_two)

for i in range(0, len(list_one)):
    list_three.append(list_one[i] * list_two[i])

print(list_three)