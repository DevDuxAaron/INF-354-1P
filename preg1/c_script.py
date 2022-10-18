import matplotlib.pyplot as plt

def leer_columna_csv(n_columna,archivo):
    with open(archivo, 'r') as f:
        datos = []
        for line in f:
            columnas = line.split(',')
            datos.append(columnas[n_columna])
        return datos

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
columnas=[0,9,12,13,14]
# columnas=[0,5]

# datos=leer_columna_csv(5,"bank.csv")
# print(datos)

for i in range(len(columnas)):
    print("Mostrando",columnas[i],"columna")
    datos=leer_columna_csv(columnas[i],"bank.csv")
    datos.pop(0)
    datos=[float(i) for i in datos if isinstance(i, float) or (isinstance(i, str) and i.isnumeric())]
    datos=sorted(datos)
    bins = 20
    plt.hist(datos, bins, (min(datos),max(datos)), color = 'blue', histtype = 'bar', rwidth = 0.8)
    plt.xlabel(preguntas[columnas[i]])
    plt.ylabel("Cantidad")
    plt.title(preguntas[columnas[i]], loc='center', wrap=True)
    # plt.show()
    plt.savefig(preguntas[i]+'.png')