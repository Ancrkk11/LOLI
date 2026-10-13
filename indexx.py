#ejercicio 1
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

#ejercicio 4
class Representante:
    def __init__(self, DNI, edad, Ndehijos, IngresoFamiliar, Propiedad):
        self.__DNI = DNI
        self.__edad = edad
        self.__Ndehijos = Ndehijos
        self.__IngresoFamiliar = IngresoFamiliar
        self.__Propiedad = Propiedad

    def getDNI(self):
        return self.__DNI

    def getEdad(self):
        return self.__edad

    def getNdehijos(self):
        return self.__Ndehijos

    def getIngresoFamiliar(self):
        return self.__IngresoFamiliar

    def getPropiedad(self):
        return self.__Propiedad

    def setDNI(self, DNI):
        if len(DNI) == 8 and DNI.isdigit():
            self.__DNI = DNI
        else:
            print("DNI inválido. Debe tener exactamente 8 dígitos.")

    def setEdad(self, edad):
        if 0 < edad < 120:
            self.__edad = edad
        else:
            print("Edad inválida. Debe estar entre 1 y 119.")

    def setNdehijos(self, Ndehijos):
        if Ndehijos >= 0:
            self.__Ndehijos = Ndehijos
        else:
            print("Número de hijos inválido. Debe ser mayor o igual a 0.")  

    def setIngresoFamiliar(self, IngresoFamiliar):
        if IngresoFamiliar >= 0:
            self.__IngresoFamiliar = IngresoFamiliar
        else:
            print("Ingreso familiar inválido. Debe ser mayor o igual a 0.")

    def setPropiedad(self, Propiedad):
        if Propiedad >= 0:
            self.__Propiedad = Propiedad
        else:
            print("Propiedad inválida. Debe ser mayor o igual a 0.")

    def calificacion(self):
        return self.getEdad() + self.getNdehijos() + self.getIngresoFamiliar() / (self.getPropiedad() + 1)

    def montoMaximo(self):
        cal = self.calificacion()
        if cal <= 150:
            return 35000.00
        elif cal <= 350:
            return 45000.00
        else:
            return 60000.00


r1 = Representante("01234567", 40, 2, 3000, 99)
print(r1.calificacion())  # 72.0
print(r1.montoMaximo())  # 35000.0

r2 = Representante("12345678", 40, 2, 2000, 9)
print(r2.calificacion())  # 242.0
print(r2.montoMaximo())  # 45000.0

r3 = Representante("87654321", 30, 3, 5000, 0)
print(r3.calificacion())  # 5033.0
print(r3.montoMaximo())  # 60000.0
