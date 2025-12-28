edad = 21
altura = 1.83
emociones = 1.5+1.5j

# Calcular area de un triangulo
base = int(input('Introduce la base del triangulo: '))
altura = int(input('Introduce la altura del triangulo: '))
area_triangulo = base*altura/2
print("El area del triangulo es:", area_triangulo, 'unidades')

# Calcular perimetro del triangulo
lado_a = int(input('Introce la longitud del lado A del triangulo: '))
lado_b = int(input('Introce la longitud del lado B del triangulo: '))
lado_c = int(input('Introce la longitud del lado C del triangulo: '))
perimtero_triangulo = lado_a + lado_b + lado_c
print("El perimetro del triangulo dado es: ", perimtero_triangulo, 'unidades')

# Calcular area y perimetro del rectangulo
alto_rectangulo = int(input("Introduce la altura del rectangulo: "))
ancho_rectangulo = int(input("Introduce la anchura del rectangulo: "))
area_rectangulo = alto_rectangulo*ancho_rectangulo
perimetro_rectangulo = 2*(alto_rectangulo+ancho_rectangulo)

print("El Area del rectangulo dado es de:", area_rectangulo, 'unidades cuadradas')
print('El Perimetro del rectangulo dado es de:', perimetro_rectangulo, 'unidades')

# Calcular area y circunferencia de un Circulo
radio = int(input('Ingrese el radio del circulo: '))
pi = 3.14
area_circulo = pi*radio**2
circunferencia = pi*radio*2
print("El area del circulo es:", area_circulo, 'unidades')
print('La circunferencia es de:', circunferencia, 'unidades')

# Calcular la pendiente
# y = 2x-2, dado que es una funcion lineal de la forma f(x) = mx + b, la pendiente es lo que acompaña a la x, entonces

x = 1
y = 2*x - 2 # La pendiente es 2, aunque no se como expresarlo en codigo
pendiente = 2

# Obtener pendiente entre dos puntos, (2,2) y (6,10)
x1,y1 = 2,2
x2,y2 = 6,10
pendiente_puntos = (y2-y1)/(x2-x1)
print('La pendiente por puntos (2,2) y (6,10) es:', pendiente_puntos)

print("Comparacion de pendientes:", pendiente == pendiente_puntos)

# Calcular valor de funcion f(x) o y dado n valores de x, se puede iterar, derivar, aplicar Bhaskara, tanteo, factorizacion, etc
# Por derivada la funcion y = x^2 + 6x + 9 nos da y' = 2x + 6, igualandola a 0 y despejando nos quedaria x = -3, es un valor donde y = 0
# Como no vamos a aplicar derivadas en este programa, ni bucles, ni raiz cuadrada (en Bhaskara), entonces sera por tanteo 

x = int(input("De un valor para que la funcion y = x^2 + 6x + 9 sea igual a 0! Obtenga un premio!: "))
y = x**2 + 6*x + 9
print("La funcion queda: ", y)
print("Tuviste razon?: ", y == 0)

# Comparasion falsa y verdadera
palabra_uno = 'python'
palabra_dos = 'dragon'
longitud_palabra_uno = len(palabra_uno)
longitud_palabra_dos = len(palabra_dos)
comparasion_falsa = longitud_palabra_uno > longitud_palabra_dos
print("Python es mas largo que Dragon?", comparasion_falsa)
print("'on' esta en", palabra_uno, 'y', palabra_dos, '?', ('on' in palabra_uno)and('on'in palabra_dos))

print('jargon' in 'I hope this course is not full of jargon')
print(('on' not in palabra_uno)and('on' not in palabra_dos))

longitud_palabra_uno_float = float(longitud_palabra_uno)
longitud_palabra_uno_string = str(longitud_palabra_uno_float)
print(longitud_palabra_uno_float, longitud_palabra_uno_string)

# Comprobar si un numero es par o no, divisible entre dos sin residuo
numero = int(input("Ingrese algun numero: "))
print('Tu numero es par?', numero%2 == 0)

# Comprobar divisiones exactas y divisiones truncadas
division = 7/3
division_truncada = int(division)
division_exacta = 7//3
print("Division:", division)
print("Division truncada:", division_truncada)
print("Division exacta:", division_exacta)
print("Comparativa:", division_exacta == division_truncada)

# Comprobacion de tipos
diez_str = '10'
diez_int = 10

print("Son diez y diez del mismo tipo?", type(diez_str) == type(diez_int)) # False

print("Comprobar si 9.8 truncado se rendodea a 10:", int(9.8) == 10)
print(int(9.8))