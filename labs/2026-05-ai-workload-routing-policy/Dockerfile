FROM python:3.13-alpine

WORKDIR /app
COPY src/router.py /app/src/router.py
COPY data /app/data

ENTRYPOINT ["python3", "src/router.py"]
