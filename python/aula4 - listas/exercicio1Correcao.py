numeros = [5, 8 , 2 , 9 ,1]

# b)
# 2 metodo
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

# 1 metodo
# for numero in numeros:
#     if numero > maior:
#         maior = numero

# c)
numeros.append(7)
numeros.insert(2 , 3)
print(numeros)

# d)
# 1 metodo
# del numeros[1]
# numeros.insert(10,1)

# 2 metodo
numeros[1] = 10
print(numeros)

# e)
del numeros[4]
del numeros[3]
del numeros[2]
print(numeros)