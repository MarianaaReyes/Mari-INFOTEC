import time
from functools import reduce

# ==========================================================
# DECORADOR PERSONALIZADO
# ==========================================================
def auditar_funcion(func):
    """
    Decorador que audita la ejecución de una función:
    - Muestra el nombre de la función
    - Cuenta cuántas veces ha sido llamada
    - Calcula la duración de ejecución
    """
    contador = {"llamadas": 0}

    def wrapper(*args, **kwargs):
        contador["llamadas"] += 1
        inicio = time.time()
        print(f"\n Ejecutando función: {func._name_}()")
        print(f" Llamada número: {contador['llamadas']}")
        
        resultado = func(*args, **kwargs)
        
        fin = time.time()
        duracion = fin - inicio
        print(f" Duración de ejecución: {duracion:.4f} segundos")
        return resultado

    return wrapper


# ==========================================================
# GENERADOR DE DATOS
# ==========================================================
def leer_temperaturas():
    """
    Generador que simula la lectura de temperaturas desde sensores.
    Devuelve tuplas con formato ("Ciudad", temperatura)
    """
    datos = [
        ("CDMX", 26),
        ("Monterrey", 34),
        ("Toluca", 19),
        ("Cancún", 38),
        ("Guadalajara", 31),
        ("Puebla", 25),
        ("Hermosillo", 40),
        ("Mérida", 37)
    ]
    for registro in datos:
        yield registro


# ==========================================================
# PROCESAMIENTO DE DATOS
# ==========================================================
@auditar_funcion
def procesar_temperaturas():
    # 1 Obtener los datos del generador
    datos = list(leer_temperaturas())

    # 2 Filtrar temperaturas >= 30°C
    filtradas = list(filter(lambda x: x[1] >= 30, datos))

    # 3 Ordenar por temperatura descendente
    ordenadas = sorted(filtradas, key=lambda x: x[1], reverse=True)

    # 4 Transformar a mensajes de alerta
    alertas = list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", ordenadas))

    # 5 Calcular promedio con reduce()
    if ordenadas:
        promedio = reduce(lambda acc, x: acc + x[1], ordenadas, 0) / len(ordenadas)
    else:
        promedio = 0

    # 6 Mostrar resultados
    print("\n  Lista de alertas ordenadas:")
    for alerta in alertas:
        print(" -", alerta)

    print(f"\n Temperatura promedio de alertas: {promedio:.1f}°C")


# ==========================================================
# EJECUCIÓN PRINCIPAL
# ==========================================================
if __name__ == "_main_":
    procesar_temperaturas()