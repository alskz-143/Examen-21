# Examen práctico - Terminal de Expedición Espacial
# Nombre y apellido: Alessia Chans
# Curso: 2°1°
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
#
# No borrar estos comentarios.


# =========================
# ETAPA 1 - INICIO
# =========================

nombre = input("Ingrese su nombre: ")
a1 = 100
print(f"Combustible disponible: {a1}")
cantidad = 0 
luna = 0
marte = 0
saturno = 0
destino = ["Luna", "Marte", "Saturno"]
costos = ["20 unidades", "35 unidades", "50 unidades"]
print(f"¡Bienvenido(a)! Su combustible disponible es: 100")


# =========================
# ETAPA 2 - NAVEGACIÓN
# =========================

menú = ["Luna", "Marte", "Saturno"]
elegido = input("Seleccione un destino: ")
if elegido == "Luna":
    print("El destino elegido es: Luna")
    print("Combustible necesario: 20 unidades")
elif elegido == "Marte":
    print("El destino elegido es: Marte")
    print("Combustible necesario: 35 unidades")
else:
    print("El destino elegido es: Saturno")
    print("Combustible necesario: 50 unidades")

# Utilizar las listas para obtener destino y costo.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la expedición.


# =========================
# ETAPA 4 - ESTADO Y RESUMEN
# =========================

# Mostrar el estado de la nave.
# Recorrer las listas con un for para mostrar destinos y costos.
