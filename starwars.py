from lista import Lista
from starwarsdata import personajes
from conjunto import Conjunto


def titulo(texto):
        print()
        print('*'*80)
        print(texto)
        print('-'*80)


def imprimir_mujeres(personajes):
    for personaje in personajes:
        if personaje.gender == 'female':
            print(personaje)


def listar_droides(personajes):
    primeras_6 = Conjunto(1,2,3,4,5,6)
    for personaje in personajes:
        try:
            specie = personaje.species[0]
        except:
            continue

        if  specie == 'Droid':
            aparece_en = Conjunto()
            for film in personaje.films:
                aparece_en.add(film)

            if aparece_en >= primeras_6:
                print(personaje.name)


def mostrar_info_de(nombre):
    nombre = nombre.upper()
    for personaje in personajes:
        if personaje.name.upper() == nombre:
            print('NOMBRE: %s'%personaje.name)
            try:
                print('ESPECIE: %s'%personaje.species[0])
            except:
                pass
            print('PLANETA: %s'%personaje.homeworld)


def estuvieron_en_4_5_6_7(personajes):
    cuatro_5_6_y_7 = Conjunto(4,5,6,7)

    for personaje in personajes:
        estuvo_en = Conjunto()
        for film in personaje.films:
            estuvo_en.add(film)
        if estuvo_en >= cuatro_5_6_y_7:
            print(personaje)

def eliminar_4_5_y_6(personajes):
    cuatro_5_y_6 = Conjunto(4,5,6)
    for personaje in personajes:
        estuvo_en = Conjunto()
        for film in personaje.films:
            estuvo_en.add(film)
        if estuvo_en.intersection(cuatro_5_y_6) == cuatro_5_y_6:
            if estuvo_en.difference(cuatro_5_y_6).is_empty():
                print('Eliminando a %s'%personaje)

def humanos_de_alderaan(personajes):
    for personaje in personajes:
        try:
            specie = personaje.species[0]
        except:
            continue

        if specie == 'Human' and personaje.homeworld == 'Alderaan':
            print(personaje.name)


def altura_menor_70(personajes):
    for personaje in personajes:
        try:
            es_menor_a_70  = int(personaje.height) < 70
        except:
            continue

        if es_menor_a_70:
            mostrar_info_de(personaje.name)


def eliminar_anteultimo_elemento(lista:Lista):
    print('Eliminando %s'%lista[-2])
    del lista[-2]

def en_que_episodios_aparece(nombre, personajes):
    nombre = nombre.upper()           
    for personaje in personajes:
        if personaje.name.upper() == nombre:
            print('%s aparece en '%nombre, end='')
            personaje.films.sort()
            for i in range(0, len(personaje.films)-1):
                print(personaje.films[i], end=', ')
            print(personaje.films[-1])


#10.a
titulo('Mujeres')
imprimir_mujeres(personajes)
#10.b
titulo('Droides de las primeras 6 pelis')
listar_droides(personajes)
#10.c
titulo('Info de Darth Vader')
mostrar_info_de('Darth Vader')
#10.d 
titulo('Estuvieron en 4,5,6 y 7:')
estuvieron_en_4_5_6_7(personajes)
# #10.e falta dato
# #10.f
titulo('Estuvieron en 4,5 y 6 solamente:')
eliminar_4_5_y_6(personajes)
#10.g
titulo('Humanos de Alderaan')
humanos_de_alderaan(personajes)
#10.h
titulo('Personajes de menos de 70cm')
altura_menor_70(personajes)
#10.i
titulo('Eliminar anteúltimo nodo de la lista')
eliminar_anteultimo_elemento(personajes)
#10.j
titulo('En que episodios aparece Chewbacca')
en_que_episodios_aparece('Chewbacca', personajes)
