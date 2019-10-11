from lista import Lista
from conjunto import Conjunto
from random import randint

#ej1
def contar_cantidad_nodos(lista:Lista):
    """Cuenta la cantidad de nodos de una lista"""
    return len(lista)

#ej2
def eliminar_vocales_lista(caracteres:Lista):
    VOCALES = 'AEIOUaeiou'
    i = 0
    while i < len(caracteres):
        if caracteres[i] in VOCALES:
            caracteres.suprime(i)
        else:
            i += 1
        #Existe una manera mas eficiente de hacerlo trabajando a bajo nivel

#ej3
def dividir_pares_impares(numeros_enteros: Lista):
    pares = Lista()
    impares = Lista()

    for numero in numeros_enteros:
        if numero % 2 == 0:
            pares.insert(numero)
        else:
            impares.insert(numero)
    return pares, impares

#ej4
def inserta_en_iesima(elemento, posicion, lista:Lista):
    lista.insert(elemento, posicion)


#ej5
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

def eliminar_primos(numeros_enteros:Lista):
    i = 0
    while i < len(numeros_enteros):
        if es_primo(numeros_enteros[i]):
            numeros_enteros.suprime(i)
        else:
            i += 1

#ej6
class SuperHeroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

def ej6(superheroes:Lista):
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

#ej7
def concatenar_listas(lista1:Lista, lista2:Lista, omitir_repetidos=False):
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


def contar_repetidos(lista1:Lista, lista2:Lista):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    return len(conjunto1.intersection(conjunto2))

def eliminar_todos_nodos(lista:Lista):
    i = 0
    while i < len(lista):
        lista.suprime(0)


#ej8
def ej8(cuantos_numeros):
    import random
    def generar():
        INICIO = -999
        FIN = 999
        return random.randint(INICIO, FIN)
        
    numeros =  Lista()

    
    while numeros.tamanio() < cuantos_numeros:
        siguiente = generar()
        
        #REGLAS
        if siguiente in numeros:    #Repetido
            continue
        elif es_primo(siguiente):   #Primo
            if (numeros.tamanio() == 0) or (numeros.tamanio() + 1 == cuantos_numeros) :
                continue
            elif abs(numeros.recupera(numeros.fin()-1) - siguiente) > 14:
                numeros.insert(siguiente)
                anterior = siguiente
                while abs(anterior - siguiente) <= 14:
                    siguiente = generar()
                numeros.insert(siguiente)
            else:
                continue
        elif siguiente % 2 != 0:    #Impar no primo
            if (numeros.tamanio() == 0) or (numeros.tamanio() + 1 == cuantos_numeros) :
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

#ej11
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

#ej12
"""
Desarrollar un algoritmo que permita visualizar el contenido de una lista de 
manera ascendente y descendente de sus elementos, debe implementar lista 
doblemente enlazada.
"""
from lista_de import Lista as Lde
def visualizar_lista(lista:Lde, descendente=False):
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

