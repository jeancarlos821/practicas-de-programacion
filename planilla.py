#Calculo de horas laboradas en el mes por la tarifa por horas
#El proposito es obtener el salario mensual
#empleado 1 N B/2.77
#empleado 2 S B/2.91

import math

print("Empleado No 1 N: ")
dias = float(input("ingrese el numero de dias laborados: "))
horas = 8
costo = 2.77

print("Salario mensual: B/", (dias*horas*costo))

salario_Emp_1= (dias*horas*costo)

print("Empleado No 2 S: ")
dias = float(input("ingrese el numero de dias laborados: "))
horas = 8
costo = 2.91

print("Salario mensual: B/", (dias*horas*costo))

salario_Emp_2= (dias*horas*costo)

Riesgos_Prof = (salario_Emp_1+salario_Emp_2)*float(0.0098)
Seguro_Edu = (salario_Emp_1+salario_Emp_2)*float(0.0275)
Seguro_Social = (salario_Emp_1+salario_Emp_2)*float(0.36656)

print("cuota mensual CSS: ",(Riesgos_Prof+Seguro_Edu+Seguro_Social))

