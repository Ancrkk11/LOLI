class Cuenta:
    def __init__(self, numCta, saldo):
        self.__numCta = numCta
        self.__saldo = saldo

    def getNumCta(self):
        return self.__numCta
    
    def getSaldo(self):
        return self.__saldo

    def deposito(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Monto de depósito inválido.")

    def retiro(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Monto de retiro inválido o saldo insuficiente.")

class Banco:
    def __init__(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def transferirDinero(self, ctaOrigen, ctaDestino, monto):
        if 0 < monto <= ctaOrigen.getSaldo():
            ctaOrigen.retiro(monto)
            ctaDestino.deposito(monto)
            print(f"Transferencia exitosa. Nuevo saldo de la cuenta origen: {ctaOrigen.getSaldo()}, Nuevo saldo de la cuenta destino: {ctaDestino.getSaldo()}")
        else:
            print("Monto de transferencia inválido o saldo insuficiente en la cuenta origen.")    

cuenta=Cuenta("123456789", 1000)
cuenta2=Cuenta("987654321", 500)
banco=Banco("Banco XYZ")
print(f"Saldo inicial de la cuenta 1: {cuenta.getSaldo()}")
print(f"Saldo inicial de la cuenta 2: {cuenta2.getSaldo()}")
banco.transferirDinero(cuenta, cuenta2, 200)
print(f"Saldo final de la cuenta 1: {cuenta.getSaldo()}")
print(f"Saldo final de la cuenta 2: {cuenta2.getSaldo()}")
banco.transferirDinero(cuenta, cuenta2, 1000)  