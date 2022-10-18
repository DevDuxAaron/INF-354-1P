import numpy as np
import pandas as pd

preguntas=[
    "edad",
    "trabajo",
    "estado",
    "educacion",
    "default",
    "balance",
    "housing",
    "deuda",
    "contacto",
    "dia",
    "mes",
    "duracion",
    "campaña",
    "pdays",
    "previous",
    "poutcome",
    "y"]
columnas=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
percentiles=[25,90,95]

df=pd.read_csv("bank.csv")

for i in range(len(preguntas)-1):
    datos=df.iloc[:,columnas[i]]
    resp=np.percentile(datos,percentiles)
    print("Primer cuartil {0}:\t{1}".format(preguntas[i], str(resp[0]) ))
    print("Percentil 90 {0}:\t{1}".format(preguntas[i], str(resp[0]) ))
    print("Percentil 95 {0}:\t{1}".format(preguntas[i], str(resp[0]) ))