FROM python:3.7

WORKDIR /app/

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "websocket_app.asgi:application", "--host 0.0.0.0"]