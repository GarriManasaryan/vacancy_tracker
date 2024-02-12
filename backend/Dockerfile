FROM python:3.10

# контейнер дожтдался доступности постгреса
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /usr/local/bin/wait

RUN chmod +x /usr/local/bin/wait

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "web_app:create_app", "--host", "0.0.0.0", "--port", "5000"]