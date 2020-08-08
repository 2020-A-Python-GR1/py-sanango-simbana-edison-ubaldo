# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import os 
import sqlite3

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# TIPOS DE ARCHIVOS



# EXCEL

path_excel_indice = "./data/artwork_data_indice.xlsx"
sub_df.to_excel(path_excel_indice,index=False)

columnas = ['artist','title','year']
path_excel_columnas = "./data/artwork_data_columnas.xlsx"
sub_df.to_excel(path_excel_columnas,columns =columnas)

# multiples spreadsheets

path_excel_mt = "./data/artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt,engine='xlsxwriter')
sub_df.to_excel(writer,sheet_name='Primera')
sub_df.to_excel(writer,sheet_name='Segunda')
sub_df.to_excel(writer,sheet_name='Tercera')
writer.save()


# Formato condicional
path_excel_colores = "./data/artwork_data_colores.xlsx"

num_artistas = sub_df['artist'].value_counts()
print(num_artistas)
writer = pd.ExcelWriter(path_excel_colores,engine='xlsxwriter')

#series
num_artistas.to_excel(writer, sheet_name='Artistas')

# seleccionando la hoja de trabajo

hoja_artistas = writer.sheets['Artistas']
rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)


# establecer formato esto está en la documentación

formato_artistas = {
    "type": "2_color_scale",
    "min_value": "10",
    "min_type": "percentile",
    "max_value": "99",
    "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,formato_artistas)
writer.save()


#### SQL 


with sqlite3.connect("data/bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas',conexion) # es la tabla


############ JSON

sub_df.to_json('data/artistas.json')

sub_df.to_json('artistas_tabla.json', orient= 'table')

