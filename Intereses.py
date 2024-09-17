#Intereses de una cuenta bancaria
def calcular_interes_compuesto(capital_inicial, tasa_interes, anios):
    monto_final = capital_inicial * (1 + tasa_interes / 100) ** anios
    return monto_final

print("* Intereses de una cuenta bancaria *")
capital_inicial = float(input("capital inicial: "))
tasa_interes = float(input("tasa de interes: "))
anios = float(input("años: "))
print(f"Interés compuesto: {calcular_interes_compuesto(capital_inicial, tasa_interes, anios):.2f} SOLES")
