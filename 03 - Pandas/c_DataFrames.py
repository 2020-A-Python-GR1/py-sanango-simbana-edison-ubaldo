#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:46:56 2020

@author: edison
"""


import numpy as np
import pandas as pd

arreglo = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arreglo)

s1 = df1[0]

s2 = df1[1]

s3 = df1[2]

df1[3] = s1 + s2

df1[4] = s1 * s2

s = df1[[0,3]] # selecciona varias columnas


datos_fisicos_uno = pd.DataFrame(
    arreglo,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)']) # Con esto se renombra a las columnas


datos_fisicos_dos = pd.DataFrame(
    arreglo,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'],
    index = [
        'Edison',
        'Locoqueama']) # Con esto se renombra a las columnas

# para acceder a un valor específcio
print(datos_fisicos_dos['Peso (kg)']['Edison'])
print(datos_fisicos_dos.iloc[0])


# modificar los índices

df1.index = ['Ubaldo', 'otroloco']
df1.columns = ['A', 'B', 'C', 'D', 'E']




