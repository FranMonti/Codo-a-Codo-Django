class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
    
    def set_dni(self, dni):
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18


class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad
    
    def set_titular(self, titular):
        self.titular = titular
    
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}\nCantidad: {self.cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        self.cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No es posible retirar dinero. Titular no válido.")
    
    def mostrar(self):
        print("Cuenta Joven")
        print(f"Titular: {self.titular.get_nombre()}\nCantidad: {self.cantidad}\nBonificación: {self.bonificacion}%")


nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))
dni = input("Ingrese el DNI de la persona: ")


persona1 = Persona(nombre, edad, dni)


cantidad_inicial = float(input("Ingrese la cantidad inicial en la cuenta: "))
bonificacion = int(input("Ingrese el porcentaje de bonificación: "))


cuenta_joven1 = CuentaJoven(persona1, cantidad_inicial, bonificacion)

print("Información de la cuenta:")
cuenta_joven1.mostrar()


cantidad_ingreso = float(input("Ingrese la cantidad a ingresar: "))
cuenta_joven1.ingresar(cantidad_ingreso)


cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
cuenta_joven1.retirar(cantidad_retiro)


print("Información de la cuenta actualizada:")
cuenta_joven1.mostrar()