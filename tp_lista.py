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



#ej16
def filtrar_por_destino(destino, vuelos):
    destino = destino.upper()
    for vuelo in vuelos:
        if vuelo.destino.upper() == destino:
            print(vuelo)

def asientos_turista_disponibles(vuelos):
    for vuelo in vuelos:
        if vuelo.cant_turista_disponibles() > 0:
            print('Vuelo {:^8} Destino: {:26.24} Disponibles: {}'.format(vuelo.nro_vuelo, vuelo.destino, vuelo.cant_turista_disponibles()))

def filtrar_por_fechas(fecha_inicial, fecha_final, vuelos):
    for vuelo in vuelos:
        if fecha_inicial <= vuelo.fecha:
            if vuelo.fecha <= fecha_final:
                print(vuelo)

def vender_pasaje_turista(persona, vuelo):
    nro_asiento = vuelo.vender_turista(persona)
    print('Total a pagar: ${}'.format(vuelo.precio_turista))
    print('Nro Asiento: {}'.format(nro_asiento))

def eliminar_vuelo(indice, vuelos):
    vuelos[indice].cancelar()
    del vuelos[indice]


#DATOS DE PRUEBA
# from aeropuerto_data import vuelos
# import datetime

# #16.a
# print('Filtrar vuelos a Atenas')
# filtrar_por_destino('Atenas', vuelos)

# #16.b
# print('Filtrar vuelos con asientos turistas disponibles')
# asientos_turista_disponibles(vuelos)

# #16.c
# #Se muestra al imprimir cada vuelo

# #16.d
# hoy = datetime.date.today()
# fecha_inicial =  datetime.datetime(hoy.year, hoy.month, hoy.day)
# fecha_final = fecha_inicial + datetime.timedelta(days=2) 
# print('Vuelos entre fechas')
# filtrar_por_fechas(fecha_inicial, fecha_final, vuelos)

# #16.e
# print('Vender un pasaje turista para JUAN PEREZ')
# vender_pasaje_turista('Juan Perez', vuelos[0])

# #16.f
# print('Eliminar un vuelo')
# print(vuelos[0])
# eliminar_vuelo(0, vuelos)

#ej17
def buscar_por_codigo(codigo, listado_local):
    """ Devuelve el producto o None"""
    retorno = None
    for producto in listado_local:
        if producto.codigo == codigo:
            retorno = producto
            break
    return retorno

def agregar_productos(productos_nuevos, listado_local):
    for producto in productos_nuevos:
        codigo = producto.codigo
        producto_en_local = buscar_por_codigo(codigo, listado_local)
        if (producto_en_local == None):
            listado_local.append(producto)
        else:
            producto_en_local.cantidad_stock += producto.cantidad_stock 

def eliminar_por_tipo_y_marca(tipo, marca, listado_local):
    tipo = tipo.upper()
    marca = marca.upper()
    i = 0
    while i < len(listado_local):
        if listado_local[i].tipo.upper() == tipo:
            if listado_local[i].marca.upper() == marca:
                print('eliminando: ')
                print(listado_local[i])
                del listado_local[i]
                continue
        i += 1

def intercambiar(a, b):
    return (b, a)

def ordenar_por_tipo_y_marca(listado_local):
    def func(actual, siguiente):
        return (actual.tipo + actual.marca) > (siguiente.tipo + siguiente.marca)
    listado_local.sort_func(func)

def ordenar_por_marca_y_tipo(listado_local):
    def func(actual, siguiente):
        return (actual.marca + actual.tipo) > (siguiente.marca + siguiente.tipo)
    listado_local.sort_func(func)

def costo_de_existencia_por_tipo(tipo, listado_local):
    tipo = tipo.upper()
    total = 0
    for producto in listado_local:
        if tipo in producto.tipo.upper():
            total += producto.precio * producto.cantidad_stock
    return total

##DATOS DE PRUEBA
# from localdata import productos as listado_local
# from localdata import Producto, proveedorA, proveedorB
# #17.a
# # Agregar productos de proveedores A y B
# agregar_productos(proveedorA, listado_local)
# agregar_productos(proveedorB, listado_local)
# for producto in listado_local:
#     print(producto)

# #17.b
# # Eliminar todos los productos de tipo "PEN DRIVE" y marca "KINGSTON"
# eliminar_por_tipo_y_marca('PEN DRIVE', 'KINGSTON', listado_local)

#17.c
# Ordenar por tipo y marca
# ordenar_por_marca_y_tipo(listado_local)
# for producto in listado_local:
#     print('{:20.18} {:15.14} {:40.40}'.format(producto.tipo, producto.marca, producto.modelo))

# print('-'*80)
# ordenar_por_tipo_y_marca(listado_local)
# for producto in listado_local:
#     print('{:20.18} {:15.14} {:40.40}'.format(producto.tipo, producto.marca, producto.modelo))

#17.d
#Obtener costo de existencia de "DISCO SOLIDO" y de "TECLADO WIRELESS"
# print(costo_de_existencia_por_tipo('DISCO SOLIDO', listado_local))
# print(costo_de_existencia_por_tipo('TECLADO WIRELESS', listado_local))



#ej18
def usuario_mas_commits(usuarios):
    mayor = usuarios[0]
    for usuario in usuarios:
        if usuario.cant_commits() > mayor.cant_commits():
            mayor = usuario

    lista_mayores = Lista()
    for usuario in usuarios:
        if usuario.cant_commits() == mayor.cant_commits():
            lista_mayores.append(usuario)
        
    return lista_mayores


def usuario_mas_lineas_agregadas(usuarios):
    mayor = usuarios[0]
    for usuario in usuarios:
        if usuario.cant_lineas_agregadas() > mayor.cant_lineas_agregadas():
            mayor = usuario
    
    return mayor


def usuario_menos_lineas_eliminadas(usuarios):
    menor = usuarios[0]
    for usuario in usuarios:
        if usuario.cant_lineas_eliminadas() < menor.cant_lineas_eliminadas():
            menor = usuario
    
    return menor


def usuarios_commit_cero_lineas(usuarios):
    lista_cero_lineas = Lista()
    for usuario in usuarios:
        for commit in usuario.commits:
            if commit.agregadas == 0:
                if commit.eliminadas == 0:
                    lista_cero_lineas.append(usuario)
                    break
    
    return lista_cero_lineas


def cambios_archivo_entre_fechas(archivo, fecha_inicial, fecha_final, usuarios):
    usuarios_cambios = Lista()
    for usuario in usuarios:
        for commit in usuario.commits:
            if commit.nombre_archivo == archivo:
                if  commit.timestamp >= fecha_inicial:
                    if  commit.timestamp <= fecha_final:
                        usuarios_cambios.append(usuario)
                        break

    return usuarios_cambios


#DATOS DE PRUEBA
# from commitdata import usuarios
# import datetime
# #18.a
# #Obtener el usuario con mayor cantidad de commits (podría ser más de uno).
# mas_commits = usuario_mas_commits(usuarios)
# for usuario in mas_commits:
#     print(usuario)

# # 18.b
# # Obtener el usuario que haya agregado mayor cantidad de líneas y el que haya 
# # eliminado menor cantidad de líneas.
# usuario = usuario_mas_lineas_agregadas(usuarios)
# print(usuario)
# print('{} lineas agregadas'.format(usuario.cant_lineas_agregadas()))

# usuario = usuario_menos_lineas_eliminadas(usuarios)
# print(usuario)
# print('{} lineas eliminadas'.format(usuario.cant_lineas_eliminadas()))


# #18.c
# #Los usuarios que realizaron cambios sobre el archivo “Test.py” despues de las
# #“19:45”.
# hoy = datetime.date.today()
# fecha_inicial =  datetime.datetime(hoy.year, hoy.month, hoy.day, 19, 45)
# fecha_final = fecha_inicial + datetime.timedelta(days=2)
# archivo = 'Test.py'

# listado = cambios_archivo_entre_fechas(archivo, fecha_inicial, fecha_final, usuarios)
# for usuario in listado:
#     print(usuario)

# #18.d
# #Los usuarios que hayan realizado al menos un commit con cero líneas
# #agregados/eliminadas.
# listado = usuarios_commit_cero_lineas(usuarios)
# for usuario in listado:
#     print(usuario)
#     # for commit in usuario.commits:
#     #     print(commit)



#ej19
def palindromo_lista_circular(palabra):
    lista1 = lc()
    lista2 = lc()
    palabra = palabra.upper()
    for letra in palabra:
        lista1.insert(letra)
        lista2.insert(letra)
    
    es_palindromo = True
    lista2.retroceder()
    for i in range(0,len(lista1)):
        if lista1.actual.data != lista2.actual.data:
            es_palindromo = False
            break
        lista1.avanzar()
        lista2.retroceder()

    return es_palindromo

# #DATOS DE PRUEBA
# palabras = Lista('menem', 'neuqUen', 'telefono', 'ana', 'anana', 'nana')

# for palabra in palabras:
#     print(palindromo_lista_circular(palabra))



#EJ 20
def ordenar_por_nombre(productos):
    def func(actual, siguiente):
        retorno = False
        if actual.nombre > siguiente.nombre:
            retorno = True
        return retorno

    productos.sort_func(func)


def ordenar_por_calificacion(productos):
    def func(actual, siguiente):
        retorno = False
        if actual.calificacion > siguiente.calificacion:
            retorno = True
        return retorno

    productos.sort_func(func)


def separar_por_calificacion(productos):
    clasificados = Lista()
    max_calificacion = 5
    for i in range(0, max_calificacion+1):
        clasificados.append(Lista())

    for producto in productos:
        clasificados[producto.calificacion].append(producto)

    return clasificados


def producto_mas_barato(productos):
    menor_precio = productos[0]
    for producto in productos:
        if producto.precio < menor_precio.precio:
            menor_precio = producto
    
    return menor_precio


def filtrar_por_inicial(inicial, productos):
    inicial = inicial.upper()
    for producto in productos:
        if producto.nombre[0].upper() == inicial:
            print(producto)

# #DATOS DE PRUEBA
# from productos_data import productos

# #20.a
# #Mostrar los datos de un determinado producto.
# print(productos[0])

# #20.b
# #Poder cambiar el orden de los elementos de la lista por nombre o calificación.
# ordenar_por_nombre(productos)
# for producto in productos:
#     print(producto)

# ordenar_por_calificacion(productos)
# for producto in productos:
#     print(producto)

# #20.c
# #Mostrar un listado ordenado por clasificación de producto (debe utilizar una lista
# #auxiliar).
# clasificados = separar_por_calificacion(productos)
# for producto in clasificados[3]: #3 estrellas
#     print(producto)

# #20.d
# #Mostrar el producto más barato de calificación 3.
# clasificados = separar_por_calificacion(productos)
# mas_barato = producto_mas_barato(clasificados[3])
# print(mas_barato)