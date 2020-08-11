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





































