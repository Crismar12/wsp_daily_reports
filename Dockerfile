FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt /app/
COPY . /app/

# Instala dependencias del sistema para paquetes que lo necesiten
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto para Flask
EXPOSE 5000

# Comando por defecto
CMD ["python", "-m", "src.app"]

