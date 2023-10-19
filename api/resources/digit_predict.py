from flask_restx import Resource, Namespace, reqparse, fields
from model import Model

classification_model = Namespace(
    "classification_model",
    "Endpiont para classifiicar os dígitos escritos a mão",
)

modelo = classification_model.model(
    "classification_model",
    {
        "pixel_values": fields.String(
            required=True,
            max_length=600,
            description="Valores na escala de cinza de cada pixel na imagem",
        )
    },
)


@classification_model.route("")
class predictionModel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument("pixel_values", type=str, required=True)

    @classification_model.expect(modelo, validate=True)
    def post(self):
        dados = predictionModel.atributos.parse_args()

        predict_model = Model()

        input_str = dados.pixel_values.split(",")


        input_dados = [float(str_value) for str_value in input_str]

        try:
            prediction = predict_model.predict(input_dados)

            return prediction

        except Exception as e:
            return {"Err": str(e)}, 500
