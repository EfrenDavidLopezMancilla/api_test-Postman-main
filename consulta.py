import psycopg2

# URL de la base de datos
db_url = "postgresql://efren:bjzyeuC0VXwWbO5tOug4sgNP32FGCrZC@dpg-cshd11u8ii6s73bcupag-a.oregon-postgres.render.com/bases_16pk"

# Conectar a la base de datos
try:
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    # Realizar una consulta (ajusta la consulta a tu caso)
    query = "SELECT * FROM estudiantes;"
    cursor.execute(query)

    # Obtener los resultados
    estudiantes = cursor.fetchall()

    # Mostrar los resultados
    print("Datos obtenidos de la base de datos:")
    for estudiante in estudiantes:
        print(estudiante)

except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    # Cerrar la conexión
    if conn:
        cursor.close()
        conn.close()
