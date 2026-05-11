FROM python:3.13-alpine

WORKDIR /app
COPY src/diagnose.py /app/src/diagnose.py
COPY data /app/data

ENTRYPOINT ["python3", "src/diagnose.py"]
