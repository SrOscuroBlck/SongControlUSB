def selectionSort(list):
    """
    Ordena una list de canciones por descargas de mayor a menor, utilizando el algoritmo de ordenamiento por selección.
    donde list es una list de canciones, posteriormente retorna la list ordenada por cantidad de descargas.
    """
    
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j][4] > list[min_idx][4]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

def topTenSongs(songs):
    """
    Retorna una lista con las 10 canciones más descargadas de la lista de canciones.
    """
    selectionSort(songs)
    return songs[:10]

def printTop(songs):
    """
    Imprime las 10 canciones más descargadas de la lista de canciones.
    """
    for i, song in enumerate(topTenSongs(songs), 1):
        print(f"{i}. {song[0]} - {song[1]} ({song[4]} descargas)")

