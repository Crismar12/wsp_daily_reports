from datetime import datetime

try:
    import zoneinfo  # Python 3.9+
except ImportError:
    from backports import zoneinfo  # Python 3.8 o menor


def reporte_diario_whatsapp(response, shift_data, today=None):
    # if today is None:
    #     today = date.today().isoformat()
    tabs = response.json()['data']['items']

    # Definir zona horaria de Santiago de Chile
    tz_santiago = zoneinfo.ZoneInfo('America/Santiago')

    # Pedidos completados (pagados) - usando zona horaria de Chile
    pedidos_completados = [
        tab
        for tab in tabs
        if tab.get('closedAt')
        # and datetime.fromisoformat(tab['closedAt']).astimezone(tz_santiago).date()
        # == today
        and tab.get('paymentStatus') == 'paid'
    ]

    # Pedidos anulados - usando zona horaria de Chile
    pedidos_anulados = [
        tab
        for tab in tabs
        if tab.get('cancelledAt')
        # and datetime.fromisoformat(tab['cancelledAt']).astimezone(tz_santiago).date()
        # == today
    ]

    # Pedidos entregados a tiempo y con retraso (ajustando zona horaria)
    entregados_a_tiempo = []
    entregados_con_retraso = []
    for tab in pedidos_completados:
        must_be_ready_at = tab.get('mustBeReadyAt')
        closed_at = tab.get('closedAt')
        ready_to_pickup_at = tab.get('readyToPickupAt')
        if must_be_ready_at:
            must_be_ready_at_dt = datetime.fromisoformat(must_be_ready_at).astimezone(
                tz_santiago
            )
            if ready_to_pickup_at:
                delivered_dt = datetime.fromisoformat(ready_to_pickup_at).astimezone(
                    tz_santiago
                )
            elif closed_at:
                delivered_dt = datetime.fromisoformat(closed_at).astimezone(tz_santiago)
            else:
                continue
            if delivered_dt <= must_be_ready_at_dt:
                entregados_a_tiempo.append(tab)
            else:
                entregados_con_retraso.append(tab)

    total_entregados = len(entregados_a_tiempo) + len(entregados_con_retraso)
    pct_tiempo = (
        (len(entregados_a_tiempo) / total_entregados * 100) if total_entregados else 0
    )
    pct_retraso = (
        (len(entregados_con_retraso) / total_entregados * 100)
        if total_entregados
        else 0
    )

    # Platos preparados (nombre, cantidad, precio)
    from collections import defaultdict

    productos_info = defaultdict(lambda: {'cantidad': 0, 'precio': 0})
    total_productos_recaudado = 0
    total_platos_preparados = 0
    for tab in pedidos_completados:
        for item in tab.get('items', []):
            nombre = item['productName']
            precio = item.get('price', 0)
            productos_info[nombre]['cantidad'] += 1
            productos_info[nombre]['precio'] = precio
            total_productos_recaudado += precio
            total_platos_preparados += 1

    preparaciones_distintas = len(productos_info)

    # Horarios de apertura y cierre del turno
    if shift_data:
        apertura = shift_data.get('startedAt')
        cierre = shift_data.get('endedAt')
    else:
        apertura = None
        cierre = None

    # Convertir a datetime y ajustar zona horaria solo si hay valor
    if apertura:
        apertura_dt = datetime.fromisoformat(apertura).astimezone(tz_santiago)
        # apertura_fmt = apertura_dt.strftime('%d/%m/%Y %H:%M')
        apertura_fmt = apertura_dt.strftime('%H:%M')
    else:
        apertura_fmt = 'N/A'

    if cierre:
        cierre_dt = datetime.fromisoformat(cierre).astimezone(tz_santiago)
        # cierre_fmt = cierre_dt.strftime('%d/%m/%Y %H:%M')
        cierre_fmt = cierre_dt.strftime('%H:%M')
    else:
        cierre_fmt = 'Turno aún abierto'

    def format_word(word, count):
        return f"{word}{'s' if count != 1 else ''}"

    count_completed = len(pedidos_completados)
    count_anulados = len(pedidos_anulados)
    count_entregados_a_tiempo = len(entregados_a_tiempo)
    count_entregados_con_retraso = len(entregados_con_retraso)

    # Formato WhatsApp
    reporte = (
        '[DARKI BOT]'
        f'\n*REPORTE DIARIO - {today}*'
        '\n\n*Pedidos:*'
        f'\n- *{count_completed}* {format_word("pedido", count_completed)} '
        # f'completado{'s' if count_completed!=1 else ''}'
        f'{format_word("completado", count_completed)}'
        f'\n- *{count_anulados}* {format_word("pedido", count_anulados)} '
        # f'anulado{'s' if count_anulados!=1 else ''}'
        f'{format_word("anulado", count_anulados)}'
        f'\n- *{count_entregados_a_tiempo}* {format_word("pedido", count_entregados_a_tiempo)} '
        f'a tiempo (*{pct_tiempo:.0f}%*)'
        f'\n- *{count_entregados_con_retraso}* {format_word("pedido", count_entregados_con_retraso)} '
        # f'retrasado{'s' if count_entregados_con_retraso!=1 else ''} (*{pct_retraso:.0f}*%)'
        f'{format_word("retrasado", count_entregados_con_retraso)} (*{pct_retraso:.0f}%*)'
        '\n\n*Platos / Productos:*'
        f'\n- *{total_platos_preparados}* {format_word("plato", total_platos_preparados)} '
        # f'preparado{'s' if total_platos_preparados!=1 else ''}'
        f'{format_word("preparado", total_platos_preparados)}'
        f'\n- *{preparaciones_distintas}* preparación{"es" if preparaciones_distintas!=1 else ""} '
        # f'distinta{'s' if preparaciones_distintas!=1 else ''}'
        f'{format_word("distinta", preparaciones_distintas)}'
        '\n\n*Horarios:*'
        f'\n- apertura sistema: *{apertura_fmt}*'
        f'\n- cierre sistema: *{cierre_fmt}*'
    )

    return reporte
