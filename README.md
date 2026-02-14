# 📊 WhatsApp Daily Operations Reports System

> **Automated restaurant operations reporting system with API integration and WhatsApp notifications**

![Dashboard Preview](https://github.com/user-attachments/assets/14ae74b3-b911-4d6b-b92e-b50a714ea541)

## 🎯 Overview

A production-ready Flask REST API that automates daily operations reporting for restaurant management. The system integrates with Justo's POS API to extract real-time operational data and delivers comprehensive reports via WhatsApp using the Evolution API.

**Key Achievement**: Automated manual reporting processes, reducing report generation time from 30+ minutes to seconds while improving data accuracy and consistency.

## ✨ Features

### 🤖 Automated Reporting
- **Real-time Data Integration**: Connects to Justo's API to fetch sales, inventory, and operational metrics
- **WhatsApp Delivery**: Automated report distribution through Evolution API integration
- **Scheduled Reports**: Daily automated report generation with date-range flexibility
- **Token-based Security**: Secure API access with authentication middleware

### 📈 Comprehensive Metrics

**Sales & Revenue Analytics:**
- Daily accounts opened, closed, and cancelled
- Number of dishes sold and variety metrics
- On-time vs. late order tracking
- Revenue and estimated earnings

**Operational Tracking:**
- Opening and closing hours monitoring
- Inventory management status
- Waste and consumption recording
- Purchase tracking and validation

**Supervision & Planning:**
- Inventory accuracy validation
- Price outlier detection
- Cash register reconciliation
- Low-stock and expiration alerts

## 🏗️ Architecture

```
src/
├── app.py                    # Flask application & API endpoints
├── ingest/
│   └── send_report.py       # API integration & report orchestration
├── whatsapp_reports/
│   └── funciones.py         # Report generation logic
├── transform/               # Data transformation utilities
├── dashboards/             # Dashboard components
└── commons/                # Shared utilities
```

## 🚀 Technology Stack

- **Backend**: Python 3.8, Flask 3.0.3
- **Data Processing**: Pandas, NumPy
- **API Integration**: Requests library for REST API consumption
- **Containerization**: Docker, Docker Compose
- **Environment Management**: python-dotenv
- **Code Quality**: Pre-commit hooks, automated linting

## 📡 API Endpoints

### `POST /daily-operations-report`
Generates and sends daily operations report via WhatsApp

**Query Parameters:**
- `date` (optional): Target date in ISO format (defaults to today)

**Headers:**
- `token`: Authentication token (required)

**Response:**
```json
{
  "status": "ok",
  "mensaje": "Generated report message",
  "shift_id": "shift_identifier",
  "evolution_response": {...}
}
```

### `GET /daily-operations-report`
Returns API information and usage instructions

### `GET /`
Health check endpoint

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Docker & Docker Compose (optional)
- Access to Justo's API
- Evolution API instance

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/Crismar12/wsp_daily_reports.git
cd wsp_daily_reports
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
Create a `.env` file with:
```env
TOKEN_DARKI=your_auth_token
TOKEN=justo_api_token
STORE_ID=your_store_id
SERVER_URL=evolution_api_url
INSTANCE_NAME=evolution_instance
CHAT_ID=whatsapp_group_id
EVOLUTION_API_KEY=evolution_api_key
```

4. **Run the application**
```bash
# Windows
run_app.bat

# Unix/Linux/Mac
python -m src.app
```

### Docker Deployment

```bash
docker-compose up -d
```

The API will be available at `http://localhost:5000`

## 📊 Use Cases

1. **Restaurant Managers**: Receive comprehensive daily operations summaries automatically
2. **Supervisors**: Monitor KPIs and operational compliance in real-time
3. **Inventory Teams**: Track stock levels and receive proactive alerts
4. **Finance Teams**: Access daily revenue and reconciliation data

## 🔒 Security Features

- Token-based authentication for all API endpoints
- Environment variable configuration for sensitive credentials
- Secure API key management for third-party integrations
- Input validation and error handling

## 🧪 Testing

```bash
# Run tests (when implemented)
pytest tests/
```

## 📈 Future Enhancements

- [ ] Interactive dashboard with Plotly/Dash
- [ ] Historical trend analysis
- [ ] Predictive analytics for inventory management
- [ ] Multi-location support
- [ ] Mobile application
- [ ] Custom report templates

## 🤝 Contributing

Contributions are welcome! Please check the [Pull Request Template](PULL_REQUEST_TEMPLATE.md) for guidelines.

## 👨‍💻 Technical Highlights for Recruiters

- **Full-Stack API Development**: RESTful API design with Flask
- **Third-Party Integration**: Experience with multiple external APIs (Justo, Evolution)
- **Data Engineering**: ETL processes with Pandas for business intelligence
- **DevOps**: Docker containerization and deployment
- **Clean Code**: Pre-commit hooks, linting, and code organization
- **Production-Ready**: Error handling, logging, and security best practices
- **Business Impact**: Measurable improvement in operational efficiency

## 📝 License

This project showcases professional development practices for portfolio purposes.

## 📫 Contact

**Crismar** - [GitHub Profile](https://github.com/Crismar12)

---

⭐ **Star this repository if you find it interesting!**
