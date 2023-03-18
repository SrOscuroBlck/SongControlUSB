#Algoritmo de busqueda
def centinela(lista, buscado):
    value = False
    for i in range(0, len(lista)):
        if (lista[i][1] == buscado):
            value = True
            break
    return value

def functionB(listaSongs):

    #Ordenes
    band = "Audioslave"
    ValueBand = False
    #Llamado a algoritmo de busqueda
    ValueBand = centinela(listaSongs,band)


    #Impresión
    if(ValueBand):
        print("Si existe alguna cancion de Audioslave en la lista de canciones")
    else:
        print("No existe alguna cancion de Audioslave en la lista de canciones")