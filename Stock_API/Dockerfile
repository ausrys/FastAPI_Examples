FROM python:3.13-slim
COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "stock.py", "--host",  "0.0.0.0", "--port",  "8000"]