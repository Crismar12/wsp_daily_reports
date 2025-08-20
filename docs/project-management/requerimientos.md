**Listado de Requerimientos**

1. **Requisitos de Usuario**
   1.1. Equipo de Operaciones: recibir diariamente un resumen de métricas clave vía grupo de WhatsApp.
   1.2. Equipo de Administración: acceder a un tablero interactivo con métricas y herramientas de análisis.

2. **Requisitos Funcionales**
   2.1. Consumo de la API REST de Justo.
   2.2. Transformación y validación de datos.
   2.3. Generación automática de reportes.
   2.4. Envío de resumen diario por WhatsApp.
   2.5. Presentación de datos en dashboard (Streamlit).

3. **Procesos y Flujos de Trabajo**
   3.1. Orquestación:

   * Ingesta (API) → ETL (transformaciones) → Reporte → Entrega (WhatsApp) → Dashboard.
     3.2. Registro de errores y verificación de integridad en cada etapa.

4. **Requisitos de Rendimiento**
   4.1. Entrega del reporte a WhatsApp ≤ 1 hora tras cierre de turno.
   4.2. Dashboard interactivo con tiempo de respuesta ≤ 5 s por consulta.

5. **Seguridad y Acceso**
   5.1. Autenticación Dashboard: OAuth 2.0 o usuario/contraseña.
   5.2. Verificación de integridad de datos en pipeline.
   5.3. Aislamiento de entornos (dev, qa, prd) y repositorio GitHub privado.

6. **Usabilidad**
   6.1. Visualizaciones claras e intuitivas.
   6.2. Interfaz responsive y accesible.
   6.3. Documentación de usuario y guías rápidas.

7. **Escalabilidad**
   7.1. Soportar incremento de volumen de datos y nuevas fuentes sin degradación.
   7.2. Arquitectura agnóstica a la nube, desplegable on-premise o cloud.

8. **Requisitos Técnicos**
   8.1. Lenguaje: Python 3.
   8.2. Dashboard: Streamlit.
   8.3. Contenerización: Docker.
   8.4. Orquestación de CI/CD en GitHub Actions (o Jenkins).
   8.5. Implementar pruebas unitarias e integración (pre-commit hooks).
   8.6. Arquitectura de pipeline NRT (near-real-time).

9. **Integraciones**
   9.1. API REST de Justo.
   9.2. Servicio de envío a WhatsApp (a definir: Twilio, WhatsApp Business API, etc.).
   9.3. Posible scraping de fuentes externas en fases futuras.

10. **Objetivos de Negocio y Métricas**
    10.1. Métricas en WhatsApp:

    * Cuentas cerradas, anuladas.
    * Platos vendidos (totales y distintos).
    * Pedidos a tiempo/retraso.
    * Horarios (apertura, cierre).
    * Tareas operativas (inventario, mermas, compras, guías).
    * Supervisión (outliers de precios, cuadratura de caja).
    * Planificación (productos con bajo stock o riesgo de malogro).
      10.2. Dashboard adicional: ingresos totales y ganancias estimadas.
      10.3. KPIs de éxito: reducción de errores, quiebres de stock, quejas y aumento de ventas.

11. **Fases Futuras**
    11.1. Consumo de APIs adicionales y scraping.
    11.2. Nuevas métricas y alertas avanzadas.
    11.3. Módulo de predicción de demanda.

12. **Normativas y Cumplimiento**
    12.1. Legislación chilena de protección de datos.
    12.2. Control de acceso y auditoría de operaciones.
    12.3. Documentación completa y cumplimiento de estándares internos.

13. **Procesos Empresariales Afectados**
    13.1. Operaciones diarias de cocina y despacho.
    13.2. Toma de decisiones del equipo de administración.
    13.3. Procedimientos de inventario y control de calidad.

