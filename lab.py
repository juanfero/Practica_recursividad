# Juan Felipe Rojas
# Universidad Sergio Arboleda
# Laboratorios Practica. 


def repeticion (arreglo):
  arreglo.sort()
  
  if arreglo [i] == 0:
    return 0
  else:
    return repeticion
    
  
  repeticion()
# primer punto 
print('!laboratorio estructura de datos¡ ')
print('ejercicio 1')
numeros=[1,7,8,9,8,1]
item_7=7
item_1=1
item_8=8
item_9=9

result=numeros.count(item_1)
print('hay =>', result)
result=numeros.count(item_9)
print('hay =>', result)


print('ejercicio 2 ')

impar_numbers=0
even_numbers = 0

for number in numeros:
  if number % 2 == 0:
    even_numbers+= number
  else:
    impar_numbers+=number

print(even_numbers)
print(impar_numbers)

print('ejercicio 3')

n=int(input('ingrese el tamaño del arreglo'))
list=[]
list_2=[]




print('ejercico 4')

def find_positions(A, X):
    positions = []
    for i, num in enumerate(A):
        if num == X:
            positions.append(i)
    return positions

A = [1, 2, 3, 4, 5, 1, 2, 3, 4]
X = 2
print(find_positions(A, X))

print('ejercicio 5')

n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = []
arreglo2 = []
for i in range(n):
    arreglo.append(int(input("ingrese el numero {}: ".format(i + 1))))
  ## ormat nos permite incluir en una cadena, texto ordinario y caracteres de formateo, que representan un tipo en particular de datos, tales como entero, cadena o flotante
  

'''
for i in range(n-1):
    arreglo2.append(arreglo[i]-arreglo[i+1])

print(arreglo2)
'''
def find_positions(A, x):
  positions = []
  for i, a in enumerate(A):
    if a == x:
      positions.append(i)
    return positions
find_positions()
