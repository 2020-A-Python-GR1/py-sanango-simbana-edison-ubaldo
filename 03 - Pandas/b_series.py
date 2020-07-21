#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:41 2020

@author: edison
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3]
tupla_numeros = (1,2,3)
np_numeros = np.array([1,2,3])

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)

series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "EDISON",
    None,
    (1),
    [2],
    {"nom":"Edison"}])


print(series_d[len(series_d)-1]) # Accede al último


ciudades = ['Quito', 'Cuenca', 'Ambato', 'Baños']

series_ciudad = pd.Series(ciudades, index=["Q", "C", "A", "B"])

print(series_ciudad[3])

valores_ciudad = {
    "Ibarra": 100,
    "Guayaquil": 200,
    "Cuenca": 300,
    "Quito": 400,
    "Loja": 500
}
# index = ["Ibarra", "Guayaquil", "CUenca", "Quito", "Loja", "A"]
series_Valor_ciudad = pd.Series(valores_ciudad)


ciudades_menor_a_300 = series_Valor_ciudad < 300    # Esto retorna una serie con valores de verdadero y falso
ciudades_menor_a_300 = series_Valor_ciudad[series_Valor_ciudad < 300] # Se filtra solo los que cumplen con la condición

print(type(series_Valor_ciudad))
print(type(ciudades_menor_a_300))
print(ciudades_menor_a_300)


mas_10_porciento = series_Valor_ciudad * 1.1

series_Valor_ciudad["Quito"] = series_Valor_ciudad["Quito"] - 20


#print(series_Valor_ciudad)

for i in series_Valor_ciudad:
    print(i) # imprime solo el valor



svc_cuadrado = np.square(series_Valor_ciudad)

ciudades_uno = pd.Series({
    "Cuenca": 300,
    "Zamora": 500,
    "Quito": 100})


ciudades_dos = pd.Series({
    "Guayaquil": 700,
    "Loja": 1000,
    "Baños": 100})


ciudades_uno["Loja"] = 0


print(ciudades_uno + ciudades_dos)

# o también

ciudades_add = ciudades_uno.add(ciudades_dos)

# verificar que no haya elemento repetido entre dos series.
ciud_concat = pd.concat([ciudades_uno, ciudades_dos],verify_integrity= False)

# append
ciud_append = ciudades_uno.append(ciudades_dos,verify_integrity= False)

print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))


print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))



# Funciones de estadística

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))


# ordenar

ciudades_uno.sort_values(ascending = False)
ciudades_uno.sort_values(ascending = True)


# 0- 100 - 5%
# 101 - 300 - 10%
#301 - 500 - 15%

print(ciudades_uno)


def calcular(valor_serie):
    if(valor_serie <= 100):
        return valor_serie * 1.05
    if(valor_serie > 100 and valor_serie <= 300):
        return valor_serie * 1.10
    if(valor_serie > 300 and valor_serie <= 500):
        return valor_serie * 1.15

resultado = ciudades_uno.map(calcular)
print(resultado)


# WHERE
# Cuando NO CUMPLE la condición, se aplica
print(ciudades_uno)
print(ciudades_uno.where(ciudades_uno < 300, ciudades_uno * 1.15))


# PROBLEMAS CON TIPOS DE DATOS 
series_numeros = pd.Series(['1.0', '2', -3])

print(pd.to_numeric(series_numeros))
print(pd.to_numeric(series_numeros, downcast= 'integer'))


series_numeros_err = pd.Series(['1.0', '2', -3, 'a'])
# errors = ignore, coerce, raise (default)
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerce'))







