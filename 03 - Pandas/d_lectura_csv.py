#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:38 2020

@author: edison
"""

import pandas as pd

path = "./data/artwork_data.csv"
data = pd.read_csv(path, nrows=10)

columnas = ['id', 'artist','title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

data = data[columnas]

# se puede setear un índice de cualquiera de las dos formas
data = data.set_index('id')
data1 = pd.read_csv(path, nrows=10, index_col ='id')


path_guardado = "./data/artwork_data.pickle"
data1.to_pickle(path_guardado)

leer_guardado = pd.read_pickle(path_guardado)