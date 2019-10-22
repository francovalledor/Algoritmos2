from lista import Lista
import datetime
from nombresdata import nombres
import random
from archivos_data import archivos
class Commit:
    def __init__(self, timestamp, mensaje, nombre_archivo, agregadas, eliminadas):
        self.timestamp = timestamp
        self.mensaje = mensaje
        self.nombre_archivo = nombre_archivo
        self.agregadas = agregadas
        self.eliminadas = eliminadas

    def __repr__(self):
        texto = '-'*80
        texto += '\n\n'
        texto += 'MENSAJE:            {}'.format(self.mensaje)
        texto += '\nARCHIVO:            {:15.15}'.format(repr(self.nombre_archivo))
        texto += '\nLINEAS MODIFICADAS: +{} -{}'.format(self.agregadas, self.eliminadas)
        texto += '\nTIMESTAMP:          {}'.format(self.timestamp.strftime('%d-%m-%Y %H:%M'))
        texto += '\n'
        texto += '-'*80
        return texto

class Usuario:
    def __init__(self, nombre_usuario):
        self.nombre = nombre_usuario
        self.commits = Lista()
    
    def nuevo_commit(self, timestamp, mensaje, nombre_archivo, agregadas, eliminadas):
        self.commits.append(Commit(timestamp, mensaje, nombre_archivo, agregadas, eliminadas))

    def __repr__(self):
        texto = '-'*80
        texto += '\n\n'
        texto += '{:25.20}'.format(self.nombre)
        texto += '{} commits'.format(len(self.commits))
        texto += '\n'
        texto += '-'*80
        return texto

    def cant_lineas_agregadas(self):
        suma = 0
        for commit in self.commits:
            suma += commit.agregadas
        
        return suma

    
    def cant_lineas_eliminadas(self):
        suma = 0
        for commit in self.commits:
            suma += commit.eliminadas
        
        return suma

    def cant_commits(self):
        return len(self.commits)
    
# Fechas
hoy = datetime.date.today()
fecha = datetime.datetime(hoy.year, hoy.month, hoy.day)

fechas = Lista()
fechas.append(fecha)
for i in range(1, 90*24*4):
    fecha += datetime.timedelta(minutes=15)
    fechas.append(fecha)

usuarios = Lista()
for i in range(0, 100):
    nombre_usuario = random.choice(nombres)
    usuarios.append(Usuario(nombre_usuario))

for usuario in usuarios:
    for i in range(0, random.randint(0, 100)):
        timestamp = random.choice(fechas)
        mensaje = 'mensaje'
        archivo = random.choice(archivos)
        agregadas = random.randint(0,100)
        eliminadas = random.randint(0,100)
        usuario.nuevo_commit(timestamp, mensaje, archivo, agregadas, eliminadas)
