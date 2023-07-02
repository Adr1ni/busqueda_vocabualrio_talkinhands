# Establece la imagen base
FROM python:3.9

WORKDIR    /app
COPY       requirements.txt /app/
RUN        pip install -r requirements.txt

COPY       *.py /app/

CMD        ["./main.py"]
