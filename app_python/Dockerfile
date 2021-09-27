FROM python:3-alpine

RUN mkdir -p /app && adduser -D myuser && chown -R myuser:myuser /app && mkdir -p /app/data && chown -R myuser:myuser /app/data
WORKDIR /app

COPY --chown=myuser:myuser requirements.txt .
COPY --chown=myuser:myuser main.py .

USER myuser

RUN python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]