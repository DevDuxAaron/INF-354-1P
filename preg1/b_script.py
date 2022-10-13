import numpy as np
import pandas as pd

preguntas=["buying","maint","doors","persons","lug_boot","safety","ClassValues"]
columnas=[0,1,2,3,4,5,6]
percentiles=[25,90,95]

df=pd.read_csv("car_data.csv")

for i in range(len(preguntas)):
    datos=df.iloc[:,columnas[i]]
    resp=np.percentile(datos,percentiles)
    print("Primer cuartil {0}:\t{1}".format(preguntas[i], str(resp[0]) ))
    print("Percentil 90 {0}:\t{1}".format(preguntas[i], str(resp[0]) ))
    print("Percentil 95 {0}:\t{1}".format(preguntas[i], str(resp[0]) ))