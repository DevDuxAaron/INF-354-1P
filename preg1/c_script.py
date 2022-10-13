import matplotlib.pyplot as plt

def leer_columna_csv(n_columna,archivo):
    with open(archivo, 'r') as f:
        datos = []
        for line in f:
            columnas = line.split(',')
            datos.append(columnas[n_columna])
        return datos

preguntas=["buying","maint","doors","persons","lug_boot","safety","ClassValues"]
columnas=[0,1,2,3,4,5,6]

for i in range(len(preguntas)):
    datos=leer_columna_csv(columnas[i],"car_data.csv")
    datos.pop(0)
    datos=[float(i) for i in datos if isinstance(i, float) or (isinstance(i, str) and i.isnumeric())]
    datos=sorted(datos)
    bins = 100
    plt.hist(datos, bins, (0,6), color = 'green', histtype = 'bar', rwidth = 0.8)
    plt.xlabel('Caracteristica')
    plt.ylabel("Cantidad")
    plt.title(preguntas[i], loc='center', wrap=True)
    #plt.show()
    plt.savefig(preguntas[i]+'.png')