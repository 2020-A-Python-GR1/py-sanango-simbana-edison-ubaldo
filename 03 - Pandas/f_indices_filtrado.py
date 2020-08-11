#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:43:12 2020

@author: edison
"""

import pandas as pd


path_pickle = './data/artwork_data.pickle'

df = pd.read_pickle(path_pickle)

# encontrar registros únicos
artistas_no_duplicados = pd.unique(df['artist'])
#print(type(artistas_no_duplicados)) # numpy array

# para ver el tamaño
#print(artistas_no_duplicados.size)

# para saber específicamente cuantos de un artista

blake = df[df['artist'] == 'Blake, William'] # es un Dataframe




