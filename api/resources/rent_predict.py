from flask_restx import Resource, Namespace, reqparse, fields
from model import Model

prediction_model = Namespace("prediction_model", "Endpiont para cadastrar, pesquisar, editar e deletar métodos prediction_model cadastrados")

modelo = prediction_model.model('prediction_model', {
    'tipo': fields.String(required=True, max_length=20, description='Tipo de imóvel cadastrado'),
    'area': fields.Integer(required=True,description='Área do imóvel cadastrado'),
    'n_quartos': fields.Integer(required=True,description='Número de quartos do imóvel'),
    'n_banheiros': fields.Integer(required=True,description='Número de banheiros do imóvel'),
    'n_vagas': fields.Integer(required=True,description='Número de vagas do imóvel'),
    'condominio': fields.Float(required=True,description='Preço do condomínio'),
    'bairro': fields.String(required=True, max_length=45, description='Nome do bairro do imóvel'),
    })

@prediction_model.route('')
class predictionModel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument(
        "tipo", type=str, required=True
    )
    atributos.add_argument(
        "area", type=int, required=True
    )
    atributos.add_argument(
        "n_quartos", type=int, required=True
    )
    atributos.add_argument(
        "n_banheiros", type=int, required=True
    )
    atributos.add_argument(
        "n_vagas", type=int, required=True
    )
    atributos.add_argument(
        "condominio", type=float, required=True
    )
    atributos.add_argument(
        "bairro", type=str, required=True
    )

    @prediction_model.expect(modelo, validate=True)
    def post(self):
        import pandas as pd

        dados = predictionModel.atributos.parse_args()

        predict_model = Model(
            tipo=dados.tipo,
            )
        
        input_df = pd.DataFrame({
            'm2' : [dados.area],
            'Quartos': [dados.n_quartos],
            'Banheiros' : [dados.n_banheiros],
            'Vagas' : [dados.n_vagas],
            'Condomínio' : [dados.condominio],
            'Bairro' : [dados.bairro],
        })

        try:
            prediction = predict_model.predict(input_df)
            
            return prediction

        except Exception as e:
            return {"Err": str(e)}, 500

