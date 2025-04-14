FROM python:3.11-slim
WORKDIR .
COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "dev", "stock.py", "--host",  "0.0.0.0", "--port",  "8000"]