# 01 - 03, ejercicios de diccionarios
dog = dict()
print(dog)
dog['nombre'], dog['color'], dog['raza'], dog['piernas'], dog['edad']  = 'Benny', 'Marron', 'Salchicha', 4, 5
print(dog)

# Student
student = {
    'primer_nombre':'Pablo',
    'apellido': 'Astorga', 
    'genero': 'Masculino', 
    'edad': 20, 
    'esta_casado': False, 
    'habilidades': ['Excel', 'Powerpoint', 'Docs', 'PowerBI'],
    'pais': 'Venezuela',
    'ciudad': 'Barcelona',
    'direccion': {
        'calle': 'Libertad',
        'codigo_postal': 661,
    }}

print(student['ciudad'])

# 04 - 06
print(len(student))
print(student.get('habilidades'),'\n', type(student['habilidades']))
nuevas_habilidades = 'HTML', 'CSS'
student['habilidades'].extend(nuevas_habilidades)
print(student['habilidades'])

# 07 - 11 FIN
keys = student.keys()
values = student.values()
list = student.items()
print(student.items())
print(student)

del student['direccion']
del dog
print(student)
# print(dog) # Error, not defined