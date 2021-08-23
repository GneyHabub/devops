FROM python:3-alpine

RUN mkdir -p /app && adduser -D myuser && chown -R myuser /app
WORKDIR /app

COPY requirements.txt .
COPY main.py .

USER myuser

RUN python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]