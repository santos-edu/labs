FROM python:3.13-alpine

WORKDIR /app
COPY src/app.py /app/src/app.py

ENV HOST=0.0.0.0
ENV PORT=8080

EXPOSE 8080
CMD ["python3", "src/app.py"]
