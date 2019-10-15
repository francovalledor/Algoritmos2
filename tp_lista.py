from lista_de import Lista as Lde
from lista import Lista
from conjunto import Conjunto
from random import randint
from time import sleep
from lista_circular import Lista as lc

# ej1


def contar_cantidad_nodos(lista: Lista):
    """Cuenta la cantidad de nodos de una lista"""
    return len(lista)

# ej2


def eliminar_vocales_lista(caracteres: Lista):
    VOCALES = 'AEIOUaeiou'
    i = 0
    while i < len(caracteres):
        if caracteres[i] in VOCALES:
            caracteres.suprime(i)
        else:
            i += 1
        # Existe una manera mas eficiente de hacerlo trabajando a bajo nivel

# ej3


def dividir_pares_impares(numeros_enteros: Lista):
    pares = Lista()
    impares = Lista()

    for numero in numeros_enteros:
        if numero % 2 == 0:
            pares.insert(numero)
        else:
            impares.insert(numero)
    return pares, impares

# ej4


def inserta_en_iesima(elemento, posicion, lista: Lista):
    lista.insert(elemento, posicion)


# ej5
def es_primo(numero):
    from math import sqrt, trunc

    if numero <= 1:
        b_es_primo = False
    elif numero == 2:
        b_es_primo = True
    elif numero % 2 == 0:
        b_es_primo = False
    else:
        b_es_primo = True

        limite = trunc(sqrt(numero))
        for cociente in range(3, limite + 1, 2):
            if (numero % cociente == 0):
                b_es_primo = False

    return b_es_primo


def eliminar_primos(numeros_enteros: Lista):
    i = 0
    while i < len(numeros_enteros):
        if es_primo(numeros_enteros[i]):
            numeros_enteros.suprime(i)
        else:
            i += 1

# ej6


class SuperHeroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia


def ej6(superheroes: Lista):
    i = 0
    while i < len(superheroes):
        biografia = superheroes[i].biografia

        if ('traje' in biografia) or ('armadura' in biografia):
            print(superheroes[i].nombre)

        if superheroes[i].anio_aparicion < 1963:
            print(superheroes[i].nombre, superheroes[i].casa)

        if superheroes[i].nombre == 'Linterna Verde':
            superheroes.suprime(i)
        else:
            if superheroes[i].nombre == 'Wolverine':
                print(superheroes[i].anio_aparicion)
            elif superheroes[i].nombre == 'Ant-Man':
                superheroes[i].casa == 'Marvel'
            else:
                i += 1

# ej7


def concatenar_listas(lista1: Lista, lista2: Lista, omitir_repetidos=False):
    if omitir_repetidos:
        i = 0
        lista_aux = Lista()
        while i < len(lista2):
            if lista2[i] not in lista1:
                lista_aux.insert(lista2[i])
        concatenacion = lista1 + lista_aux
    else:
        concatenacion = lista1 + lista2

    return concatenacion


def contar_repetidos(lista1: Lista, lista2: Lista):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    return len(conjunto1.intersection(conjunto2))


def eliminar_todos_nodos(lista: Lista):
    i = 0
    while i < len(lista):
        lista.suprime(0)


# ej8
def ej8(cuantos_numeros):
    import random

    def generar():
        INICIO = -999
        FIN = 999
        return random.randint(INICIO, FIN)

    numeros = Lista()

    while numeros.tamanio() < cuantos_numeros:
        siguiente = generar()

        # REGLAS
        if siguiente in numeros:  # Repetido
            continue
        elif es_primo(siguiente):  # Primo
            if (numeros.tamanio() == 0) or (numeros.tamanio() + 1 == cuantos_numeros):
                continue
            elif abs(numeros.recupera(numeros.fin()-1) - siguiente) > 14:
                numeros.insert(siguiente)
                anterior = siguiente
                while abs(anterior - siguiente) <= 14:
                    siguiente = generar()
                numeros.insert(siguiente)
            else:
                continue
        elif siguiente % 2 != 0:  # Impar no primo
            if (numeros.tamanio() == 0) or (numeros.tamanio() + 1 == cuantos_numeros):
                continue
            elif numeros.recupera(numeros.fin()-1) % 2 == 0:
                numeros.insert(siguiente)
                while siguiente % 2 != 0:
                    siguiente = generar()
                numeros.insert(siguiente)
            else:
                continue
        else:
            numeros.insert(siguiente)
    return numeros

# ej11
# """
# Desarrollar un algoritmo que implemente lista de archivo para realizar las siguientes
# actividades:
#     a. Agregar números aleatorios a la lista, no pueden estar repetidos.
#     b. Borrar números y permitir reutilizar los huecos que quedan en el archivo.
#     c. Realizar un barrido de la lista.
#     d. Consultar cuantos elementos y cuantos huecos hay en la lista.
# """
# numeros = Lista()
# #a
# for i in range(0,100):
#     while True:
#         numero_aleatorio = random.randint(0,1000)
#         if numero_aleatorio not in numeros:
#             numeros.insert(numero_aleatorio)
#             break

# #b
# for i in range(1,10):
#     posicion_aleatoria = random.randint(0,len(numeros))
#     del numeros[posicion_aleatoria]

# #c
# for numero in numeros:
#     print(numero)

# #d
# print('hay %d elementos en la lista'%len(numeros))
# print('No hay huecos en la lista')


# ej12
"""
Desarrollar un algoritmo que permita visualizar el contenido de una lista de 
manera ascendente y descendente de sus elementos, debe implementar lista 
doblemente enlazada.
"""


def visualizar_lista(lista: Lde, descendente=False):
    lista.sort()
    if descendente:
        for elemento in reversed(lista):
            print(elemento, end=' ')
    else:
        for elemento in lista:
            print(elemento, end=' ')
    print()

# elementos = Lde(0,1,2,3,4,5,6,7,8)
# visualizar_lista(elementos)
# visualizar_lista(elementos, descendente=True)


# ej13
"""
Un grupo de amigos se reúnen a jugar un juego de dados, supongamos que dichos
jugadores están cargados en una lista de acuerdo a un número asignado de manera
aleatoria. Desarrollar un algoritmo que contemple las siguientes condiciones:
a. Simular la tirada de un dado (de seis lados D6) en cada turno del jugador.
b. El orden de los turnos en que juegan es como están cargados en la lista.
c. Después de que tira el último jugador de la lista debe seguir el primero.
d. El juego termina cuando uno de los jugadores saca un 5.
e. Debe implementar lista circular.
"""


def tirar_dado() -> int:
    return randint(1, 6)


def juego_dados():
    while True:
        try:
            cantidad_jugadores = int(input('Cantidad de jugadores: '))
            if cantidad_jugadores < 1:
                continue
        except:
            continue
        break

    jugadores = lc()
    for i in range(1, cantidad_jugadores + 1):
        nombre = input('Jugador #%d: ' % i)
        jugadores.insert(nombre)

    print('='*80)
    print('Comienzo del juego')
    while True:
        print('-'*80)
        print('%s es su turno.' % jugadores.actual.data)
        sleep(0.5)
        dado = tirar_dado()
        print('Dado: %d' % dado)
        sleep(0.5)
        if dado == 5:
            break
        else:
            jugadores.avanzar()
    print('*'*80 + '\n')
    print('Ganador: %s' % jugadores.actual.data)
    print('\n' + '*'*80)
    volver_a_jugar = input('Volver a jugar? (s/n) ')
    if volver_a_jugar in ('s', 'S'):
        juego_dados()


# 14
def cantidad_pokemones(entrenador):
    return len(entrenador.pokemones)


def ganaron_mas_de_3_torneos(entrenadores):
    for entrenador in entrenadores:
        if entrenador.torneos_ganados > 3:
            print(entrenador)


def mayor_nivel_pokemon_mas_torneos(entrenadores):
    mas_torneos_ganados = entrenadores[0]
    for entrenador in entrenadores:
        if entrenador.torneos_ganados > mas_torneos_ganados.torneos_ganados:
            mas_torneos_ganados = entrenador

    pokemon_mayor_nivel = mas_torneos_ganados.pokemones[0]
    for pokemon in mas_torneos_ganados.pokemones:
        if pokemon.nivel > pokemon_mayor_nivel.nivel:
            pokemon_mayor_nivel = pokemon

    return pokemon_mayor_nivel


def porcentaje_mayor_79(entrenadores):
    for entrenador in entrenadores:
        if 100*entrenador.ganadas/entrenador.perdidas > 79:
            print(entrenador)


def fuego_planta_agua_volador(entrenadores):
    fuego = 'fire'
    planta = 'grass'
    agua = 'water'
    volador = 'flying'
    tipos = (fuego, planta, agua, volador)
    for entrenador in entrenadores:
        for pokemon in entrenador.pokemones:
            if pokemon.tipo in tipos:
                print(entrenador)
                break

            if pokemon.subtipo in tipos:
                print(entrenador)
                break


def promedio_pokemones(entrenador):
    if len(entrenador.pokemones) > 0:
        suma = 0
        for pokemon in entrenador.pokemones:
            suma += pokemon.nivel
        promedio = suma / len(entrenador.pokemones)
    else:
        promedio = 0
    print('\nEntrenador: %s \nPromedio: %.2f' %
          (entrenador.nombre, promedio))


def cuantos_entrenadores_lo_tienen(pokemon, entrenadores):
    contador = 0
    for entrenador in entrenadores:
        for pokemon_entrenador in entrenador.pokemones:
            if pokemon_entrenador == pokemon:
                contador += 1
                break

    return contador


def si_tiene_pokemones_repetidos(entrenador):
    repetidos = True
    conj = Conjunto()
    for pokemon in entrenador.pokemones:
        conj.add(pokemon)

    if len(entrenador.pokemones) == len(conj):
        repetidos = False

    return repetidos


def mostrar_pokemones_repetidos(entrenadores):
    for entrenador in entrenadores:
        if si_tiene_pokemones_repetidos(entrenador):
            print(entrenador)

# ##Datos de prueba
# from pokemondata import entrenadores, pokemones

# #14.a
# print('\nCantidad de pokemones de : %s'%entrenadores[5].nombre)
# cantidad_pokemones(entrenadores[5])
# #14.b
# print('\nGanaron mas de tres torneos: ')
# ganaron_mas_de_3_torneos(entrenadores)
# #14.c
# print('\nEl Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados')
# print(mayor_nivel_pokemon_mas_torneos(entrenadores))
# #14.d
# print('\nEntrenadores cuyo porcentaje de batallas ganados sea mayor al 79%')
# porcentaje_mayor_79(entrenadores)
# #14.e
# print('\nEntrenadores que tienen Pokémons de tipo fuego y planta o agua/volador')
# fuego_planta_agua_volador(entrenadores)
# #14.f
# print('\nPromedio de nivel de los Pokémons de %s'%entrenadores[5].nombre)
# promedio_pokemones(entrenadores[5])
# #14.g
# print('\nCuantos entrenadores tienen a %s: '%pokemones[5].nombre, end=' ')
# print(cuantos_entrenadores_lo_tienen(pokemones[5], entrenadores))
# #14.h
# print('\nEntrenadores que tienen Pokémons repetidos:')
# mostrar_pokemones_repetidos(entrenadores)


# EJ15
def tiempo_promedio_actividades(proyecto):
    if len(proyecto) > 0:
        suma = 0
        for actividad in proyecto:
            suma += actividad.tiempo_estimado

        promedio = suma / len(proyecto)
    else:
        promedio = 0

    return promedio


def costo_total(proyecto):
    suma = 0
    for actividad in proyecto:
        suma += actividad.costo

    return suma


def actividades_a_cargo_de(persona, proyecto):
    for actividad in proyecto:
        if actividad.persona_a_cargo == persona:
            print(actividad)


def actividades_entre_fechas(proyecto, fecha_inicial, fecha_final):
    for actividad in proyecto:
        if actividad.fecha_inicio >= fecha_inicial:
            if actividad.fecha_inicio <= fecha_final:
                print(actividad)

# ##Datos de prueba
# from actividad_proyecto_data import proyecto, personas

# #15.a
# promedio = tiempo_promedio_actividades(proyecto)
# print('\nTiempo promedio de actividades: {} dias'.format(promedio))
# #15.b
# total = costo_total(proyecto)
# print('\nCosto total del proyecto ${}'.format(total))
# #15.c
# print('\nActividades realizadas por {}'.format(personas[0].nombre_completo))
# actividades_a_cargo_de(personas[0], proyecto)

# #15.d
# print('\nActividades entre 1-ene-2019 y 1-jul-2019')
# import datetime
# fecha_inicial = datetime.date(2019, 1, 1)
# fecha_final = datetime.date(2019, 7, 1)
# actividades_entre_fechas(proyecto, fecha_inicial, fecha_final)


