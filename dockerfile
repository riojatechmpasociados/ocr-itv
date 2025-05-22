FROM python:3.11-slim

# Instalar Tesseract y dependencias
RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-spa libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Crear directorio app
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 10000

# Comando para ejecutar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]