tpl = tuple()
brothers = ('Angel', 'Pablo', 'Beny')
sisters = ('Valeria', 'Andrea', 'Valentina')
print(brothers)
print(sisters)
siblings = brothers + sisters
print(siblings)
siblings = list(siblings)
print('Tengo un total de: ', len(siblings), 'hermanos')
siblings.append('Hector')
mom = 'Maria'
siblings.append(mom)
family_members = tuple(siblings)
print(family_members)

# Level 2
bro_1, bro_2, bro_3, sis_1,sis_2,sis_3,father,mother = family_members
print('El primer hermano y la primera hermana son:', bro_1, 'y', sis_1)
print('Los padres son:', father, 'y', mother)

fruits = ('manzana', 'naranja', 'patilla')
vegetables = ('brocoli', 'zanahoria', 'coliflor')
animal = ('pollo', 'solomo', 'queso')
comida = fruits + vegetables + animal
print('La comida disponible para ordenar es:', comida)
comida_lt = list(comida)
print(len(comida))
print(comida_lt[0:3])
print(comida_lt[-3::1])
print(comida[len(comida)//2])
del comida

# FIN
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia es un pais nordico?", 'Estonia' in nordic_countries)
print("Islandia es un pais nordico?", 'Iceland' in nordic_countries)