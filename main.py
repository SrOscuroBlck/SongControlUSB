from Functions.GenderFilter import getGenderFilter
from Functions.PointB import functionB
from Functions.Top10 import printTop
from Functions.OrdrdBandYear import ordrdBandYear
import Functions.CancionesNirvana as buscar_canciones_nirvana;

# Position 0: Name, 1: Artist, 2: Genre, 3: Year, 4: Downloads
songs = [
["Smells Like Teen Spirit", "Nirvana", "grunge", 1991, 10000000],
["Come Together", "The Beatles", "rock", 1969, 10000000],
["Paint It Black", "The Rolling Stones", "rock", 1966, 1213100000],
["I Want To Hold Your Hand", "The Beatles", "rock", 1963, 50000],
["Hey Jude", "The Beatles", "rock", 1968, 4000000],
["Yesterday", "The Beatles", "rock", 1965, 1450000000],
["Satisfaction", "The Rolling Stones", "rock", 1965, 1560000],
["Imagine", "John Lennon", "rock", 1971, 1000000],
["Stairway To Heaven", "Led Zeppelin", "rock", 1971, 13400000],
["Baby One More Time", "Britney Spears", "pop", 1999, 10034500],
["Baby", "Justin Bieber", "pop", 2010, 11233000],
["Something in the Way", "Nirvana", "grunge", 1991, 131232100000],
["Heart-Shaped Box", "Nirvana", "grunge", 1993, 1120000000],
["Like a Stone", "Audioslave", "rock", 2002,683432],
["Gasoline","Audioslave","rock",2002,86673213]
]

print("=================================================")
print("> [1] - Buscar canciones de Nirvana\n> [2] - Ordenar por banda y año\n> [3] - Géneros con cantidad de canciones y promedio de descargas\n> [4] - Mostrar canciones por rango de año\n> [5] - Banda o artista con mayor cantidad de canciones por año\n> [6] - Top 10 canciones con mayor descarga\n> [7] - Canciones de Audio Slave\n> [8] - Salir")
print("=================================================\n")

op = int(input("Ingrese una opción: "))

while op != 8:
    
    if op == 1:
        buscar_canciones_nirvana.buscar_canciones_nirvana(songs)
        
    elif op == 2:
        print("\nOrdenar por banda y año: \n")
        ordrdBandYear(songs)
    elif op == 3:
        print("\nGéneros con cantidad de canciones y promedio de descargas: \n")
        genre = input("Ingrese el género: ")
        getGenderFilter(genre, songs)
    elif op == 4:
        print("\nMostrar canciones por rango de año: \n")
        
        str = int(input("Ingrese el primer rango de años: "))
        str2 = int(input("Ingrese el segundo rango de años: "))
        
    elif op == 5:
        print("\nBanda o artista con mayor cantidad de canciones por año: \n")
        arr = []
        for i in range(0, len(songs)):
            arr.append(songs[i][3])


        print(arr)

        def insertion(songs):
            for i in range(1, len(songs)):
                song = songs[i]
                j = i - 1
                while j >= 0 and song[3] < songs[j][3]:
                    songs[j + 1] = songs[j]
                    j -= 1
                songs[j + 1] = song
            return songs

        print(insertion(songs))


        #Algoritmo de busqueda
        def centinela(lista, buscado):
            cont = 0
            for i in range(0, len(lista)):
                if (lista[i][1] == buscado):
                    cont = cont + 1
            return cont


        print("El numero de canciones de The Beatles es: ", centinela(songs, "The Beatles"))
        print("El numero de canciones de Nirvana es: ", centinela(songs, "Nirvana"))
        print("El numero de canciones de The Rolling Stones es: ", centinela(songs, "The Rolling Stones"))
        print("El numero de canciones de John Lennon es: ", centinela(songs, "John Lennon"))
        print("El numero de canciones de Led Zeppelin es: ", centinela(songs, "Led Zeppelin"))
        print("El numero de canciones de Britney Spears es: ", centinela(songs, "Britney Spears"))
        print("El numero de canciones de Justin Bieber es: ", centinela(songs, "Justin Bieber"))

    elif op == 6:
        print("\nTop 10 canciones con mayor descarga: \n")
        printTop(songs)
    elif op == 7:
        print("\nExisten canciones de Audioslave en la lista?: \n")
        functionB(songs)
    else:
        print("Opción no valida")
    
    op = int(input("\nIngrese una opción: "))
