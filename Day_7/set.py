# Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))
print(it_companies)
it_companies.add('Twitter')
more_it_companies = {'Nintendo', 'Sony', 'Tencent'}
it_companies.update(more_it_companies)
print(it_companies)
it_companies.remove('Facebook')
# La diferencia entre remove y discard es que remove elimina un elemento dado,
# Cuando no se encuentra genera un error, mientras que discard lo elimina, pero si no lo encuentra
# No Genera un error. Siendo discard() mejor para casos generales, pero remove()
# Mejor para casos especificos donde queramos que se nos notifique si NO existe el elemento dado y tratar ese error
it_companies.discard('Dell')
# it_companies.remove('Dell') # KeyError: 'Dell'
print(it_companies)
print(len(it_companies))

# Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(A)
print(A.intersection(B)) 
print(A.issubset(B)) # True, se iguales o menos elementos iguales que el superset
print(A.isdisjoint(B)) # False, porque comparten elementos
# La diferencia simetrica entre conjuntos son los elementos totales de AMBOS conjuntos sumados,
# Excluyendo a los elementos que comparte (union), sea A.symmetric_difference(B) o B.A.symmetric_difference(A)
# Daran el mismo resultado, cosa que no ocurre con una .difference() usual
print(A.difference(B)) # Ninguna
print(B.difference(A))
A.add(1) # Para ejemplificar mejor
print(A.symmetric_difference(B))
print(B.symmetric_difference(A)) # Igual a la anterior

# Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Es mas largo el conjunto o la lista?", len(age) > len(age_set)) # La lista es mas larga... porque el set elimina los repetidos como 24, 24 y 25, reduciendo en 3 su tamaño, de 8 a 5 elementos
'''
De base los 4 tipos de informacion: string, list, tuple y set son grupos de n elementos
String, es un grupo de caracteres concatenados uno despues de otro formando un texto.
List, es un grupo de elementos alterables y ordenados, es un grupo variable.
Tuple, es un grupo de elementos constantes y ordenados, es un grupo variable (porque se pueden eliminar o agregar elementos,pero no alterar, menos flexible que una List)
Set, es un conjunto de elementos constantes, desordenados y unicos (irrepetibles), es un grupo variable (se pueden eliminar o agregar elementos, pero no alterar o ubicar)
'''
string = "I am a teacher and I love to inspire and teach people"
string_list = list(string.split(' '))
print(len(string_list))
string_set = set(string.split(' '))
print(len(string_set))
print(string_set)
print('Hay', len(string_list), 'palabras en la oracion total, pero solo', len(string_set), 'son palabras unicas, es decir hay', len(string_list)-len(string_set), 'palabras repetidas')