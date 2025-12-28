# Como ya se hacia engorroso siempre rellenar datos, hice otro archivo para los ejercicios restantes
# Calcular salario dado pago por hora y horas de trabajo
horas_pautadas = int(input('Indique las horas de trabajo semanal: '))
pago_por_hora = float(input('Indique el pago por hora asignado: '))
salario_semanal = horas_pautadas*pago_por_hora
salario_mensual = salario_semanal*4
salario_anual = salario_mensual*12

print("Dados los datos, el salario semanal es de:", salario_semanal, '$')
print('El salario mensual es de:', salario_mensual, '$')
print('El salario anual es de:', salario_anual, '$')

# Calcular segundos vividos segun año dado y segundos por vivir
año = int(input("Cuantos años tienes? "))
segundos_vividos = año*365*24*60*60
segundo_por_vivir = (100*365*24*60*60)-segundos_vividos
print('Has vivido: ', segundos_vividos, 'segundos')
print('Te quedan por vivir', segundo_por_vivir, 'segundos')
print('Valoras cada segundo que pasa? Piensalo')

# Desplegar tabla de potencias, elevado a la 0, 1, 2 y 3
num1, num2, num3, num4, num5 = 1,2,3,4,5
print(num1, num1**0, num1**1, num1**2, num1**3)
print(num2, num2**0, num2**1, num2**2, num2**3)
print(num3, num3**0, num3**1, num3**2, num3**3)
print(num4, num4**0, num4**1, num4**2, num4**3)
print(num5, num5**0, num5**1, num5**2, num5**3)