import pandas as pd

# ==========================================================
# 1 CARGA Y VALIDACIÓN DE DATOS
# ==========================================================
def cargar_datos(ruta_estudiantes, ruta_correctas):
    # 1. Cargar los archivos
    df_estudiantes = pd.read_csv("C:\Users\Alan\Documents\Mariana Python\\respuestas_estudiantes.csv")
    df_correctas = pd.read_excel("C:\Users\Alan\Documents\Mariana Python\\respuestas_correctas.xlsx")

    # 2. Obtener las preguntas usando métodos
    preguntas = df_correctas['Pregunta'].values
    
    return df_estudiantes, df_correctas, preguntas


# ==========================================================
# 2 PROCESAMIENTO CENTRAL
# ==========================================================
def calcular_puntuaciones(df_estudiantes, df_correctas, preguntas):
    # 3. Crear diccionario de respuestas correctas
    clave_respuestas = {}
    for i in range(df_correctas.shape[0]):
        pregunta = df_correctas['Pregunta'].iloc[i]
        respuesta = df_correctas['Respuesta'].iloc[i]
        clave_respuestas[pregunta] = respuesta

    # 4. Calcular puntuación para cada estudiante
    df_estudiantes['Puntuación'] = 0
    for p in preguntas:
        respuesta_correcta = clave_respuestas[p]
        df_estudiantes['Puntuación'] += (df_estudiantes[p] == respuesta_correcta).astype(int)
    
    return df_estudiantes, clave_respuestas


# ==========================================================
# 3 GENERACIÓN DE REPORTES
# ==========================================================
def generar_reportes(df_estudiantes, preguntas, clave_respuestas):
    # 5. Mostrar detalle completo de respuestas
    df_detalle = df_estudiantes.copy()
    for p in preguntas:
        df_detalle[p] = df_detalle[p].where(
            df_detalle[p] == clave_respuestas[p],
            df_detalle[p] + 'X'
        )

    # Ordena por puntuación (mayor a menor)
    df_detalle = df_detalle.sort_values('Puntuación', ascending=False)
    print("Leyenda: RespuestaX = Incorrecta")
    print(df_detalle.to_string(index=False))

    # 6. Mostrar resultados resumidos
    print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
    print(df_estudiantes[['Nombre', 'Puntuación']].sort_values('Puntuación', ascending=False).to_string(index=False))

    # Promedio general
    print(f"\nPromedio general: {df_estudiantes['Puntuación'].mean():.2f}")

    # 7. Guardar resultados
    df_estudiantes.to_csv("resultados_examen.csv", index=False)
    print("\nResultados guardados en 'resultados_examen.csv'")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================
if _name_ == "_main_":
    # Bloque 1: Cargar y validar datos
    df_estudiantes, df_correctas, preguntas = cargar_datos(
        "./respuestas_estudiantes.csv",
        "./respuestas_correctas.xlsx"
    )
    
    # Bloque 2: Procesar datos (clave y puntuaciones)
    df_resultados, clave_respuestas = calcular_puntuaciones(df_estudiantes, df_correctas, preguntas)
    
    # Bloque 3: Generar reportes
    generar_reportes(df_resultados, preguntas, clave_respuestas) 