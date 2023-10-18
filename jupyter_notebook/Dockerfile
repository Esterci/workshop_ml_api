#Sistema Operacional
FROM python:3.10

#Dependências do sistema
RUN apt-get update -y && \
    apt-get install -y python3-pip

#Pacotes do Python
COPY ./requirements.txt requirements.txt 
RUN pip install -r requirements.txt
RUN pip install jupyter

#Diretório do usuário docker
RUN mkdir -p /home/user

#Diretório da api para salvar modelos
RUN mkdir -p /home/user/app

WORKDIR /home/user

EXPOSE 4000

CMD jupyter notebook --ip 0.0.0.0 --port 4000 --allow-root