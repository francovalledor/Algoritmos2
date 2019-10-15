class Nodo:
    def __init__(self, data=None, anterior=None, siguiente=None):
        self.data = data
        self.anterior = anterior
        self.siguiente = siguiente
    def __repr__(self):
        return repr(self.data)


class Lista:
    POSICION_NO_VALIDA = IndexError('la posicion ingresada no es valida')
    ELEMENTO_NO_ENCONTRADO = ValueError(
        'El elemento no se encuentra en la lista')

    def __init__(self, *elementos):
        """
        Crea una lista doblemente enlazada con los elementos pasados
        """
        self.actual = None
        self.tamanio = 0

        for elemento in elementos:
            self.insert(elemento)

    def __len__(self):
        """Return len(self)."""
        return self.tamanio

    def insert(self, valor, despues_de:Nodo=None):
        """
        Insert an element in a given position
        """
        if len(self)== 0:
            aux = Nodo(valor)
            aux.siguiente = aux
            aux.anterior = aux
            self.actual = aux
        else:
            if despues_de==None:
                despues_de = self.actual.anterior

            aux = Nodo(valor, despues_de, despues_de.siguiente)
            despues_de.siguiente.anterior = aux
            despues_de.siguiente = aux
        self.tamanio += 1

    def remove(self, nodo:Nodo):
        """
        Remove a node
        """
        if len(self)==0:
            raise IndexError('No quedan elementos en la lista')
        else:
            nodo.siguiente.anterior = nodo.anterior 
            nodo.anterior.siguiente = nodo.siguiente
            self.tamanio -= 1
            if nodo == self.actual:
                self.actual = nodo.siguiente

    def avanzar(self):
        self.actual = self.actual.siguiente
    
    def retroceder(self):
        self.actual = self.actual.siguiente


    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration
        elif self.actual.siguiente == None:
            raise StopIteration
        else:
            retorno = self.actual.data 
            self.actual = self.actual.siguiente
            return retorno
