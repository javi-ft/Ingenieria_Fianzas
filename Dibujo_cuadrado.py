import turtle

# Dibujo de un cuadrado
def dibujar_cuadrado(lado):
    pantalla = turtle.Screen()
    lapiz = turtle.Turtle()

    for _ in range(4):
        lapiz.forward(lado)
        lapiz.right(90)

    pantalla.mainloop()

print("*** Dibujo de un cuadrado ***")
lado = float(input("Ingrese el Lado: "))
dibujar_cuadrado(lado)