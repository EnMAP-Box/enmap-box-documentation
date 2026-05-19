FROM python:3.9-slim

WORKDIR /docs

RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["make", "html"]
