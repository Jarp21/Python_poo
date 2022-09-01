# inicio
from mimetypes import init
from unicodedata import name

#Clase persona
class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

#Clase coordenadas
class coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coorenada):
        x_diff = (self.x - otra_coorenada.x)**2
        y_diff = (self.y - otra_coorenada.y)**2
        return(x_diff + y_diff)**0.5

#Clase vehiculo
class automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.combustible = tanque(100)
        self.estado = 'en_reposo'
        self.motor = motor(cilindros = 4)

    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapida':
            self.motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)

        self.estado = 'En movimiento'
class motor:
    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def inyecta_gasolina(self, cantidad):
        tanque.consumo(cantidad)
class tanque:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def consumo(self, consumo):
        self.cantidad = self.cantidad - consumo

'Abstraccion'
#Clase lavadora
class Lavadora:
    def __init__(self) -> None:
        pass

    def lavar(self, temperatura = 'fria'):
        self._llenar_tanque_de_agua(temperatura)
        self._anhadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua{temperatura}')

    def _anhadir_jabon(self):
        print('anhadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugano la ropa')

'Encapsulacion'

'Decoradores'
class decoradores:
    def suma(a, b):
        print(a + b)
    def ini_suma():
        mi_operacion = decoradores.suma
        decoradores.ini_sumados(mi_operacion)
    def ini_sumados(operacion):
        print('Antes de la ejecucion')
        operacion(70, 90)

    #a(b) ->cdecorator
    def decorator(funcion):
        def wrapper(*args, **kwargs):
            print('Antes de la operacion')
            resultado = funcion(*args, **kwargs)
            print('Despues de la operacion')

            return resultado

        return wrapper

    @decorator
    def saludar():
        print('Hola, desde una funcion')

    @decorator
    def suma(a, b):
        return a + b

    def calcular_tiempo(funcion):
        def wrapper(*args, **kwargs):
            pass

        return wrapper

'Getters y Setters'
#cuenta de ahorros
class cuenta():
    def __init__(self, pro, sal, mon) -> None:
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    #getters
    def get_Saldo(self):
        return self.__saldo
    def get_propietario(self):
        return self.__propietario
    def get_moneda(self):   
        return self.__moneda
    #setters
    def set_moneda(self, moneda):
        self.__moneda = moneda
class dentro:
    def acciones():
        cuenta1 = cuenta("oscar", 15000, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_moneda())
        cuenta1.set_moneda("Dolares")
        print(cuenta1.get_moneda())


class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
    @property
    def region(self):
        return self.__region
    @region.setter
    def region(self, region):
        if region in self.__region:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.pais}')

class CasillaDentro:

    pass
    
#Acciones
class Accion:
    def persona():
        #Uso
        david = persona('David', 35)
        erika = persona('Erika', 32)

        #Saludo
        print(david.saluda(erika))

    def coordenada():
        cor1 = coordenada(3, 30)
        cor2 = coordenada(4, 8)
        print(cor1.distancia(cor2))
        cor2 = coordenada(4, 8)

    def lavadora():
        Lavadora().lavar()

    def decoradores_suma():
        decoradores.ini_suma()

    def decoradores():
        print(decoradores.suma(10, 20))
    
    def cuenta():
        dentro.acciones()

if __name__ == '__main__':
    Accion.cuenta()