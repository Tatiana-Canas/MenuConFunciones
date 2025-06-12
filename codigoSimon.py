import random

def generar_dos_numeros_azar(rango_inicio=1, rango_fin=100):
    numero1 = random.randint(rango_inicio, rango_fin)
    numero2 = random.randint(rango_inicio, rango_fin)
    return numero1, numero2

# Llamada a la función
n1, n2 = generar_dos_numeros_azar()
print("Primer número aleatorio:", n1)
print("Segundo número aleatorio:", n2)
