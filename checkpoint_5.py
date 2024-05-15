
for saludar in range(1,3):
  print("Hola")



def suma(arg_1, arg_2, arg_3):
  return arg_1 + arg_2 + arg_3
  
resultado = suma(1,2,3)
print(resultado)

otra_suma = lambda arg_1, arg_2, arg_3: arg_1 +arg_2 + arg_3
print(otra_suma(1,2,3))



nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']


if nombre in lista_nombre:
  print(f'el nombre {nombre} esta en la lista')
else:
  print(f'el nombre {nombre} no esta en la lista')
