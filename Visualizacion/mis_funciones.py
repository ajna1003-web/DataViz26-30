# Función 1: Calcular el factorial
def factorial(n):
    """Calcula el factorial de n"""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Función 2: Sumar números impares
def sumar_impares(n):
    """Suma todos los números impares del 0 al n"""
    suma = 0
    for i in range(n):
        if i % 2 != 0:
            suma += i
    return suma

# Función 3: Generar múltiplos
def multiplos(a, n):
    """Genera una lista de múltiplos de a hasta n"""
    return [i * a for i in range(1, n // a + 1)]