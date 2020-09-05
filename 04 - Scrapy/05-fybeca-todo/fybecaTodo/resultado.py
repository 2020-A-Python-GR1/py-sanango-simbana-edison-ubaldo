#dataframe_final = pd.concat(self.lista_final)

import pandas as pd 


columns = columns=['Productos','Imagen','Precio normal', 'Precio miembro','Diferencia precios']
dataframe_final = pd.read_csv("./05-fybeca-todo/fybecaTodo/fybecaTodo/spiders/data.csv",names=columns)
dataframe_final = dataframe_final.reset_index(drop=True)
print(dataframe_final.head(10))

# cual es el item con mayor y menor precio -- por precio normales
mayor_precio = dataframe_final.iloc[dataframe_final['Precio normal'].idxmax()]
print("ITEM CON MAYOR PRECIO NORMAL:")
print(mayor_precio)

menor_precio = dataframe_final.iloc[dataframe_final['Precio normal'].idxmin()]
print("ITEM CON MENOR PRECIO NORMAL:")
print(menor_precio)

# cuanto ahorramos si compramos todo como afiliado
ahorrado = dataframe_final.sum()
print("AL COMPRAR COMO AFILIADO SE AHORRA:{}".format(ahorrado['Diferencia precios']))
