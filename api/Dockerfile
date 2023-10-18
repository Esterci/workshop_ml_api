FROM python:3.10

RUN apt-get update -y && \
    apt-get install -y python3-pip


COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

EXPOSE 5000

CMD ["python", "./app.py"]