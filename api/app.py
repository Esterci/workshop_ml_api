# Esse código é um exemplo de um aplicativo web em Python usando 
# o framework Flask, que oferece uma API de classificação de dígitos. 

from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS
from resources.digit_predict import classification_model

# Cria uma instância do aplicativo Flask.
app = Flask(__name__)

# Cria uma instância da classe Api passando o aplicativo Flask 
# criado anteriormente. Define informações sobre a API, como título, 
# versão e descrição, que são usadas para documentação.
api = Api(
    app,
    title="API do workshop de integração com ML",
    version="1.0",
    description="API de classificação de dígitos",
)

# Configura a política de compartilhamento de recursos (CORS) para 
# o aplicativo Flask. Isso permite que a API seja acessada a partir de
#  diferentes origens, por exemplo, de um navegador web.
cors = CORS(app)

# Adiciona um namespace à API, que é definido pelo objeto classification_model.
#  Isso vincula um conjunto de endpoints da API a esse namespace, que, 
# neste caso, é relacionado à classificação de dígitos.
api.add_namespace(classification_model, '/digit-predict')

#  Inicia o servidor web Flask. Ele escuta na interface "0.0.0.0" 
# (o que significa que está disponível em todas as interfaces), na porta 5000, 
# com depuração ativada. O argumento threaded=False significa que o aplicativo 
# não deve ser executado em um ambiente com múltiplas threads.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False)
