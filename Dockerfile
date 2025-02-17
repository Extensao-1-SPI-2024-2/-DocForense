FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
