class Persona:
    def __init__(self, nombre_completo, DNI, direccion=None, telefono=None):
        self.nombre_completo = nombre_completo
        self.DNI = DNI
        self.direccion = direccion
        self.telefono = telefono

    def __repr__(self):
        return repr('{} - {}'.format( self.nombre_completo, self.DNI))


class Actividad:
    def __init__(self, nombre, costo, tiempo_estimado, fecha_inicio, persona_a_cargo):
        """
        Actividad de proyecto
        nombre: (str) Nombre de la actividad
        costo:  (float) Costo de la actividad
        tiempo_estimado: (int)  Tiempo estimado en dias
        fecha_inicio: (datetime.date) Fecha de inicio
        persona_a_cargo: (persona) Persona responsable de la actividad
        """
        self.nombre = nombre
        self.costo = costo
        self.tiempo_estimado = tiempo_estimado
        self.fecha_inicio = fecha_inicio
        self.persona_a_cargo = persona_a_cargo
    
    def __repr__(self):
        texto = '-'*80
        texto += '\n {}'.format(self.nombre)
        texto += '\n Costo ${}'.format(self.costo)
        texto += '\n Inicio: {}'.format(self.fecha_inicio.strftime('%d-%m-%Y'))
        texto += '\n A cargo: {} \n'.format(self.persona_a_cargo)
        texto += '-'*80
        return texto


from lista import Lista
import random
import datetime

personas = Lista()
personas.append(Persona('RAQUEL ELIZABET', 39485626))
personas.append(Persona('MARÍA ROSARIO', 23749384))
personas.append(Persona('ALBERTO OSCAR', 25928472))


fecha = datetime.datetime(2019,10,15)
fechas = Lista()
fechas.append(fecha)
for i in range(1,90*24):
    fecha += datetime.timedelta(hours=1)
    fechas.append(fecha)

nombres_actividades = Lista()
nombres_actividades.append('Entrevista con cliente')
nombres_actividades.append('Reunion de equipo')
nombres_actividades.append('Reunion de equipo')
nombres_actividades.append('Reunion de equipo')
nombres_actividades.append('Reunion de equipo')
nombres_actividades.append('Reunion de equipo')
nombres_actividades.append('Reunion de cliente')
nombres_actividades.append('Reunion de cliente')
nombres_actividades.append('Reunion de cliente')
nombres_actividades.append('Definicion de requerimientos')
nombres_actividades.append('Prototipado')
nombres_actividades.append('Muestra prototipo al cliente')
nombres_actividades.append('Diseño del software')
nombres_actividades.append('Implementacion')
nombres_actividades.append('Testing')
nombres_actividades.append('Despliegue')


proyecto = Lista()
for nombre in nombres_actividades:
    costo = random.randint(0,100000)
    tiempo_estimado = random.randint(1,20)
    fecha_inicio = random.choice(fechas)
    persona_a_cargo = random.choice(personas)
    proyecto.append(Actividad(nombre, costo, tiempo_estimado, fecha_inicio, persona_a_cargo))
