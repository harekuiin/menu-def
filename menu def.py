def sumar(a,b):
    sumar = a + b
    print(f"La suma de los argumentos es: {sumar}")
    return(sumar)

def restar(a,b):
    restar = a - b
    print(f"La resta de los argumentos es: {restar}")
    return(restar)

def multiplicar(a,b):
    mult = a * b
    print(f"La multiplicación de los argumentos es: {mult}")
    return(mult)

def dividir(a,b):
    if b == 0:
        print("No se puede dividir por 0")
        return None
    div = a / b
    print(f"La division de los argumentos es: {div}")
    return div

def menu():
    xd = "*" * 15
    op = 0

    while op != 5:
        print(xd)
        print("Calculadora")
        print(xd)
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")
        print("5. salir")
        op = int(input("Seleccione una opción: "))

        if op == 1:
               a = int(input("Ingrese primer numero: "))
               b = int(input("Ingrese segundo numero: "))
               resultado = sumar(a, b)
               print(f"El resultado es: {resultado}")
        elif op == 2:
               a = int(input("Ingrese primer numero: "))
               b = int(input("Ingrese segundo numero: "))
               resultado = restar(a, b)
               print(f"El resultado es: {resultado}")
        elif op == 3:
               a = int(input("Ingrese primer numero: "))
               b = int(input("Ingrese segundo numero: "))
               resultado = multiplicar(a, b)
               print(f"El resultado es: {resultado}")
        elif op == 4:
               a = int(input("Ingrese primer numero: "))
               b = int(input("Ingrese segundo numero: "))
               resultado = dividir(a, b)
               print(f"El resultado es: {resultado}")
        elif op == 5:
             print("salir")
             op = op + 5

menu()


