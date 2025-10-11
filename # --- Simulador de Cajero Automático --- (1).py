# --- Simulador de Cajero Automático ---

# Inventario de billetes disponibles
billetes = {
    1000: 10,
    500: 10,
    200: 10,
    100: 10,
    50: 10,
    20: 10
}

print("\n--- DISPENSADORA DE BILLETES ---")

while True:
    # Solicitar monto
    entrada = input("\nIngrese el monto a retirar (0 para salir): ")

    # Convertimos el valor a entero
    monto = int(entrada)

    # Si el usuario quiere salir
    if monto == 0:
        print("\nGracias por usar el cajero. ¡Hasta luego!")
        break

    # Validar que el monto sea múltiplo de 10 (ya que no hay billetes menores)
    if monto % 10 != 0:
        print("El monto debe ser múltiplo de 10.")
        continue

    # Guardamos el monto restante
    monto_restante = monto

    # Diccionario para los billetes a entregar
    entregar = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0}

    # Algoritmo para entregar la menor cantidad de billetes posible
    for valor in billetes.keys():
        if monto_restante >= valor:
            max_billetes = monto_restante // valor  # Cantidad de billetes necesarios
            # No se pueden entregar más de los disponibles
            if max_billetes > billetes[valor]:
                max_billetes = billetes[valor]
            entregar[valor] = max_billetes
            monto_restante -= valor * max_billetes

    # Verificar si se pudo entregar el monto completo
    if monto_restante == 0:
        # Restar los billetes entregados del inventario
        for valor in entregar.keys():
            billetes[valor] -= entregar[valor]

        print("\n--- Billetes entregados ---")
        for valor, cantidad in entregar.items():
            if cantidad > 0:
                print(f"${valor}: {cantidad} billete(s)")
        print("-----------------------------")
    else:
        print("\nNo hay suficiente combinación de billetes para entregar ese monto.")

    # Mostrar inventario actualizado
    print("\nInventario actual:")
    for valor, cantidad in billetes.items():
        print(f"${valor}: {cantidad} disponibles")







        # Datos correctos del sistema
usuario_correcto = "admin"
contrasena_correcta = "1234"

# Número máximo de intentos
intentos = 3

# Bucle para controlar los intentos
while intentos > 0:
    print("\nINICIO DE SESIÓN")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Verificar si alguno de los campos está vacío
    if usuario == "" or contrasena == "":
        print("Error de autenticación: usuario o contraseña vacíos.")
    # Verificar si el usuario y contraseña son correctos
    elif usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("Inicio de sesión exitoso. ¡Bienvenido!")
        break
    # Verificar si alguno de los datos no existe
    elif usuario != usuario_correcto or contrasena != contrasena_correcta:
        print("Error: usuario o contraseña incorrectos.")

    # Restar un intento
    intentos -= 1
    print(f"Intentos restantes: {intentos}")

# Si se acaban los intentos
if intentos == 0:
    print("Ha superado el número máximo de intentos. Acceso bloqueado.")