import math

#Cálculo de la raíz cuadrada
def calcular_raiz_cuadrada(numero):
    return math.sqrt(numero)

print("*** Cálculo de la raíz cuadrada ***")
numero = float(input("Ingrese el Numero:"))
print(f"La raíz cuadrada de {numero} es {calcular_raiz_cuadrada(numero):.2f}")