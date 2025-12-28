# Dia 2 de los 30 dias programando con Python!
primer_nombre = 'Hector'
apellido = 'Barrios'
nombre_completo = 'Hector Barrios'
pais = 'Venezuela'
ciudad = 'Barcelona'
edad = 21
año = 2025
esta_casado = False
es_verdadero = True
esta_luz_prendida = True
año_nacimiento, semestre_universitario, esta_contratado, carrera = 2004, 7.3, False, 'Ingenieria de Sistemas'

# Determinar tipo de variables
print(type(primer_nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(esta_casado))
print(type(es_verdadero))
print(type(esta_luz_prendida))
print(type(año_nacimiento))
print(type(semestre_universitario))
print(type(esta_contratado))
print(type(carrera))

# Longitud del primer nombre
print(len(primer_nombre))
longitud_primer_nombre = len(primer_nombre)
longitud_apellido = len(apellido)
comparativa_de_longitudes = longitud_primer_nombre - longitud_apellido
print(' El primer nombre tiene una longitud de:', longitud_primer_nombre, 'caracteres\n', 'Mientras que el apellido tiene una longitud de:', longitud_apellido, 'caracteres\n', 'Hay una diferencia de:', comparativa_de_longitudes, 'caracteres entre ambos, en relacion nombre-apellido')

# Numeros
numero_uno = 5
numero_dos = 4
total = numero_uno + numero_dos
diferencia = numero_dos - numero_dos
producto = numero_uno * numero_dos
division = numero_uno / numero_dos
residuo = numero_dos % numero_uno
potencia = numero_uno ** numero_dos
division_exacta = numero_uno // numero_dos

# Circulo
print('\n')
radio = 30
area_del_circulo = 3.1416*(radio**2)
circunferencia_del_circulo = 3.1416*(radio*2)
print('La area de un circulo de radio 30mts es de', area_del_circulo, 'mts cuadrados')
print('La circunferencia de un circulo de radio 30mts es de', circunferencia_del_circulo, 'mts')

print('\n')
radio = int(input('Ingrese el radio del circulo a medir: '))
area_del_circulo = 3.1416*(radio**2)
circunferencia_del_circulo = 3.1416*(radio*2)
print('La area de un circulo de radio', radio, 'mts es de', area_del_circulo, 'mts cuadrados')
print('La circunferencia de un circulo de radio', radio, 'mts es de', circunferencia_del_circulo, 'mts')

print("\nIngrese sus datos")
primer_nombre = input("Primer nombre ")
apellido = input("Apellido ")
pais = input("Pais ")
edad = input("Edad ")

print("Te llamas:", primer_nombre, apellido, 'Eres de:', pais, 'y tienes', edad, 'años.')

help('keywords')