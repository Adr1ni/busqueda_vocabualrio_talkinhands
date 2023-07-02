# Establece la imagen base
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación y el archivo de requisitos
COPY app/ app/
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Establece el comando de inicio de la aplicación
CMD ["python", "-m", "app.main"]
