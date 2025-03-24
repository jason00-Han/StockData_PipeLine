FROM python:3.9-slim

WORKDIR /ReadFromSource

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "ReadWebSocket:app", "--host", "0.0.0.0", "--port", "8000"]