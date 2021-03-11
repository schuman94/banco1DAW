from cliente import Cliente
from movimientos import Movimientos
from movimiento import Movimiento

class Cuenta:
    num_cuenta = 0

    def __init__(self, titular, movimientos):
        self.__set_numero()
        self.set_titular(titular)
        self.__set_movimientos(movimientos)
        self.__actualizar_saldo()

    def __set_numero(self):
        Cuenta.num_cuenta += 1
        self.__numero = Cuenta.num_cuenta


    def get_numero(self):
        return self.__numero

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def __set_movimientos(self, movimientos):
        self.__movimientos = movimientos

    def __actualizar_saldo(self):
            self.__saldo = self.__movimientos.calcula_saldo()

    def saldo_actual(self):
        return self.__saldo

    def __str__(self):
        return 'Nº:' + str(self.get_numero()) + ' | ' + 'Titular: ' + str(self.get_titular()) + ' | ' + 'Saldo: ' + str(self.saldo_actual())

#Utilizar funciones de orden superior para unificar retirar y depositar
    def retirar(self, concepto, cantidad):
        m = Movimiento(concepto, -cantidad)
        self.__movimientos.anyadir_movimiento(m)
        self.__actualizar_saldo()

    def depositar(self, concepto, cantidad):
        m = Movimiento(concepto, cantidad)
        self.__movimientos.anyadir_movimiento(m)
        self.__actualizar_saldo()
