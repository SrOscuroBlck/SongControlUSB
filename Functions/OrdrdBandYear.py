# Artist Position: 1
# Name Position: 0
 

def cocktailBubbleSort(songs, pos) :
    i = 0
    notFinished = True
    
    while (i < (len(songs)-1) and notFinished) :
        notFinished = False
        for j in range(len(songs) - 1 - i) :
            if (songs[j][0]> songs[j+1][0]) :
                notFinished = True
                songs[j], songs[j+1] = songs[j+1], songs[j]
        i += 1
    
    return songs

def SearchArtistSongs(songs, artist) :
    artistList = []
    for i in range(len(songs)) :
        if (songs[i][1] == artist) :
            artistList.append(songs[i])
                
    return artistList
    
    

def orderByBandYear(songs) :
    artists = []
    orderedSongs = []
    for i in range(len(songs)) :
        if (songs[i][1] not in artists) :
            artists.append(songs[i][1])
    
    artists.sort()
    
    for i in range(len(artists)) :
        artistSongs = cocktailBubbleSort(SearchArtistSongs(songs, artists[i]), 3)
        for j in range(len(artistSongs)) :
            orderedSongs.append(artistSongs[j])
    
    return orderedSongs

def ordrdBandYear(list) :
    
    songs = orderByBandYear(list)    
    print(songs)
    for i in range(len(songs)) :
        print("\nSong Name: " +  songs[i][0])
        print("Artist: " +  songs[i][1])
        print("Genre: " +  songs[i][2])
        print("Release Year: " +  str(songs[i][3]))
        print("Downloads: " +  str(songs[i][4]))
    