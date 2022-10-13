import math
import csv

def leer_columna_csv(n_columna,archivo):
    with open(archivo, 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        datos = []
        for line in csvreader:
            datos.append(line[n_columna])
        return datos

def grabar_datos_csv(datos,archivo):
    with open(archivo, 'w',newline='') as f:
        write = csv.writer(f)
        write.writerows(datos)

def filtrar_csv(archivo,columnas):
    datos=[]
    resultado=[]
    nd=0
    for i in range(len(columnas)):
        col=leer_columna_csv(columnas[i],archivo)
        datos.append(col)
        if(len(col)>nd):
            nd=len(col)
    for i in range(nd):
        row=[]
        for j in range(len(columnas)):
            row.append(datos[j][i])
        resultado.append(row)
    return resultado

def eliminar_nan(datos):
    datos=[int(i) for i in datos if isinstance(i, int) or (isinstance(i, str) and i.isnumeric())]
    datos=[i for i in datos if i>0]
    return datos

def normalizar(datos):
    media = float(sum(datos)) / float(len(datos))
    de = math.sqrt(sum(pow(x-media, 2) for x in datos) / len(datos))
    resultado = [(x-media)/de for x in datos]
    return resultado


preguntas=["buying","maint","doors","persons","lug_boot","safety","ClassValues"]
columnas=[0,1,2,3,4,5,6]

filtrado=filtrar_csv("car_data.csv",columnas)
grabar_datos_csv(filtrado,"filtrado.csv")

columnas=[0,1,2,3,4]

for i in range(len(preguntas)):
    datos=leer_columna_csv(columnas[i],"filtrado.csv")
    datos.pop(0) # quitamos el nombre de la columna
    print(preguntas[i])
    print("Datos Originales")
    print(datos)
    print("Eliminando datos no numéricos y ceros")
    print(eliminar_nan(datos))
    print("Normalizando datos")
    print(normalizar(eliminar_nan(datos)))