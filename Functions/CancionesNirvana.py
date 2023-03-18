#Buscar canciones de Nirvana
def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    
    return i

def buscar_canciones_nirvana(songs):
    
    lista = quick_sort(songs)
    
    canciones_nirvana = []
    hay_nirvana = False
    
    count = 0;
    
    for song in lista:
        if song[1] == "Nirvana":
            canciones_nirvana.append(song)
            hay_nirvana = True
            count += 1
            
    if hay_nirvana:
        print("\nSe encontraron", count, "canciones de Nirvana:\n")
        for cancion in canciones_nirvana:
            print("Nombre:", cancion[0], "- Genero:", cancion[2], "- Año:", cancion[3], "- Numero de descargas:", cancion[4])
    else:
        print("\nNo se encontraron canciones de Nirvana en la lista\n")

#==============================================================================|