def multiplo(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // multiplo(a, b)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = multiplo(num1, num2)
print(f"El mínimo común múltiplo entre {num1} y {num2} es {resultado}")
