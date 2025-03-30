# Calculadora de Factorial
# Autor: Colin Carreño - Jarith Hernandez
# Licencia: MIT

def calcular_factorial(numero):
    """Calcula el factorial de un número positivo."""
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("Debe ingresar un número entero positivo.")
    return 1 if numero == 0 else numero * calcular_factorial(numero - 1)

def main():
    print("Calculadora de Factorial")
    print("------------------------")
    try:
        num = int(input("Ingrese un número entero positivo: "))
        resultado = calcular_factorial(num)
        print(f"\nEl factorial de {num} es: {resultado}")
    except ValueError as e:
        print(f"\nError: {e}")
    except RecursionError:
        print("\nError: Número demasiado grande para cálculo recursivo")

if __name__ == "__main__":
    main()