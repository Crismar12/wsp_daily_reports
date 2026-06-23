import os
import random

import requests

# from backports import zoneinfo  # o import zoneinfo si usás Python 3.9+
from dotenv import load_dotenv
from flask import jsonify, request

from ..whatsapp_reports.funciones import reporte_diario_whatsapp

# from datetime import date, datetime


load_dotenv()


def send_report(date):
    # Validar token del usuario
    user_token = request.headers.get('token')
    token_secreto = os.getenv('TOKEN_DARKI')

    from_date = f'{date}T00:00:00-03:00'
    to_date = f'{date}T23:59:59-03:00'

    if user_token != token_secreto:
        return jsonify({'error': 'Token inválido'}), 401

    # Obtener datos desde Justo
    url = (
        f'https://api.service.getjusto.com/v3/tabs/{os.getenv("STORE_ID")}'
        f'/tabs?fromDate={from_date}&toDate={to_date}'
    )
    headers = {'Authorization': f'Bearer {os.getenv("TOKEN")}'}
    response = requests.get(url, headers=headers)
    tabs = response.json()['data']['items']

    # hoy = date.today()
    # tz_chile = zoneinfo.ZoneInfo('America/Santiago')
    shift_ids = set(
        [pago['shiftId'] for tab in tabs for pago in tab.get('payments', [])]
    )

    if not shift_ids:
        return jsonify({'error': 'No se encontraron shift_id válidos para hoy'}), 404

    shift_id = sorted(shift_ids)[0]  # Usamos el primero encontrado

    # Obtener datos del shift
    url_shift = f'https://api.service.getjusto.com/v3/tabs/{os.getenv("STORE_ID")}/shifts/{shift_id}'
    response_shift = requests.get(url_shift, headers=headers)
    shift_data = response_shift.json().get('data', {})

    # Generar mensaje
    mensaje = reporte_diario_whatsapp(response, shift_data, today=date)

    # Enviar mensaje por Evolution API
    delay = random.randint(3000, 5000)
    url_evo = f'{os.getenv("SERVER_URL")}/message/sendText/{os.getenv("INSTANCE_NAME")}'
    payload = {
        'number': os.getenv('CHAT_ID'),
        'text': mensaje,
        'delay': delay,
        'mentionsEveryOne': True,
    }
    headers_evo = {
        'apikey': os.getenv('EVOLUTION_API_KEY'),
        'Content-Type': 'application/json',
    }
    resp = requests.post(url_evo, json=payload, headers=headers_evo)

    return jsonify(
        {
            'status': 'ok',
            'mensaje': mensaje,
            'shift_id': shift_id,
            'evolution_response': resp.json(),
        }
    )
