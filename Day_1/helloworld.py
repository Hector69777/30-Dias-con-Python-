# La version de Python se mostrara en el terminal
# Operandos seran 3 y 4, para realizar suma, resta, multiplicacion, division, potenciacion
print(3+4) # Suma
print(3-4) # Resta
print(3*4) # Multiplicacion
print(3%4) # Modulo
print(3/4) # Division
print(3**4) # Potenciacion
print(3//4) # Division Exacta

# Cadenas de Texto
print('Hector') # Nombre
print('Barrios') # Apellido
print('Venezuela') # Pais
print('Estoy disfrutando este inicio de 30 dias de Python') # Holaa

# Type de elementos
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Hector', 'Python', 'Venezuela']))
print(type('Hector'))
print(type('Barrios'))
print(type('Venezuela'))

# Ejemplos de uso de diferentes tipos de datos
print('\n')

print(2+2, type(2+2))
print(2/2, type(2/2))
print((1+3j)/2, type((1+3j)/2))
print('Hola Mundo!', type('Hola Mundo!'))
print(True, type(True))
print(['Maria', 'Hector', 'Valeria'], type(['Maria', 'Hector', 'Valeria']))
print((12,24), type((12,24)))
print({1, 2, 3, 5, 7, 11, 13}, type({1, 2, 3, 5, 7, 11, 13})) # Conjunto de numeros primos
print({'Tlf': 424, 'Pais': 'Venezuela'}, type({'Tlf': 424, 'Pais': 'Venezuela'})) # Diccionario simple

# Obtener distancia euclidiana entre los puntos (2,3) y (10,8)

print("\n La distancia euclidiana entre los puntos (2,3) y (10,8) es: ")
print(((10-2)**2) + ((8-3)**2)) # Esta es la distancia al cuadrado
print("Esta es la distancia elevada al cuadrado, se debe obtener la raiz cuadrada para conseguir la distancia")
print('En este caso seria mas o menos: 9.44 unidades')