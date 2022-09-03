#Definir las funciones: Suma, resta, multiplicación y división
#Darle opciones al usuario y que elija valores
#Llamado a las funciones
#Continuar con el programa hasta que el usuario lo cierre

def suma(a,b):
    rta = a+b
    print(str(a)+ " + "+ str(b) + " = " + str(rta) + "\n")

def resta(a,b):
    rta = a-b
    print(str(a)+ " - "+ str(b) + " = " + str(rta)+ "\n")

def mult(a,b):
    rta = a*b
    print(str(a)+ " x "+ str(b) + " = " + str(rta)+ "\n")

def div(a,b):  #Ojo si b es 0
    rta = a/b
    print(str(a)+ " / "+ str(b) + " = " + str(rta)+ "\n")

while True:
    print("Opcion A: Suma")
    print("Opcion B: Resta")
    print("Opcion C: Multiplicación")
    print("Opcion D: División")
    print("Opcion Z: Salir")

    opcion = input("Elegí tu operación: ")

    if opcion =="a" or opcion =="A":
        print("Suma")
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo número: "))
        suma(a,b)
    elif opcion == "b" or opcion == "B":
        print("Resta")
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo número: "))
        resta(a,b)
    elif opcion == "c" or opcion == "C":
        print("Multiplicación")
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo número: "))
        mult(a,b)
    elif opcion == "d" or opcion == "D":
        print("División")
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo número: "))
        div(a,b)
    elif opcion == "z" or opcion == "Z":
        print("¡Nos vemos!")
        quit()