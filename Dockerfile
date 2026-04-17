FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gdown && \
    gdown "https://drive.google.com/uc?id=16knNIyEL_biTfWMOWiKzWQgJzuAJ1y0L" -O /app/best_resnet50.pth

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]