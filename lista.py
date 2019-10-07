"""
Implementación del TDA según 
"Estructuras de Datos y Algoritmos - A. Aho, J. Hopcroft, J. Ullman - Pearson - 1998"

"""


class Nodo:
    def __init__(self, data=None, siguiente=None):
        self.data = data
        self.siguiente = siguiente


class Lista:
    POSICION_NO_VALIDA = IndexError('la posicion ingresada no es valida')
    ELEMENTO_NO_ENCONTRADO = ValueError(
        'El elemento no se encuentra en la lista')

    def __init__(self, *elementos):
        """
        Crea una lista con los elementos pasados
        """
        self.frente = Nodo()
        self.tamanio = 0
        self.__ultimo__ = self.frente

        for elemento in elementos:
            self.inserta(elemento)

    def __len__(self):
        """Return len(self)."""
        return self.tamanio

    def __get_nodo(self, posicion):
        if (posicion < 0) or (posicion >= len(self)):
            raise self.POSICION_NO_VALIDA
        else:
            actual = self.frente
            for i in range(0, posicion+1):
                actual = actual.siguiente
            return actual

    def inserta(self, elemento, posicion=None):
        """
        Inserta el elemento "elemento" en la posicion "posicion" pasando los 
        elementos de "posicion" y posteriores un casillero hacia adelante

        Si se omite "posicion" el elemento es insertado al final de la lista
        """
        if posicion == None:
            posicion = len(self)
        elif (posicion > len(self)) or posicion < 0:
            raise self.POSICION_NO_VALIDA

        aux = Nodo(elemento)
        if posicion == len(self):
            self.__ultimo__.siguiente = aux
            self.__ultimo__ = aux
        elif posicion == 0:
            aux.siguiente = self.frente.siguiente
            self.frente.siguiente = aux
        else:
            anterior = self.__get_nodo(posicion-1)
            aux.siguiente = anterior.siguiente
            anterior.siguiente = aux

        self.tamanio += 1

    def localiza(self, elemento):
        """
        Devuelve la posicion de la priera aparición de "elemento" en la lista.
        Lanza exepción ValueError si elm elemento no está en la lista
        """
        actual = self.frente
        posicion = -1

        while not (actual.siguiente == None):
            if actual.data == elemento:
                break
            posicion += 1
            actual = actual.siguiente
        else:
            raise self.ELEMENTO_NO_ENCONTRADO

        return posicion

    def recupera(self, posicion):
        """
        Devuelve el elemento que está en la posición "posicion"
        Lanza "IndexError" si esa posicion no existe en la lista
        """
        return self.__get_nodo(posicion).data

    def suprime(self, posicion):
        """
        Elimina el elemento de la posición "posicion"
        Todas las posiciones posteriores a "posicion" son corridas a la 
        izquierda 1 casillero
        """
        if posicion == 0:
            anterior = self.frente
        elif (posicion > 0) and (posicion < len(self)):
            anterior = self.__get_nodo(posicion-1)
        else:
            raise self.POSICION_NO_VALIDA
        anterior.siguiente = anterior.siguiente.siguiente
        self.tamanio -= 1

    def modifica(self, posicion, valor):
        """ Modifica el valor de un elemento"""
        self.__get_nodo(posicion).data = valor

    def anula(self):
        """
        Convierte la lista en una lista vacía
        """
        self.tamanio = 0
        self.frente.siguiente = None

    def tamanio(self):
        """ Devuelve la cantidad de elementos que hay en la lista """
        return len(self)

    def copia(self):
        """ Devuelve una copia de la lista"""
        copia = Lista()
        for elemento in self:
            copia.inserta(elemento)
        return copia

    def reversa(self):
        """ Devuelve una copia de la lista en orden inverso"""
        nueva_lista = Lista()
        for elemento in self:
            nueva_lista.inserta(elemento, 0)
        return nueva_lista

    def __repr__(self) -> str:
        strElementos = ''
        if len(self) > 0:
            for elemento in self:
                strElementos += repr(elemento) + ', '
            strElementos = strElementos[0:-2]

        representacion = '{self.__class__.__name__}({strElementos})'.format(
            self=self, strElementos=strElementos)
        return representacion

    def __getitem__(self, posicion):
        """x.__getitem__(y) <==> x[y]"""
        if type(posicion) == slice:
            paso = 1
            inicio = posicion.start
            fin = posicion.stop
            if posicion.step:
                if type(posicion.step) == int and posicion.step > 0:
                    paso = posicion.step
                else:
                    raise ValueError('"step" debe ser de tipo "int"')

            if posicion.start == None:
                inicio = 0
            elif posicion.start < 0:
                inicio = len(self)+posicion.start

            if posicion.stop == None:
                fin = len(self)
            elif posicion.stop < 0:
                fin = len(self)+posicion.stop

            sublista = Lista()
            i = inicio
            while i < fin:
                sublista.inserta(self.recupera(i))
                i += paso
            return sublista

        else:
            if posicion < 0:
                posicion = len(self)+posicion
            return self.recupera(posicion)

    def __setitem__(self, posicion, valor):
        if type(posicion) == slice:
            paso = 1
            inicio = posicion.start
            fin = posicion.stop
            if posicion.step:
                if type(posicion.step) == int and posicion.step > 0:
                    paso = posicion.step
                else:
                    raise ValueError('"step" debe ser de tipo "int"')

            if posicion.start < 0:
                inicio = len(self)+posicion.start

            if posicion.stop < 0:
                fin = len(self)+posicion.stop

            i = inicio
            while i < fin:
                self.modifica(i, valor)
                i += paso

        else:
            self.modifica(posicion, valor)

    def __delitem__(self, posicion):
        """Delete self[key]."""
        self.suprime(posicion)


    def __add__(self, otra):
        """Return self+value"""
        if type(otra) == type(self):
            suma = self.copia()
            for elemento in otra:
                suma.inserta(elemento)
            return suma
        else:
            raise TypeError('No se pueden sumar %s y %s' %
                            (type(self), type(otra)))


    def __contains__(self, valor):
        """Return key in self."""
        retorno = False

        for elemento in self:
            if elemento == valor:
                retorno = True
                break

        return retorno

    def __eq__(self, otra):
        """Return self==value."""
        es_igual = False
        if (type(otra) == type(self)) and (len(self) == len(otra)):
            es_igual = True
            for i in range(0, len(self)):
                if self[i] != otra[i]:
                    es_igual = False
                    break

        return es_igual


    def __gt__(self, otra):
        """Return self>value."""
        es_mayor = False
        if (type(otra) == type(self)) and (len(self) > len(otra)):
            es_mayor = True
            for i in range(0, len(otra)):
                    if self[i] != otra[i]:
                        es_mayor = False
                        break
        return es_mayor

    
    def __ge__(self, otra):
        """Return self>=value."""
        return (self.__gt__(otra) or self.__eq__(otra))


    def __iadd__(self, otra):
        """Implement self+=value."""
        if (type(otra) == type(self)):
            for elemento in otra:
                self.inserta(elemento)
        else:
            raise TypeError('Solo se puede sumar a otro %s'%(type(self)))
        return self


    def __imul__(self, entero):
        """Implement self*=value."""
        if type(entero) != int:
            raise TypeError('La Lista solo se puede multiplicar por un entero')
        else:
            aux = Lista()
            for i in range(0, entero):
                aux += self.copia()
        return aux

    def __le__(self, otra):
        """Return self<=value."""
        return otra > self
    
    def __mul__(self, entero):
        """Return self*value."""
        return self.__imul__(entero)

    def __ne__(self, otra):
        """Return self!=value."""
        return not (self == otra)
    
    def __rmul__(self, entero):
        """Return entero*self."""
        return self*entero

    def append(self, elemento):
        """Append object to the end of the list."""
        return self.inserta(elemento)

    def clear(self):
        """Remove all items from list."""
        self.__init__()

    def copy(self):
        """Return a shallow copy of the list."""
        return self.copia()

    def count(self, valor):
        """Return number of occurrences of value."""
        contador = 0
        for elemento in self:
            if elemento == valor:
                contador += 1
        
        return contador

    
    def extend(self, objeto_iterable):
        """Extend list by appending elements from the iterable."""
        for elemento in objeto_iterable:
            self.inserta(elemento)                


    def index(self, valor, start=None, stop=None):
        """
        Return first index of value.
        Raises ValueError if the value is not present.
        """
        if start == None:
            start = 0
        if stop == None:
            stop = len(self)
        aux = self[start:stop]
        print(aux)
        return start + aux.localiza(valor)

    # ITERATOR
    def __iter__(self):
        self._iter_actual = self.frente
        return self

    def __next__(self):
        if self._iter_actual.siguiente == None:
            raise StopIteration
        else:
            self._iter_actual = self._iter_actual.siguiente
            retorno = self._iter_actual.data
            return retorno


a = Lista(1,2,3,4,5,2)
b = Lista(6,7,8,9)

print(a.index(2, start=3))

print(a)