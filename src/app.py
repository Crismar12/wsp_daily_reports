import os
from datetime import date

from dotenv import load_dotenv
from flask import Flask, jsonify, request

from .ingest.send_report import send_report

load_dotenv()

app = Flask(__name__)


@app.route('/daily-operations-report', methods=['POST'])
def create_and_send_report():
    token = os.getenv('TOKEN_DARKI')
    user_token = request.headers.get('token')

    input_date = request.args.get('date')

    if not input_date:
        input_date = date.today().isoformat()

    if token == user_token:
        return send_report(input_date)

    else:
        return jsonify(
            {
                'status': 'error',
                'code': 401,
            }
        )


@app.route('/daily-operations-report', methods=['GET'])
def get_report():
    return jsonify(
        {
            'status': 'ok',
            'mensaje': 'Endpoint para enviar reporte diario de operaciones',
            'requerimientos': 'Se necesita usar el método POST',
        }
    )


@app.route('/', methods=['GET'])
def get_main_page():
    return jsonify(
        {
            'status': 'ok',
            'mensaje': 'API de reportes',
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
