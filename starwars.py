from lista import Lista
import swapi

def titulo(texto):
        print()
        print('*'*80)
        print(texto)
        print('-'*80)

personajes =  Lista()

##Obteniendo todos los personajes (swapi.get_all('people') aveces da error)
for i in range(1,89):
    try:
        personajes.inserta(swapi.get_person(i))
    except:
        continue

def imprimir_mujeres(personajes):
    for personaje in personajes:
        if personaje.gender == 'female':
            print(personaje.name)


def listar_droides(personajes):
    for personaje in personajes:
        try:
            especie = personaje.get_species().items[0].name 
            if  especie == 'Droid':
                films = personaje.get_films().items
                primeras_6 = {1,2,3,4,5,6}
                aparece_en = set()
                for film in films:
                    if film.episode_id in (1,2,3,4,5,6):
                        aparece_en.add(film.episode_id)
                if aparece_en == primeras_6:
                    print(personaje.name)
        except:
            pass


def mostrar_info_de(nombre):
    nombre = nombre.upper()
    for personaje in personajes:
        if personaje.name.upper() == nombre:
            print('NOMBRE: %s'%personaje.name)
            print('ESPECIE: %s'%personaje.get_species().items[0].name)
            print('PLANETA: %s'%personaje.get_homeworld().name)


def personajes_por_episodio(personajes):
       
    episodios = {
    'https://swapi.co/api/films/7/' : 7 ,
    'https://swapi.co/api/films/6/' : 6 ,
    'https://swapi.co/api/films/5/' : 5 ,
    'https://swapi.co/api/films/4/' : 4 , 
    'https://swapi.co/api/films/3/' : 3 ,
    'https://swapi.co/api/films/2/' : 2 ,
    'https://swapi.co/api/films/1/' : 1 
    }
    #Para no hacer tantas peticiones ¯\_(ツ)_/¯

    conjuntos = {numero:set() for (url, numero) in episodios.items()}

    for personaje in personajes:
        for film in personaje.films:
            conjuntos[episodios[film]].add(personaje.name.upper())
    
    interseccion = conjuntos[7]
    for i in (4,5,6):
        interseccion = interseccion.intersection(conjuntos[i])
    
    titulo('Personajes que aparecen en 4,5,6 y 7 (en todas ellas)')
    for nombre in interseccion:
        print(nombre)
    
    en_4_5_y_6 = set().union(conjuntos[4])
    for i in (5,6):
        en_4_5_y_6 = en_4_5_y_6.intersection(conjuntos[i])

    estuvieron_alguna_otra = set()
    for i in (1,2,3,7):
        estuvieron_alguna_otra = estuvieron_alguna_otra.union(conjuntos[i])

    solo_en_4_5_6 = en_4_5_y_6 - estuvieron_alguna_otra

    titulo('Solo estuvieron en 4, 5 y 6 (en todas ellas)')
    for personaje in solo_en_4_5_6:
        print(personaje)


def humanos_de_alderaan(personajes):
    alderaan = 'https://swapi.co/api/planets/2/'
    humano = 'https://swapi.co/api/species/1/'

    titulo('Humanos de Alderaan')
    for personaje in personajes:
        try:
            if personaje.species[0] == humano and personaje.homeworld == alderaan:
                print(personaje.name)
        except:
            continue


def altura_menor_70(personajes):
    for personaje in personajes:
        try:
            print('algo')
            if int(personaje.height) < 70:
                mostrar_info_de(personaje.name)
        except:
            continue


def eliminar_anteultimo_elemento(lista:Lista):
    anteultimo = lista.tamanio() - 2
    lista.suprime(anteultimo)


def en_que_episodios_aparece(nombre, personajes):
    nombre = nombre.upper()           
    episodios = {
    'https://swapi.co/api/films/7/' : 7 ,
    'https://swapi.co/api/films/6/' : 6 ,
    'https://swapi.co/api/films/5/' : 5 ,
    'https://swapi.co/api/films/4/' : 4 , 
    'https://swapi.co/api/films/3/' : 3 ,
    'https://swapi.co/api/films/2/' : 2 ,
    'https://swapi.co/api/films/1/' : 1 
    }

    conjuntos = {numero:set() for (url, numero) in episodios.items()}
    for personaje in personajes:
        for film in personaje.films:
            conjuntos[episodios[film]].add(personaje.name.upper())

    for clave in conjuntos:
        if nombre in conjuntos[clave]:
            print('%s aparece en episodio %s'%(nombre, clave))


#10.a
imprimir_mujeres(personajes)
#10.b
listar_droides(personajes)
#10.c
mostrar_info_de('Darth Vader')
#10.d y 10.f
personajes_por_episodio(personajes)
#10.e falta dato

#10.g
humanos_de_alderaan(personajes)
#10.h
altura_menor_70(personajes)
#10.i
#eliminar_anteultimo_elemento(lista)
#10.j
en_que_episodios_aparece('Chewbacca', personajes)
