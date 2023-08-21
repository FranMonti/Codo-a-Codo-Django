def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("El valor ingresado no es un entero válido. Intente de nuevo.")

entero = get_int()
print(f"Valor entero ingresado: {entero}")
