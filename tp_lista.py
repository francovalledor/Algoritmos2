from lista import Lista

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

#ej3
def dividir_pares_impares(numeros_enteros: Lista):
    pares = Lista()
    impares = Lista()

    for numero in numeros_enteros:
        if numero % 2 == 0:
            pares.inserta(numero)
        else:
            impares.inserta(numero)
    return pares, impares

#ej4
def inserta_en_iesima(elemento, posicion, lista:Lista):
    lista.inserta(elemento, posicion)


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
                lista_aux.inserta(lista2[i])
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
                numeros.inserta(siguiente)
                anterior = siguiente
                while abs(anterior - siguiente) <= 14:
                    siguiente = generar()
                numeros.inserta(siguiente)
            else:
                continue
        elif siguiente % 2 != 0:    #Impar no primo
            if (numeros.tamanio() == 0) or (numeros.tamanio() + 1 == cuantos_numeros) :
                continue
            elif numeros.recupera(numeros.fin()-1) % 2 == 0:
                numeros.inserta(siguiente)
                while siguiente % 2 != 0:
                    siguiente = generar()
                numeros.inserta(siguiente)
            else:
                continue
        else:
            numeros.inserta(siguiente)
    return numeros

#ej10
