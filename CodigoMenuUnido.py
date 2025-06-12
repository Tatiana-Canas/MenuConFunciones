import random   
#funcion que entrega un numero al azar dentro de un rango
def generar_dos_numeros_azar(rango_inicio=1, rango_fin=100):
    numero1 = random.randint(rango_inicio, rango_fin)
    numero2 = random.randint(rango_inicio, rango_fin)
    return numero1, numero2

#funcion que ordena numeros de mayor a menor
listaNumeros = []

def ordenarMayorAMenor(listaNum):
    listaNum = sorted(listaNum)
    return listaNum[::-1]

#Función que calcula promedio de 5 Numeros ingresados por pantalla
def promedio():
    suma = 0
    promedio_total = 0
    for i in range(1,6):
        nota = int(input(f"ingrese la nota del alumno {i} numeros: ""\n"))
        suma = suma + nota
    promedio_total = suma / 5
    print( "el promedio de las notas es: ", promedio_total)
    











while True:
    try:

        print("********---MENU DE FUNCIONES---********")
        print("****1: GENERAR UN NÚMERO AL AZAR")
        print("****2: ORDENAR NUMEROS DE MENOR A MAYOR")
        print("****3: INGRESAR 5 NÚMEROS Y MOSTRAR EL PROMEDIO")
        print("****4: SALIR ")

        while True :
            try:
                opcion=int(input(" INGRESE SU OPCION :  "))
                if 0 < opcion <= 4 :
                    print(" Opcin válida ")
                    break
                else:
                    print(" Ingrese una opción dentro del rango 1 a 3")
            except ValueError:
                print(" Ingrese sólo Numeros enteros entre 1 y 3")

        if opcion==1 :
            # Llamada a la función
            n1, n2 = generar_dos_numeros_azar()
            print("Primer número aleatorio:", n1)
            print("Segundo número aleatorio:", n2)

        elif opcion==2 :
            for i in range(5):
                while True:
                    try:
                        numero = int(input("Ingrese un número: "))
                    except ValueError:
                        print("[! Ingrese un número entero.")
                        continue
                    listaNumeros += [numero] # append
                    break
            print(f"Números de mayor a menor: {ordenarMayorAMenor(listaNumeros)}")


        elif opcion==3 :
            promedio()


        elif opcion==4:
            print("terminar y salir")
            break
    except ValueError:
        print("Debe ingresar sólo numeros enteros dentro del rango")  


           