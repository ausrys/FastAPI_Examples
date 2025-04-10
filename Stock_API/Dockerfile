FROM python:3.11-slim
WORKDIR .
COPY stock.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "dev", "stock.py"]