#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:05:50 2020

@author: edison
"""

# loc

import pandas as pd

path_pickle = './data/artwork_data.pickle'

df = pd.read_pickle(path_pickle)

primero = df.loc[1035] # es el indice y jala todo un registro - retorna SERIE

print(primero['artist']) # retorna solo el string

print(primero.index) # indices son las columnas del df original




df_1035 = df[df.index == 1035] # se filtra solo por el indice del dataframe}
# y retorna otro dataframe es como hacer un split y solo quedarse con ese.


grupo = df.loc[[1035,1039]]

grupo2 = df.loc[1035,['artist','medium']] # varios indices - retorna SERIES



# ILOC


fila = df.iloc[0] # Serie

fila1 = df.iloc[[0,1]] # dataframe

fila2 = df.iloc[0:10] # dataframe

fila3 = df.iloc[df.index == 1035] # dataframe


fila4 = df.iloc[0:10, 0:2] # rango de filas, rango de columnas .dataframe



#################################################################

import pandas as pd

datos = {
    "nota 1":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria":9},
    "nota 2":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria":9},
    "disciplina":{
        "Pepito": 4,
        "Juanita": 9,
        "Maria":2}
    }

notas = pd.DataFrame(datos)


condicion_nota = notas["nota 1"] > 7
condicion_disc = notas["disciplina"] > 7
condicion_nota_2 = notas["nota 2"] > 6
mayores_siete = notas.loc[condicion_nota, ["nota 1"]]
buena_disciplina = notas.loc[condicion_disc, ["disciplina"]]

pasaron = notas.loc[condicion_nota][condicion_disc][condicion_nota_2]

# para actualizar valores
notas.loc["Maria", "disciplina"] = 5
notas.loc[:,"disciplina"] = 7

# Promedio de las 3 notas 

nota_1_mean = notas.loc[:,"nota 1"].mean()
nota_2_mean = notas.loc[:,"nota 2"].mean()
disiciplina_mean = notas.loc[:,"disciplina"].mean()


mean_total = (nota_1_mean + nota_2_mean + disiciplina_mean) / 3



notas["promedio"] = (notas.loc[:,"nota 1"] + notas.loc[:,"nota 2"] + notas.loc[:,"disciplina"])/3










