from lista import Lista
#ej9
class Cancion:
    def __init__(self, nombre, artista, duracion, reproducciones):
        self.nombre = nombre.upper()
        self.artista = artista.upper()
        self.duracion = duracion
        self.reproducciones = reproducciones
    
    def __str__(self):
        nl = '\n'
        strNombre = 'NOMBRE: %s'%self.nombre
        strArtista = 'ARTISTA: %s'%self.artista
        strDuracion = 'DURACION: %s min'%(((self.duracion * 100) //60)/100)
        strReproducciones = 'REPRODUCCIONES: %s'%(self.reproducciones) 
        return strNombre + nl + strArtista + nl + strDuracion + nl + strReproducciones + nl

def buscar_mayor_duracion(canciones:Lista):
    mayor_duracion = canciones[0]
    for cancion in canciones:
        if cancion.duracion > mayor_duracion.duracion:
            mayor_duracion = cancion
    return mayor_duracion

def tops(canciones:Lista):
    """Devuelve un top5, un top10 y un top40"""
    canciones = canciones.copia() #Para no modificar la lista original
    if canciones.tamanio() < 40:
        raise IndexError('Debe haber mas de 40 canciones')
    
    def top1(canciones:Lista):
        """Devolver y eliminar el top1"""
        mas_escuchada = canciones[0]
        posicion = 0
        i = 1
        while i < canciones.tamanio():
            if canciones[i]. reproducciones > mas_escuchada.reproducciones:
                mas_escuchada = canciones[i]
                posicion = i
            i += 1
        canciones.suprime(posicion)
        return mas_escuchada

    top5 = Lista()
    for i in range(0,5):
        top5.inserta(top1(canciones))
    
    top10 = top5.copia()
    for i in range(0,5):
        top10.inserta(top1(canciones))

    top40 = top10.copia()
    for i in range(0,30):
        top40.inserta(top1(canciones))
    
    return top5, top10, top40

def get_canciones_por_artista(artista, canciones:Lista):
    artista = artista.upper()
    canciones_artista = Lista()

    for cancion in canciones:
        if artista == cancion.artista:
            canciones_artista.inserta(cancion)
        
    return canciones_artista

canciones = Lista()
canciones.inserta(Cancion("Creep", "Radiohead", 239, 1671571))
canciones.inserta(Cancion("The Less I Know the Better", "Tame Impala", 0, 477144))
canciones.inserta(Cancion("Take Me Out", "Franz Ferdinand", 256, 1699145))
canciones.inserta(Cancion("Seven Nation Army", "The White Stripes", 449, 1542643))
canciones.inserta(Cancion("Do I Wanna Know?", "Arctic Monkeys", 272, 939727))
canciones.inserta(Cancion("Last Nite", "The Strokes", 0, 1023255))
canciones.inserta(Cancion("Smells Like Teen Spirit", "Nirvana", 301, 2102912))
canciones.inserta(Cancion("Midnight City", "M83", 244, 996633))
canciones.inserta(Cancion("Lonely Boy", "The Black Keys", 193, 819218))
canciones.inserta(Cancion("Love Will Tear Us Apart", "Joy Division", 0, 1144228))
canciones.inserta(Cancion("Losing My Religion", "R.E.M.", 301, 1224435))
canciones.inserta(Cancion("Karma Police", "Radiohead", 0, 1654772))
canciones.inserta(Cancion("Wonderwall", "Oasis", 259, 1893788))
canciones.inserta(Cancion("Where Is My Mind?", "Pixies", 0, 1196604))
canciones.inserta(Cancion("Lean On (feat. MØ & DJ Snake)", "Major Lazer", 0, 452149))
canciones.inserta(Cancion("Hello", "Adele", 0, 427406))
canciones.inserta(Cancion("Can't Feel My Face", "The Weeknd", 0, 482609))
canciones.inserta(Cancion("Sultans of Swing", "Dire Straits", 348, 1064334))
canciones.inserta(Cancion("Mr. Brightside", "The Killers", 224, 2020239))
canciones.inserta(Cancion("Sweet Child o' Mine", "Guns N' Roses", 356, 1407513))
canciones.inserta(Cancion("Let It Happen", "Tame Impala", 0, 380113))
canciones.inserta(Cancion("No Surprises", "Radiohead", 0, 1327206))
canciones.inserta(Cancion("Sex on Fire", "Kings of Leon", 222, 1506746))
canciones.inserta(Cancion("Come as You Are", "Nirvana", 208, 1854896))
canciones.inserta(Cancion("Cheap Thrills", "Sia", 0, 393843))
canciones.inserta(Cancion("Uprising", "Muse", 302, 1001774))
canciones.inserta(Cancion("Reptilia", "The Strokes", 214, 1242285))
canciones.inserta(Cancion("Adventure Of A Lifetime", "Coldplay", 0, 311777))
canciones.inserta(Cancion("Under the Bridge", "Red Hot Chili Peppers", 265, 1564579))
canciones.inserta(Cancion("Feel Good Inc.", "Gorillaz", 221, 1528670))
canciones.inserta(Cancion("Boys Don't Cry", "The Cure", 139, 996658))
canciones.inserta(Cancion("My Number", "Foals", 240, 494779))
canciones.inserta(Cancion("Uptown Funk", "Mark Ronson", 0, 506726))
canciones.inserta(Cancion("Friday I'm in Love", "The Cure", 214, 1075210))
canciones.inserta(Cancion("What You Know", "Two Door Cinema Club", 197, 907309))
canciones.inserta(Cancion("Shape of You", "Ed Sheeran", 0, 429384))
canciones.inserta(Cancion("Teardrop", "Massive Attack", 279, 1319967))
canciones.inserta(Cancion("Bohemian Rhapsody - Remastered 2011", "Queen", 0, 349480))
canciones.inserta(Cancion("Burn the Witch", "Radiohead", 0, 284236))
canciones.inserta(Cancion("Intro", "The xx", 127, 1115590))
canciones.inserta(Cancion("The House of the Rising Sun", "The Animals", 268, 971643))
canciones.inserta(Cancion("Fortunate Son", "Creedence Clearwater Revival", 138, 1009327))
canciones.inserta(Cancion("Kids", "MGMT", 288, 1613941))
canciones.inserta(Cancion("The Passenger", "Iggy Pop", 373, 806029))
canciones.inserta(Cancion("Skinny Love", "Bon Iver", 239, 1096015))
canciones.inserta(Cancion("Back to Black", "Amy Winehouse", 0, 1184921))
canciones.inserta(Cancion("What Do You Mean?", "Justin Bieber", 0, 341140))
canciones.inserta(Cancion("Copenhague", "Vetusta Morla", 353, 50535))
canciones.inserta(Cancion("Walk on the Wild Side", "Lou Reed", 252, 754131))
canciones.inserta(Cancion("Bitter Sweet Symphony", "The Verve", 275, 1191214))
canciones.inserta(Cancion("Creep", "Radiohead", 239, 1671571))
canciones.inserta(Cancion("Do I Wanna Know?", "Arctic Monkeys", 272, 939727))
canciones.inserta(Cancion("Last Nite", "The Strokes", 0, 1023255))
canciones.inserta(Cancion("Karma Police", "Radiohead", 0, 1654772))
canciones.inserta(Cancion("Under the Bridge", "Red Hot Chili Peppers", 265, 1564579))
canciones.inserta(Cancion("Losing My Religion", "R.E.M.", 301, 1224435))
canciones.inserta(Cancion("Puente", "Gustavo Cerati", 275, 62787))
canciones.inserta(Cancion("The Less I Know the Better", "Tame Impala", 0, 477144))
canciones.inserta(Cancion("Come as You Are", "Nirvana", 208, 1854896))
canciones.inserta(Cancion("Smells Like Teen Spirit", "Nirvana", 301, 2102912))
canciones.inserta(Cancion("Reptilia", "The Strokes", 214, 1242285))
canciones.inserta(Cancion("Crimen", "Gustavo Cerati", 228, 72198))
canciones.inserta(Cancion("Take Me Out", "Franz Ferdinand", 256, 1699145))
canciones.inserta(Cancion("Seven Nation Army", "The White Stripes", 449, 1542643))
canciones.inserta(Cancion("Feel Good Inc.", "Gorillaz", 221, 1528670))
canciones.inserta(Cancion("Can't Feel My Face", "The Weeknd", 0, 482609))
canciones.inserta(Cancion("Love Will Tear Us Apart", "Joy Division", 0, 1144228))
canciones.inserta(Cancion("No Surprises", "Radiohead", 0, 1327206))
canciones.inserta(Cancion("Otherside", "Red Hot Chili Peppers", 255, 1389331))
canciones.inserta(Cancion("Coffee & TV", "Blur", 318, 681464))
canciones.inserta(Cancion("Where Is My Mind?", "Pixies", 0, 1196604))
canciones.inserta(Cancion("Californication", "Red Hot Chili Peppers", 322, 1637846))
canciones.inserta(Cancion("High and Dry", "Radiohead", 256, 1101270))
canciones.inserta(Cancion("Bitter Sweet Symphony", "The Verve", 275, 1191214))
canciones.inserta(Cancion("Fluorescent Adolescent", "Arctic Monkeys", 182, 1014785))
canciones.inserta(Cancion("Paranoid Android", "Radiohead", 385, 1359993))
canciones.inserta(Cancion("Take on Me", "a-ha", 227, 1191719))
canciones.inserta(Cancion("Clint Eastwood", "Gorillaz", 339, 1258408))
canciones.inserta(Cancion("Boys Don't Cry", "The Cure", 139, 996658))
canciones.inserta(Cancion("Friday I'm in Love", "The Cure", 214, 1075210))
canciones.inserta(Cancion("Wonderwall", "Oasis", 259, 1893788))
canciones.inserta(Cancion("Scar Tissue", "Red Hot Chili Peppers", 234, 1398870))
canciones.inserta(Cancion("Burn the Witch", "Radiohead", 0, 284236))
canciones.inserta(Cancion("Girls & Boys", "Blur", 259, 708774))
canciones.inserta(Cancion("Everlong", "Foo Fighters", 323, 1345396))
canciones.inserta(Cancion("Bohemian Rhapsody - Remastered 2011", "Queen", 0, 349480))
canciones.inserta(Cancion("Close to Me", "The Cure", 221, 812136))
canciones.inserta(Cancion("Sex on Fire", "Kings of Leon", 222, 1506746))
canciones.inserta(Cancion("Someday", "The Strokes", 0, 1132268))
canciones.inserta(Cancion("Sweet Child o' Mine", "Guns N' Roses", 356, 1407513))
canciones.inserta(Cancion("Adiós", "Gustavo Cerati", 245, 54465))
canciones.inserta(Cancion("Black Hole Sun", "Soundgarden", 0, 1064912))
canciones.inserta(Cancion("R U Mine?", "Arctic Monkeys", 200, 755175))
canciones.inserta(Cancion("Irresponsables", "Babasónicos", 156, 56316))
canciones.inserta(Cancion("Yellow", "Coldplay", 267, 1596163))
canciones.inserta(Cancion("Mr. Brightside", "The Killers", 224, 2020239))
canciones.inserta(Cancion("Seguir Viviendo Sin Tu Amor", "Luis Alberto Spinetta", 160, 24818))
canciones.inserta(Cancion("Back to Black", "Amy Winehouse", 0, 1184921))
canciones.inserta(Cancion("Walk on the Wild Side", "Lou Reed", 252, 754131))
canciones.inserta(Cancion("Fake Plastic Trees", "Radiohead", 285, 1092240))
canciones.inserta(Cancion("Creep", "Radiohead", 239, 1671571))
canciones.inserta(Cancion("Karma Police", "Radiohead", 0, 1654772))
canciones.inserta(Cancion("The Less I Know the Better", "Tame Impala", 0, 477144))
canciones.inserta(Cancion("Last Nite", "The Strokes", 0, 1023255))
canciones.inserta(Cancion("Take Me Out", "Franz Ferdinand", 256, 1699145))
canciones.inserta(Cancion("Do I Wanna Know?", "Arctic Monkeys", 272, 939727))
canciones.inserta(Cancion("Seven Nation Army", "The White Stripes", 449, 1542643))
canciones.inserta(Cancion("Losing My Religion", "R.E.M.", 301, 1224435))
canciones.inserta(Cancion("Love Will Tear Us Apart", "Joy Division", 0, 1144228))
canciones.inserta(Cancion("No Surprises", "Radiohead", 0, 1327206))
canciones.inserta(Cancion("Can't Feel My Face", "The Weeknd", 0, 482609))
canciones.inserta(Cancion("Smells Like Teen Spirit", "Nirvana", 301, 2102912))
canciones.inserta(Cancion("Paranoid Android", "Radiohead", 385, 1359993))
canciones.inserta(Cancion("Reptilia", "The Strokes", 214, 1242285))
canciones.inserta(Cancion("High and Dry", "Radiohead", 256, 1101270))
canciones.inserta(Cancion("Girls & Boys", "Blur", 259, 708774))
canciones.inserta(Cancion("Coffee & TV", "Blur", 318, 681464))
canciones.inserta(Cancion("Tren Al Sur", "Los Prisioneros", 337, 45337))
canciones.inserta(Cancion("Mr. Brightside", "The Killers", 224, 2020239))
canciones.inserta(Cancion("Estrechez De Corazón", "Los Prisioneros", 385, 26555))
canciones.inserta(Cancion("Feel Good Inc.", "Gorillaz", 221, 1528670))
canciones.inserta(Cancion("Bitter Sweet Symphony", "The Verve", 275, 1191214))
canciones.inserta(Cancion("Under the Bridge", "Red Hot Chili Peppers", 265, 1564579))
canciones.inserta(Cancion("Where Is My Mind?", "Pixies", 0, 1196604))
canciones.inserta(Cancion("Come as You Are", "Nirvana", 208, 1854896))
canciones.inserta(Cancion("One More Time", "Daft Punk", 0, 1200051))
canciones.inserta(Cancion("Un Amor Violento", "Los Tres", 315, 29930))
canciones.inserta(Cancion("Bohemian Rhapsody - Remastered 2011", "Queen", 0, 349480))
canciones.inserta(Cancion("Fake Plastic Trees", "Radiohead", 285, 1092240))
canciones.inserta(Cancion("Lean On (feat. MØ & DJ Snake)", "Major Lazer", 0, 452149))
canciones.inserta(Cancion("Amiga Mía", "Los Prisioneros", 244, 17063))
canciones.inserta(Cancion("Fluorescent Adolescent", "Arctic Monkeys", 182, 1014785))
canciones.inserta(Cancion("Friday I'm in Love", "The Cure", 214, 1075210))
canciones.inserta(Cancion("Close to Me", "The Cure", 221, 812136))
canciones.inserta(Cancion("Boys Don't Cry", "The Cure", 139, 996658))
canciones.inserta(Cancion("Black Hole Sun", "Soundgarden", 0, 1064912))
canciones.inserta(Cancion("Otherside", "Red Hot Chili Peppers", 255, 1389331))
canciones.inserta(Cancion("Sex on Fire", "Kings of Leon", 222, 1506746))
canciones.inserta(Cancion("Everlong", "Foo Fighters", 323, 1345396))
canciones.inserta(Cancion("Let It Happen", "Tame Impala", 0, 380113))
canciones.inserta(Cancion("Chop Suey!", "System of a Down", 208, 1531764))
canciones.inserta(Cancion("Even Flow", "Pearl Jam", 0, 889287))
canciones.inserta(Cancion("1979", "The Smashing Pumpkins", 263, 1033693))
canciones.inserta(Cancion("Burn the Witch", "Radiohead", 0, 284236))
canciones.inserta(Cancion("Pumped Up Kicks", "Foster the People", 236, 1266869))
canciones.inserta(Cancion("Sorry", "Justin Bieber", 0, 372143))
canciones.inserta(Cancion("Electric Feel", "MGMT", 229, 1436425))
canciones.inserta(Cancion("There Is A Light That Never Goes Out - 2011 Remastered Version", "The Smiths", 0, 251665))
canciones.inserta(Cancion("Californication", "Red Hot Chili Peppers", 322, 1637846))
canciones.inserta(Cancion("Take on Me", "a-ha", 227, 1191719))


for cancion in canciones:
    print(cancion.nombre)
# print(buscar_mayor_duracion(canciones))
# (top5, top10, top40) = tops(canciones)

# for cancion in top40:
#     print(cancion)