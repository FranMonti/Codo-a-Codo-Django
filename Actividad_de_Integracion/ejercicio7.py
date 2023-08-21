class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo")

    def get_edad(self):
        return self.__edad

    def set_dni(self, dni):
        if len(dni) == 8:
            self.__dni = dni
        else:
            print("El DNI debe tener 8 dígitos")

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

    def es_mayor_de_edad(self):
        return self.__edad >= 18

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:")
        self.__titular.mostrar()
        print(f"Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
            

# SI SE DESEA "PREDETERMINAR" LOS DATOS
"""
persona = Persona("Franco", 19, "45544917")


cuenta = Cuenta(persona, 1000.0)


cuenta.mostrar()


cuenta.ingresar(1000.0)
print("Después de ingresar dinero:")
cuenta.mostrar()


cuenta.retirar(2500.0)
print("Después de retirar dinero:")
cuenta.mostrar()
"""


# SI SE DESEA QUE EL USUARIO INGRESE LOS DATOS POR TECLADO
nombre = input("Ingrese el nombre del titular: ")
edad = int(input("Ingrese la edad del titular: "))
dni = input("Ingrese el DNI del titular: ")
titular = Persona(nombre, edad, dni)


cuenta = Cuenta(titular)


cuenta.mostrar()


cantidad_ingreso = float(input("Ingrese la cantidad a ingresar: "))
cuenta.ingresar(cantidad_ingreso)
print("Después de ingresar dinero:")
cuenta.mostrar()


cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
cuenta.retirar(cantidad_retiro)
print("Después de retirar dinero:")
cuenta.mostrar()