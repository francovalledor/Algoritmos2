import datetime
import random
from lista import Lista
from nombresdata import nombres
import locale

locale.setlocale(locale.LC_ALL, '')  


class Asiento:
    def __init__(self, numero, primera_clase=False, ocupado=False, pasajero=None):
        self.numero = numero
        self.primera_clase = primera_clase
        self.ocupado = ocupado
        self.pasajero = pasajero


class Pasaje:
    def __init__(self, asiento_nro, pasajero=None):
        self.asiento_nro = asiento_nro
        self.pasajero = pasajero


class Avion:
    def __init__(self, matricula, modelo, capacidad, cant_primera_clase):
        self.matricula = matricula
        self.modelo = modelo
        self.asientos = Lista()
        self.capacidad = capacidad
        self.capacidad_turista = capacidad - cant_primera_clase
        self.capacidad_primera_clase = cant_primera_clase

    def __repr__(self):
        texto = '-'*80
        texto += '\n'
        texto += '{}'.format(self.modelo)
        texto += '\nMatricula {}'.format(self.matricula)
        texto += '\n'
        texto += '-'*80

        return texto

    @staticmethod
    def Embraer190(matricula):
        return Avion(matricula, 'Embraer 190', 96, 8)

    @staticmethod
    def Boeing737_700(matricula):
        return Avion(matricula, 'Boeing 737 700', 128, 8)

    @staticmethod
    def Boeing737_800(matricula):
        return Avion(matricula, 'Boeing 737 800', 170, 8)

    @staticmethod
    def Boeing737_MAX_8(matricula):
        return Avion(matricula, 'Boeing 737 MAX 8', 170, 8)

    @staticmethod
    def Airbus340_300(matricula):
        return Avion(matricula, 'Airbus 340-300', 293, 30)

    @staticmethod
    def Airbus330_200(matricula):
        return Avion(matricula, 'Airbus 330-200', 272, 24)

    @staticmethod
    def Airbus330_200(matricula):
        return Avion(matricula, 'Airbus 330-200', 272, 24)


class Vuelo:
    def __init__(self, empresa, nro_vuelo, avion: Avion, fecha, origen, destino, kms):
        self.empresa = empresa
        self.nro_vuelo = nro_vuelo
        self.avion = avion
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.kms = kms
        self.precio_turista = 350 * kms
        self.precio_primera = 988* kms
        self.turista_vendidos = Lista()
        self.turista_no_vendidos = Lista()
        self.primera_vendidos = Lista()
        self.primera_no_vendidos = Lista()

        for i in range(0, avion.capacidad_primera_clase):
            self.primera_no_vendidos.append(Pasaje(i))

        for i in range(avion.capacidad_primera_clase, avion.capacidad):
            self.turista_no_vendidos.append(Pasaje(i))

    def vender_turista(self, pasajero):
        if len(self.turista_no_vendidos) == 0:
            raise IndexError('No quedan asientos turista disponibles')
        else:
            pasaje = self.turista_no_vendidos.pop()
            pasaje.pasajero = pasajero
        self.turista_vendidos.append(pasaje)
        return pasaje.asiento_nro

    def vender_primera_clase(self, pasajero):
        if len(self.primera_no_vendidos) == 0:
            raise IndexError('No quedan asientos turista disponibles')
        else:
            pasaje = self.primera_no_vendidos.pop()
            pasaje.pasajero = pasajero
        self.primera_vendidos.append(pasaje)

    def cant_disponibles(self):
        libres_turista = len(self.turista_no_vendidos)
        libres_primera = len(self.primera_no_vendidos)
        return {'turista': libres_turista, 'primera': libres_primera}

    def cant_turista_disponibles(self):
        return len(self.turista_no_vendidos)

    def cant_primera_disponibles(self):
        return len(self.primera_no_vendidos)

    def recaudado(self):
        """Muestra el total recaudado por el vuelo"""
        recaudado_turista = self.precio_turista * len(self.turista_vendidos)
        recaudado_primera = self.precio_primera * len(self.primera_vendidos)
        return recaudado_primera + recaudado_turista


    def cancelar(self):
        """Cancelar el vuelo y devolver el dinero a los pasajeros"""

        while True:
            try:
                pasaje = self.turista_vendidos.pop()
            except IndexError:
                break
            print('Devolver {} a {}'.format(
                locale.currency(self.precio_turista, grouping=True), pasaje.pasajero))
            pasaje.pasajero = None
            self.turista_no_vendidos.append(pasaje)

        while True:
            try:
                pasaje = self.primera_vendidos.pop()
            except IndexError:
                break
            print('Devolver {} a {}'.format(
                locale.currency(self.precio_primera, grouping=True), pasaje.pasajero))
            pasaje.pasajero = None
            self.primera_no_vendidos.append(pasaje)


    def __repr__(self):
        recaudado = locale.currency(self.recaudado(), grouping=True)
        texto = '-'*80
        texto += '\n\n'
        texto += 'EMPRESA:   {}'.format(self.empresa)
        texto += '\nORIGEN:    {:25} - DESTINO: {:25}'.format(self.origen, self.destino)
        texto += '\nDISTANCIA: {}kms'.format(self.kms)
        texto += '\nFECHA:     {}'.format(self.fecha.strftime('%d-%m-%Y %H:%M'))
        texto += '\nAVION:     {:20} MATRICULA: {}'.format(self.avion.modelo, self.avion.matricula)
        texto += '\n'
        texto += '-'*80
        texto += '\nRECAUDADO: {}'.format(recaudado)
        texto += '\n'
        texto += '-'*80
        return texto

# Fechas
hoy = datetime.date.today()
fecha = datetime.datetime(hoy.year, hoy.month, hoy.day)
fechas = Lista()
fechas.append(fecha)
for i in range(1, 90*24):
    fecha += datetime.timedelta(hours=1)
    fechas.append(fecha)

# FLOTA AEROLINEAS ARGENTINAS
flota_aerolineas = Lista()
flota_aerolineas.append(Avion.Airbus340_300('LV-FPV'))
flota_aerolineas.append(Avion.Airbus340_300('LV-FPU'))
flota_aerolineas.append(Avion.Airbus330_200('LV-FNI'))
flota_aerolineas.append(Avion.Airbus330_200('LV-FNK'))
flota_aerolineas.append(Avion.Airbus330_200('LV-FNL'))
flota_aerolineas.append(Avion.Airbus330_200('LV-FNJ'))
flota_aerolineas.append(Avion.Airbus330_200('LV-FVH'))
flota_aerolineas.append(Avion.Airbus330_200('LV-FVI'))
flota_aerolineas.append(Avion.Airbus330_200('LV-GHQ'))
flota_aerolineas.append(Avion.Airbus330_200('LV-GKO'))
flota_aerolineas.append(Avion.Airbus330_200('LV-GKP'))
flota_aerolineas.append(Avion.Airbus330_200('LV-GIF'))
flota_aerolineas.append(Avion.Boeing737_700('LV-BYY'))
flota_aerolineas.append(Avion.Boeing737_700('LV-BZA'))
flota_aerolineas.append(Avion.Boeing737_700('LV-BZO'))
flota_aerolineas.append(Avion.Boeing737_700('LV-GOO'))
flota_aerolineas.append(Avion.Boeing737_700('LV-CAD'))
flota_aerolineas.append(Avion.Boeing737_700('LV-CAP'))
flota_aerolineas.append(Avion.Boeing737_700('LV-CBF'))
flota_aerolineas.append(Avion.Boeing737_700('LV-CBT'))
flota_aerolineas.append(Avion.Boeing737_800('LV-CTC'))
flota_aerolineas.append(Avion.Boeing737_800('LV-CTB'))
flota_aerolineas.append(Avion.Boeing737_800('LV-CXS'))
flota_aerolineas.append(Avion.Boeing737_800('LV-CXT'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FQB'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FQC'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FQY'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FRK'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FRQ'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FSK'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FUA'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FUB'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FQZ'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FUC'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FVM'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FVN'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FWS'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FVO'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FXQ'))
flota_aerolineas.append(Avion.Boeing737_800('LV-FYK'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GFQ'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GGK'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GGQ'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GKS'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GKT'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GKU'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GUB'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GUC'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GVA'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GVB'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GVC'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GVD'))
flota_aerolineas.append(Avion.Boeing737_800('LV-GVE'))
flota_aerolineas.append(Avion.Boeing737_800('LV-HKU'))
flota_aerolineas.append(Avion.Boeing737_800('LV-HKV'))
flota_aerolineas.append(Avion.Boeing737_800('LV-HKW'))
flota_aerolineas.append(Avion.Embraer190('LV-CDY'))
flota_aerolineas.append(Avion.Embraer190('LV-CDZ'))
flota_aerolineas.append(Avion.Embraer190('LV-CET'))
flota_aerolineas.append(Avion.Embraer190('LV-CEU'))
flota_aerolineas.append(Avion.Embraer190('LV-CEV'))
flota_aerolineas.append(Avion.Embraer190('LV-CHO'))
flota_aerolineas.append(Avion.Embraer190('LV-CHQ'))
flota_aerolineas.append(Avion.Embraer190('LV-CHR'))
flota_aerolineas.append(Avion.Embraer190('LV-CHS'))
flota_aerolineas.append(Avion.Embraer190('LV-CID'))
flota_aerolineas.append(Avion.Embraer190('LV-CIE'))
flota_aerolineas.append(Avion.Embraer190('LV-CIF'))
flota_aerolineas.append(Avion.Embraer190('LV-CIG'))
flota_aerolineas.append(Avion.Embraer190('LV-CIH'))
flota_aerolineas.append(Avion.Embraer190('LV-CKZ'))
flota_aerolineas.append(Avion.Embraer190('LV-CMA'))
flota_aerolineas.append(Avion.Embraer190('LV-CMB'))
flota_aerolineas.append(Avion.Embraer190('LV-CPI'))
flota_aerolineas.append(Avion.Embraer190('LV-CPJ'))
flota_aerolineas.append(Avion.Embraer190('LV-CPK'))
flota_aerolineas.append(Avion.Embraer190('LV-FPS'))
flota_aerolineas.append(Avion.Embraer190('LV-FPT'))
flota_aerolineas.append(Avion.Embraer190('LV-GAQ'))
flota_aerolineas.append(Avion.Embraer190('LV-GBK'))
flota_aerolineas.append(Avion.Embraer190('LV-GIK'))
flota_aerolineas.append(Avion.Embraer190('LV-GIQ'))


destinos = Lista()
destinos.append('Bahía Blanca, Provincia de Buenos Aires')
destinos.append('Bariloche, Provincia de Río Negro')
destinos.append('Catamarca, Provincia de Catamarca')
destinos.append('Comodoro Rivadavia, Provincia del Chubut')
destinos.append('Córdoba, Provincia de Córdoba (Argentina)')
destinos.append('Corrientes, Provincia de Corrientes')
destinos.append('El Calafate, Provincia de Santa Cruz')
destinos.append('Esquel, Provincia del Chubut')
destinos.append('Formosa, Provincia de Formosa')
destinos.append('Iguazú, Provincia de Misiones')
destinos.append('Jujuy, Provincia de Jujuy')
destinos.append('La Rioja, Provincia de La Rioja (Argentina)')
destinos.append('Mar del Plata, Provincia de Buenos Aires')
destinos.append('Mendoza, Provincia de Mendoza')
destinos.append('Neuquén, Provincia del Neuquén')
destinos.append('Paraná, Provincia de Entre Ríos')
destinos.append('Posadas, Provincia de Misiones')
destinos.append('Resistencia, Provincia del Chaco')
destinos.append('Río Cuarto, Provincia de Cordoba')
destinos.append('Río Gallegos, Provincia de Santa Cruz')
destinos.append('Río Grande, Provincia de Tierra del Fuego')
destinos.append('Rosario, Provincia de Santa Fe')
destinos.append('Salta, Provincia de Salta')
destinos.append('San Juan, Provincia de San Juan')
destinos.append('San Luis, Provincia de San Luis')
destinos.append('San Martín de los Andes, Provincia del Neuquén')
destinos.append('San Rafael, Provincia de Mendoza')
destinos.append('Santa Fe, Provincia de Santa Fe')
destinos.append('Santa Rosa, Provincia de La Pampa')
destinos.append('Santiago del Estero, Provincia de Santiago del Estero')
destinos.append('Termas de Río Hondo, Provincia de Santiago del Estero')
destinos.append('Trelew, Provincia del Chubut')
destinos.append('Tucumán, Provincia de Tucumán')
destinos.append('Ushuaia, Provincia de Tierra del Fuego')
destinos.append('Viedma, Provincia de Río Negro')
destinos.append('Miami')
destinos.append('Nueva York')
destinos.append('Orlando')
destinos.append('Cancún')
destinos.append('Punta Cana')
destinos.append('Santa Cruz de la Sierra')
destinos.append('Río de Janeiro')
destinos.append('Salvador de Bahía')
destinos.append('São Paulo')
destinos.append('Santiago de Chile')
destinos.append('Bogotá')
destinos.append('Asunción')
destinos.append('Lima')
destinos.append('Montevideo')
destinos.append('Punta del Este')
destinos.append('Madrid')
destinos.append('Roma')
destinos.append('Curitiba')
destinos.append('Florianópolis')
destinos.append('Porto Alegre')
destinos.append('Porto Seguro')
destinos.append('Río de Janeiro')
destinos.append('Salvador de Bahía')
destinos.append('São Paulo')
destinos.append('Santiago de Chile')
destinos.append('Asunción')
destinos.append('Montevideo')
destinos.append('Punta del Este')
destinos.append('Atenas')


vuelos = Lista()
empresa = 'Aerolineas Argentinas'
origen = 'Buenos Aires, Argentina'
for i in range(0, 200):
    nro_vuelo = random.randint(0, 10000)
    avion = random.choice(flota_aerolineas)
    fecha = random.choice(fechas)
    destino = random.choice(destinos)
    kms = random.randint(1, 10000)
    vuelo = Vuelo(empresa, nro_vuelo, avion, fecha, origen, destino, kms)
    pasajeros_turista = random.randint(0, vuelo.avion.capacidad_turista)
    pasajeros_primera_clase = random.randint(
        0, vuelo.avion.capacidad_primera_clase)

    for i in range(0, pasajeros_turista):
        pasajero = random.choice(nombres)
        vuelo.vender_turista(pasajero)

    for i in range(0, pasajeros_primera_clase):
        pasajero = random.choice(nombres)
        vuelo.vender_primera_clase(pasajero)

    vuelos.append(vuelo)