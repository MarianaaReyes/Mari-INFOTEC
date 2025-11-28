import re  # Importamos módulo para usar expresiones regulares

# ----------------------------------------------------------
# FUNCIÓN PARA VALIDAR LOS DATOS DEL USUARIO
# ----------------------------------------------------------
def validar_datos(nombre, edad, correo):
    print("\n>>> Iniciando validación de datos...")

    # ----------------------------
    # Validación del nombre
    # ----------------------------

    # Verifica que el nombre no esté vacío
    if not nombre.strip():
        print("Error: El nombre no puede estar vacío.")
        return False
    
    # Verifica que el nombre solo tenga letras y espacios (sin números)
    if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', nombre):
        print("Error: El nombre solo puede contener letras y espacios (no números).")
        return False

    # ----------------------------
    # Validación de la edad
    # ----------------------------

    # Verifica que la edad contenga únicamente números
    if not edad.isdigit():
        print("Error: La edad debe contener solo números.")
        return False

    # Convertir edad a entero y verificar que sea mayor a 0
    edad = int(edad)
    if edad <= 0:
        print("Error: La edad debe ser mayor que cero.")
        return False

    # ----------------------------
    # Validación del correo
    # ----------------------------

    # Verificar que no existan espacios en el correo
    if " " in correo:
        print("Error: El correo no debe contener espacios.")
        return False

    # Validación del formato usando expresión regular
    patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron_correo, correo):
        print("Error: El correo no tiene un formato válido.")
        return False

    # Si todas las validaciones pasan
    print("Datos validados correctamente.")
    print(">>> Finalizando validación...\n")
    return True


# Lista global donde se guardarán los usuarios registrados
lista_usuarios = []


# ----------------------------------------------------------
# FUNCIÓN PARA REGISTRAR USUARIOS
# ----------------------------------------------------------
def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    
    # Solicitar los datos
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    correo = input("Correo: ")

    # Validar los datos ingresados
    if validar_datos(nombre, edad, correo):
        
        # Crear un diccionario con los datos validados
        usuario = {
            "nombre": nombre,
            "edad": int(edad),
            "correo": correo
        }

        # Guardarlo en la lista global
        lista_usuarios.append(usuario)

        # Mostrar resumen de la información registrada
        print("\n Usuario agregado con éxito.")
        print("=== RESUMEN DEL USUARIO REGISTRADO ===")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Correo: {correo}")
        print("======================================\n")


# ----------------------------------------------------------
# FUNCIÓN PARA MOSTRAR TODOS LOS USUARIOS REGISTRADOS
# ----------------------------------------------------------
def mostrar_usuarios():
    print("\n=== USUARIOS REGISTRADOS ===")

    # Si la lista está vacía
    if not lista_usuarios:
        print("No hay usuarios registrados.")
        return
    
    # Recorrer e imprimir los usuarios uno por uno
    for i, user in enumerate(lista_usuarios, start=1):
        print(f"\nUsuario #{i}")
        print(f"Nombre: {user['nombre']}")
        print(f"Edad: {user['edad']}")
        print(f"Correo: {user['correo']}")


# ----------------------------------------------------------
# MENÚ PRINCIPAL DEL PROGRAMA
# ----------------------------------------------------------
def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Registrar un nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        # Evaluar la opción ingresada
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            print("Saliendo del programa...")
            break  # Termina el ciclo y el programa
        else:
            print("Opción no válida, intenta de nuevo.\n")


# Llamada al menú principal para iniciar el programa
menu()