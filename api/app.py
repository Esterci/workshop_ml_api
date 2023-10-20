from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS
from resources.digit_predict import classification_model

app = Flask(__name__)

api = Api(
    app,
    title="API do workshop de integração com ML",
    version="1.0",
    description="API de classificação de dígitos",
)

cors = CORS(app)

api.add_namespace(classification_model, "/digit-predict")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False)
