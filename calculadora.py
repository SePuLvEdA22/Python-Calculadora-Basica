def suma(n1,n2):
    return n1 + n2

def resta(n1,n2):
    return n1 - n2

def multiplicacion(n1,n2):
    return n1 * n2

def division(n1,n2):
    if n2 != 0:
        return n1 / 2
    
    else:
        print('Error, division por cero')
        

while True:
    print('Calculadora')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Salir')
    
    opcion = input('Ingrese su opcion (1, 2, 3, 4): ')
    
    if opcion == "5":
        print("Saliendo del programa")
        break
    
    if opcion in ("1", "2", "3", "4"):
        try:
            num1 = float(input('Ingrese su primer numero: '))
            num2 = float(input('Ingrese su segundo numero: '))
            
        except ValueError:
            print('Los valores ingresados son incorrectos')
            continue
        
        if opcion == "1":
            print(f"El restultado es: {suma(num1,num2)}")
        elif opcion == "2":
            print(f"El restultado es: {resta(num1,num2)}")
        elif opcion == "3":
            print(f"El restultado es: {multiplicacion(num1,num2)}")
        elif opcion == "4":
            print(f"El restultado es: {division(num1,num2)}")
    
    else:
        print("Opcion no valida")
            
            
            