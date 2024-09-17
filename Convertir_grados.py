import math

#Convertir de grados sexagesimales a radianes y viceversa
def grados_a_radianes(grados):
    return grados * math.pi / 180

def radianes_a_grados(radianes):
    return radianes * 180 / math.pi

print("*** Convertir de grados sexagesimales a radianes y viceversa ***")
grados = float(input("Ingrese Grados: "))
radianes = grados_a_radianes(grados)
print(f"{grados} grados son {radianes:.2f} radianes")

radianes = math.pi
grados = radianes_a_grados(radianes)
print(f"{radianes:.2f} radianes son {grados:.2f} grados")