def getCantPromGender(genre, list):
    """
    Esta función recibe como parámetros un género y una lista de canciones, y retorna una tupla con la cantidad de canciones
    y el promedio de descargas de las canciones del género especificado, este es el momento en el que se usa un algoritmo de
    busqueda lineal para recorrer la lista de canciones y obtener la información solicitada.
    """
    songs = 0
    totalDownloads = 0
    for song in list:
        if song[2] == genre:
            songs += 1
            totalDownloads += song[4]
            
    return (songs, totalDownloads/songs)


def getGenderFilter(genre, list):
    
    genres = []
    for song in list:
        if song[2] not in genres:
            genres.append(song[2].lower())
      
    loweredGenre = genre.lower()      
    if loweredGenre not in genres:
        print("El género no existe")
        return
    else:
        genreInfo = getCantPromGender(loweredGenre, list)
        print("El genero: ", genre, " tiene ", genreInfo[0], " canciones y un promedio de descargas de ", genreInfo[1])
        
            
        
    
    
