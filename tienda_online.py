from collections import Counter, OrderedDict

# --- Diccionario con los datos ---
datos_clientes = {
    "compras": [
        "Luis", "Ana", "Luis", "Carlos", "Marta", "Ana",
        "Sofía", "Elena", "Luis", "Carlos"
    ],
    "registrados": [
        "Ana", "Carlos", "Marta", "Elena"
    ]
}

# --- Acceso a las listas ---
compras = datos_clientes["compras"]
registrados = datos_clientes["registrados"]

# 1 Filtrar clientes nuevos no registrados
nuevos_clientes = set(compras) - set(registrados)

# 2 Eliminar duplicados y mantener orden
clientes_unicos = list(OrderedDict.fromkeys(compras))

# 3 Contar cuántas veces se repite cada nombre
conteo_compras = Counter(compras)

# 4 Crear resumen de clientes frecuentes (más de una compra)
resumen_frecuentes = {
    cliente: f"Ha comprado {veces} veces"
    for cliente, veces in conteo_compras.items()
    if veces > 1
}

# --- Formato final de salida ---
print("=== CLIENTES NUEVOS (no registrados) ===")
for cliente in nuevos_clientes:
    print(f"- {cliente}")

print("\n=== LISTA DE CLIENTES ÚNICOS ===")
for cliente in clientes_unicos:
    print(f"- {cliente}")

print("\n=== CLIENTES FRECUENTES (más de 1 compra) ===")
for cliente, mensaje in resumen_frecuentes.items():
    print(f"- {cliente}: {mensaje}")