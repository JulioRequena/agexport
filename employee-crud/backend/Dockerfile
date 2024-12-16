# Dockerfile para Flask
FROM python:3.9

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el código de la aplicación
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
