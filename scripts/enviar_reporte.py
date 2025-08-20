import os

import requests
from dotenv import load_dotenv

# Cargar variables desde .env si existe
load_dotenv()

# Obtener el token desde variable de entorno o pedirlo al usuario
token = os.getenv('TOKEN_DARKI')
if token:
    print('🔐 Token detectado automáticamente desde el entorno.')
else:
    token = print('🔐 No se detectó ningún token. No tienes acceso a la aplicación ')

# Preparar headers
headers = {
    'token': token,
}

# Hacer la solicitud
resp = requests.post(
    # 'http://localhost:5000/daily-operations-report',
    'https://api.intranet.darki.cl/daily-operations-report?date=2025-07-11',
    headers=headers,
)

resp.raise_for_status()  # Lanza un error si la solicitud falla

# Mostrar respuesta
print(resp.json())
