

class Empleado:

    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__sueldo = None
        self.__diasLiquidados = 30

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getSueldo(self):
        return self.__sueldo        

    def setNombre(self, nombre : str):
        self.__nombre = nombre

    def setApellido(self, apellido : str):
        self.__apellido = apellido        

    def setSueldo(self, sueldo : str):
        self.__sueldo = sueldo    

    def setDiasLiquidados(self, diasLiquidados : str):
        self.__diasLiquidados = diasLiquidados    

    def salarioDevengado(self):
        return (self.__sueldo/30) * float(self.__diasLiquidados)

    def __str__(self):
        return str('Nombre : ' + self.__nombre +
                '\nApellido: ' +  self.__apellido +
                '\nSueldo: ' +  str(self.__sueldo) +
                '\nDiasLiquidados: ' + str(self.__diasLiquidados) +
                '\nSalario: ' + str(self.salarioDevengado())) 