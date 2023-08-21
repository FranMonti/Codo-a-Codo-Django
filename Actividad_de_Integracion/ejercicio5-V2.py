def get_int_recursivo():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("El valor ingresado no es un entero válido. Intente de nuevo.")
        return get_int_recursivo()

entero = get_int_recursivo()
print(f"Valor entero ingresado: {entero}")
