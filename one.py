'''
Escreva um programa que leia e mostre em uma estrutura composta 20 elementos inteiros. A
seguir, conte quantos valores pares existem.
'''
list1 = []
i = 0
count = 0
for i in range(0, 10):
    list1.append(int(input('Informe o %d° elemento: ' %(i+1))))
    i += 1
print(list1)

for item in list1:
    if item%2 == 0:
       count += 1

print("Quantidade de elementos pares: %d" %count)
