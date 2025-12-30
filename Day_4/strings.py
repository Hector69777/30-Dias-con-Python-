# 01
string_1 = 'Treinta '
string_2 = 'Dias '
string_3 = 'De '
string_4 = 'Python'
string_complete = string_1 + string_2 + string_3 + string_4
print(string_complete)

# 02
string_1 = 'Codigo'
string_2 = 'Para'
string_3 = 'Todos'
space = ' '
string_complete = string_1 + space + string_2 + space+  string_3
print(string_complete)

# 03 - 07

company = "Coding For All"
print(company)
print('Longitud de la oracion:', len(company), 'caracteres')
company_upper = company.upper()
company_lower = company.lower()
print(company_upper)
print(company_lower)
# 08
print('\n--- Capitalize, title y swapcase ---\n')
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 09
coding = company[0:6]
print(coding)

# 10
print(company.find('Coding'))
print(company.index('For'))

# 11
print(company.replace('Coding', 'Python'))

# 12
company_python = company.replace('Coding', 'Python')
company_alt = 'Python For Everyone'
for_all = 'For All'
print(company_alt.replace('For Everyone', for_all))

# 13 y 14
print(company.split(' '))
redes = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(redes.split(','))
print(redes.split(',')[1])

# 15 - 17
print(company[0]) # Primer caracter
print(company[-1]) # Ultimo caracter
print(company[10], '---(Es un espacio en blanco)') # Es un espacio en blanco
print(company[11])
# 18 - 22
print('\n--- Acronimos, index y rfind ---\n')
print(company_alt[0]+ company_alt[company_alt.find('F')]+company_alt[company_alt.find('E')])
print(company[0]+company[company.index('F')]+company[company.index('A')])
print('Primera vez que aparece "C": ', company.index('C'))
print('Primera vez que aparece "F": ', company.index('F'))
print(company.rfind('l'))

# 23 - 27
print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
print(len('because'))
print('You cannot end a sentence with because because because is a conjunction'[31:47+(len('because'))])
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'[31:47+7])

# 28 y 29
print(company.startswith('Coding'))
print(company.endswith('coding'))

# 30
company_space = '   Coding For All      '
print(company_space.strip(' ') + '-')

# 31, la segunda variable retornara True, es un nombre valido
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print('Thirty_days_of_python'.isidentifier())
# 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'+' #'.join(libraries))
# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34, 35, 36, FIN

print('Name\t    Age\tCountry\tCity'.expandtabs(12))
print('Asabeneh\t250\tFinland\t    Helsinki')

radio = 10
area = 3.14 * radio ** 2
print("El area del circulo con radio {} es {} metros cuadrados".format(radio, area))
num_1 = 8
num_2 = 6
print('\nAqui se mostraran %s \nEn total %d operaciones:'%('Operaciones matematicas', 7))
print(f'{num_1} + {num_2} = {num_1+num_2}')
print(f'{num_1} - {num_2} = {num_1-num_2}')
print(f'{num_1} * {num_2} = {num_1*num_2}')
print(f'{num_1} / {num_2} = {num_1/num_2:.2f}')
print(f'{num_1} % {num_2} = {num_1%num_2}')
print(f'{num_1} // {num_2} = {num_1//num_2}')
print(f'{num_1} ** {num_2} = {num_1**num_2}')