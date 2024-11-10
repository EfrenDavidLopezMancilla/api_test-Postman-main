import requests

# URL de la API
url = "https://api-test-2-vnx1.onrender.com/estudiantes"

try:
    # Hacer la solicitud GET a la API
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Mostrar el resultado en formato JSON
        data = response.json()
        print("Datos obtenidos de la API:")
        for estudiante in data:
            print(estudiante)
    else:
        print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
    