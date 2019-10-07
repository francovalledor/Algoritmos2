from lista import Lista

class Conjunto:
    def __init__(self, *valores):
        self.__elementos = Lista()
        for valor in valores:
            self.agregar(valor)

    def agregar(self, elemento):
        if elemento not in self:
            self.__elementos.inserta(elemento)

    def descartar(self, elemento):
        """elimina "elemento" del conjunto, si este no pertenece no hace nada"""
        if elemento in self:
            posicion = self.__elementos.localiza(elemento)
            self.__elementos.suprime(posicion)

    def quitar(self, elemento):
        """elimina "elemento" del conjunto, si este no pertenece lanza KeyError"""
        if elemento in self:
            self.descartar(elemento)
        else:
            raise KeyError('El elemento no pertenece al conjunto')

    def __len__(self):
        return len(self.__elementos)

    def __contains__(self, elemento):
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
        Devuelve un conjunto como union de ambos conjuntos
        """
        self.__igual_tipo(otro)

        union = Conjunto()
        for elemento in self.__elementos:
            union.agregar(elemento)

        for elemento in otro.__elementos:
            union.agregar(elemento)

        return union

    def interseccion(self, otro):
        """
        Devuelve la interseccion de ambos conjuntos
        """
        self.__igual_tipo(otro)
        interseccion = Conjunto()

        for elemento in self.__elementos:
            if elemento in otro:
                interseccion.agregar(elemento)

        return interseccion

    def diferencia(self, otro):
        """
        Devuelve la diferencia de ambos conjuntos
        """
        self.__igual_tipo(otro)

        diferencia = Conjunto()

        for elemento in self.__elementos:
            if elemento not in otro:
                diferencia.agregar(elemento)

        return diferencia

    def diferencia_simetrica(self, otro):
        """
        Devuelve la diferencia simetrica de ambos conjuntos
        """
        self.__igual_tipo(otro)

        diferencia = Conjunto()

        for elemento in self.__elementos:
            if elemento not in otro:
                diferencia.agregar(elemento)

        for elemento in otro.__elementos:
            if elemento not in self:
                diferencia.agregar(elemento)

        return diferencia

    def __add__(self, otro):
        """emula operador (+)"""
        return self.union(otro)

    def __sub__(self, otro):
        """emula operador (-)"""
        return self.diferencia(otro)

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
        return self.interseccion(otro)

    def __or__(self, otro):
        """ return self | otro """
        return self.union(otro)

    def __gt__(self, otro):
        """ return self>otro """
        self.__igual_tipo(otro)
        return (self.es_superconjunto_de(otro) and not (self - otro).es_vacio())

    def __ge__(self, otro):
        """ return self>=otro """
        self.__igual_tipo(otro)
        return self.es_superconjunto_de(otro)

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


    def es_subconjunto_de(self, otro):
        self.__igual_tipo(otro)
        return (self - otro).es_vacio()


    def es_superconjunto_de(self, otro):
        self.__igual_tipo(otro)
        return (otro - self).es_vacio()

    
    def es_vacio(self):
        return (len(self) == 0)
    
    def es_disjunto_con(self, otro):
        return self.interseccion(otro).es_vacio()

    def vaciar(self):
        self.__init__()

    
    def copia(self):
        return self.union(Conjunto())


    def pop(self):
        if self.es_vacio():
            raise KeyError('Conjunto vacio')
        else:
            a = self.__elementos[0]
            del self.__elementos[0]
            return a

