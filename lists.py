list2 = []
list2 = [1, 2, 3, 4.5, 'Linguagem', 'Python', [100, 200, 300]]
i = 0
print(list2[2])

print(list2[6][1])

print(list2[-2])

print(list2[1:6])

print(list2[0: 5: 2])

#exibe a lista de trás para frente
print(list2[::-1])

while i < len(list2):
    print(list2[i])
    i += 1

print(3 in list2)
print(9 in list2)
print('Linguagem' in list2)

for item in list2:
    print(item)

del(list2[0])

print(list2)

del(list2[0:3])
print(list2)

print(max(list2[2]))
print(min(list2[2]))

list2.append("Programação")
print(list2)

list2.append(list('Programação'))
print(list2)

list2.pop()
print(list2)

print(list2)

list2.clear()
print(list2)

list1 = [0, 5, 8, 9, 78, 10, 20]
print(list1)
