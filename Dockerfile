FROM dhi.io/python:3.11-debian13-dev AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN python3 -m pip install --target=/install -r requirements.txt

FROM dhi.io/python:3.11-debian13

WORKDIR /app

COPY --from=builder /install /usr/lib/python3.11/site-packages

COPY app/ .

EXPOSE 8080

CMD ["python3", "app.py"]