import os
from psycopg2 import connect

# Obtener los valores de las variables de entorno
db_url = os.getenv('DATABASE_URL')

try:
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    query = "SELECT * FROM estudiantes;"
    cursor.execute(query)

    estudiantes = cursor.fetchall()

    print("Datos obtenidos de la base de datos:")
    for estudiante in estudiantes:
        print(estudiante)

except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    if conn:
        cursor.close()
        conn.close()
