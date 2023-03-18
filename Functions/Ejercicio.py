songs = [
["Smells Like Teen Spirit", "Nirvana", "Grunge", 1991, 10000000],
["Come Together", "The Beatles", "Rock", 1969, 10000000],
["Paint It Black", "The Rolling Stones", "Rock", 1966, 1213100000],
["I Want To Hold Your Hand", "The Beatles", "Rock", 1963, 50000],
["Hey Jude", "The Beatles", "Rock", 1968, 4000000],
["Yesterday", "The Beatles", "Rock", 1965, 1450000000],
["Satisfaction", "The Rolling Stones", "Rock", 1965, 1560000],
["Imagine", "John Lennon", "Rock", 1971, 1000000],
["Stairway To Heaven", "Led Zeppelin", "Rock", 1971, 13400000],
["Baby One More Time", "Britney Spears", "Pop", 1999, 10034500],
["Baby", "Justin Bieber", "Pop", 2010, 11233000],
["Something in the Way", "Nirvana", "Grunge", 1991, 131232100000],
["Heart-Shaped Box", "Nirvana", "Grunge", 1993, 1120000000],
]

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
