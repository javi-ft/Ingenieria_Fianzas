# Calificaciones numéricas y literales
def convertir_calificacion_numerica_a_literal(calificacion):
    if calificacion >= 90:
        return 'A'
    elif calificacion >= 80:
        return 'B'
    elif calificacion >= 70:
        return 'C'
    elif calificacion >= 60:
        return 'D'
    else:
        return 'F'

print("*** Calificaciones numéricas y literales ***")
calificacion = float(input("Ingrese Calificación: "))
print(f"Calificación literal: {convertir_calificacion_numerica_a_literal(calificacion)}")