def divisor(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = divisor(num1, num2)
print(f"El máximo común divisor entre {num1} y {num2} es {resultado}")
