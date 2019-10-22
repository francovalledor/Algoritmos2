from lista import Lista
import locale
from localdata import productos as otros_prod
import random

locale.setlocale(locale.LC_ALL, '')  

class Producto:
    def __init__(self, nombre, precio, calificacion):
        self.nombre = nombre
        self.precio = precio
        self.calificacion = calificacion
    
    def __repr__(self):
        texto = '-'*80
        texto += '\n\n'
        texto += '{:40.40} {}'.format(self.nombre, locale.currency(self.precio))
        texto += '\n{} Estrellas'.format(repr(self.calificacion))
        texto += '\n'
        texto += '-'*80
        return texto


productos = Lista()
for item in otros_prod:
    estrellas = random.randint(1,5)
    productos.append(Producto(item.modelo, item.precio, estrellas))
