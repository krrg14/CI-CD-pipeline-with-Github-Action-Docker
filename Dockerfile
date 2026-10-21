FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.12-slim 

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY . .

EXPOSE 5000

CMD [ "python", "app.py"]
