from lista import Lista

class Conjunto:
    def __init__(self, *valores):
        self.__elementos = Lista()
        for valor in valores:
            self.add(valor)

    def add(self, elemento):
        """
        Add an element to a set.
        This has no effect if the element is already present.
        """
        if elemento not in self:
            self.__elementos.insert(elemento)

    def __iand__(self, otro):
        """
        Return self&=value.
        """
        return self.__and__(otro)

    def __rand__(self, otro):
        """
        Return value&=self.
        """
        return self.__and__(otro)

    def discard(self, elemento):
        """elimina "elemento" del conjunto, si este no pertenece no hace nada"""
        if elemento in self:
            posicion = self.__elementos.localiza(elemento)
            self.__elementos.suprime(posicion)

    def remove(self, elemento):
        """elimina "elemento" del conjunto, si este no pertenece lanza KeyError"""
        if elemento in self:
            self.discard(elemento)
        else:
            raise KeyError('El elemento no pertenece al conjunto')

    def __len__(self):
        return len(self.__elementos)

    def __contains__(self, elemento):
        """
        x.__contains__(y) <==> y in x.
        """
        return (elemento in self.__elementos)

    def __repr__(self) -> str:
        strElementos = ''
        if len(self.__elementos) > 0:
            for elemento in self.__elementos:
                strElementos += repr(elemento) + ', '
            strElementos = strElementos[0:-2]

        representacion = '{self.__class__.__name__}({strElementos})'.format(
            self=self, strElementos=strElementos)
        return representacion

    def union(self, otro):
        """
        Return the union of sets as a new set.
        """
        self.__igual_tipo(otro)

        union = Conjunto()
        for elemento in self.__elementos:
            union.add(elemento)

        for elemento in otro.__elementos:
            union.add(elemento)

        return union

    def intersection(self, otro):
        """
        Devuelve la interseccion de ambos conjuntos
        """
        self.__igual_tipo(otro)
        interseccion = Conjunto()
        for elemento in self.__elementos:
            if elemento in otro:
                interseccion.add(elemento)
        return interseccion

    def intersection_update(self, otro):
        """
        Update a set with the intersection of itself and another.
        """
        self.__igual_tipo(otro)
        for elemento in self.__elementos:
            if elemento not in otro:
                self.remove(elemento)
        return interseccion

    def difference(self, otro):
        """
        Return the difference of two or more sets as a new set.
        (i.e. all elements that are in this set but not the others.)
        """
        self.__igual_tipo(otro)
        diferencia = Conjunto()
        for elemento in self.__elementos:
            if elemento not in otro:
                diferencia.add(elemento)
        return diferencia

    def difference_update(self, otro):
        """
        Remove all elements of another set from this set.
        """
        self.__igual_tipo(otro)
        for elemento in otro.__elementos:
            if elemento in self:
                self.remove(elemento)

    def symmetric_difference(self, otro):
        """
        Return the symmetric difference of two sets as a new set.
        """
        self.__igual_tipo(otro)
        diferencia = Conjunto()
        for elemento in self.__elementos:
            if elemento not in otro:
                diferencia.add(elemento)

        for elemento in otro.__elementos:
            if elemento not in self:
                diferencia.add(elemento)
        return diferencia


    def symmetric_difference_update(self, otro):
        """
        Return the symmetric difference of two sets as a new set.
        """
        self.__igual_tipo(otro)
        diferencia = Conjunto()
        for elemento in self.__elementos:
            if elemento not in otro:
                diferencia.add(elemento)

        for elemento in otro.__elementos:
            if elemento not in self:
                diferencia.add(elemento)

        self.__elementos = diferencia.__elementos

    def __add__(self, otro):
        """emula operador (+)"""
        return self.union(otro)

    def __sub__(self, otro):
        """emula operador (-)"""
        return self.difference(otro)

    def __rsub__(self, otro):
        """Return value-self."""
        return self.difference(otro)

    def __eq__(self, otro):
        """ return self == otro """
        son_iguales = False
        if type(self) == type(otro):
            if len(self) == len(otro):
                son_iguales = True
                for elemento in self.__elementos:
                    if elemento not in otro:
                        son_iguales = False
                        break
        return son_iguales

    def __and__(self, otro):
        """ return self & otro """
        return self.intersection(otro)

    def __or__(self, otro):
        """ return self | otro """
        return self.union(otro)

    def __ror__(self, otro): 
        """ return otro | self """
        return self.__or__(otro)

    def __gt__(self, otro):
        """ return self>otro """
        self.__igual_tipo(otro)
        return (self.issuperset(otro) and not (self - otro).is_empty())

    def __ge__(self, otro):
        """ return self>=otro """
        self.__igual_tipo(otro)
        return self.issuperset(otro)

    def __igual_tipo(self, otro):
        """
        comprueba que ambos objetos sean del mismo tipo,
        en caso contrario lanza una excepción TypeError
        """
        if not (type(otro) == type(self)):
            raise TypeError('Ambos deben ser conjuntos (%s y %s)' %
                            (type(otro), type(self)))

    def __iter__(self):
        """Iterator (para bucle "for in")"""
        return iter(self.__elementos)


    def issubset(self, otro):
        """
        Report whether another set contains this set.
        """
        self.__igual_tipo(otro)
        return (self - otro).is_empty()


    def issuperset(self, otro):
        """
        Report whether this set contains another set.
        """
        self.__igual_tipo(otro)
        return (otro - self).is_empty()

    
    def is_empty(self):
        return (len(self) == 0)
    
    def isdisjoint(self, otro):
        """
        Return True if two sets have a null intersection.
        """
        return self.intersection(otro).is_empty()

    def clear(self):
        """Remove all elements from this set."""
        self.__init__()

    
    def copy(self):
        """
        Return a shallow copy of a set.
        """
        return self.union(Conjunto())


    def pop(self):
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        if self.is_empty():
            raise KeyError('Conjunto vacio')
        else:
            a = self.__elementos[0]
            del self.__elementos[0]
            return a


    def update(self, *iterables):
        """
        Update a set with the union of itself and others
        """
        for grupo in iterables:
            for elemento in grupo:
                self.add(elemento)


    def __xor__(self, otro):
        """
        Return self^value.
        """
        return self.union(otro) - self.intersection(otro)

    def __ixor__(self, otro):
        """
        Return self^=value.
        """
        return self.__xor__(otro)

    def __rxor__(self, otro):
        """
        Return value^=self.
        """
        return self.__xor__(otro)

con = Conjunto(1,2,3,4,5)
con2 = Conjunto(4,5,6,7,'d')
con.symmetric_difference_update(con2)