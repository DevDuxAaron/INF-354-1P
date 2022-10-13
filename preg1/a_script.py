def percent(datos,p):
    tam=len(datos)
    ordenado=sorted(datos)
    n=((p/100)*tam)
    n=round(n)
    elem=ordenado[n]
    return n,elem

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
    
    resp=percent(datos,25)
    print("Primer cuartil {0}:\t{1}\t posicion:\t{2}".format(preguntas[i], str(resp[1]), str(resp[0]) ))
    resp=percent(datos,90)
    print("Percentil 90 {0}:\t{1}\t posicion:\t{2}".format(preguntas[i], str(resp[1]), str(resp[0]) ))
    resp=percent(datos,95)
    print("Percentil 95 {0}:\t{1}\t posicion:\t{2}".format(preguntas[i], str(resp[1]), str(resp[0]) ))
    print()