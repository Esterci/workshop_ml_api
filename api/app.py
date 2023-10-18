from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS
from resources.rent_predict import prediction_model


app = Flask(__name__)


api = Api(
    app,
    title="API Vitrine Urbana",
    version="1.0",
    description="API de previsão de preços de imóveis",
)

cors = CORS(app)

api.add_namespace(prediction_model, '/price-predict')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False)
