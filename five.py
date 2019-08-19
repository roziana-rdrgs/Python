'''Escreva um algoritmo que armazene 20 valores em uma estrutura composta. Em seguida, troque
o primeiro elemento com o último, o segundo com o penúltimo, o terceiro com o antepenúltimo e
assim sucessivamente. Mostre os valores depois da troca.'''

list_one = []

for i in range(0,20):
    list_one.append(i)

print(list_one)

list_one.reverse()
print(list_one)