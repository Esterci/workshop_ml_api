# Importações das bibliotecas necessárias. Flask-Restx é usado para criar
# a API REST. O Model é importado do módulo model, que deve conter a classe
# de modelo discutida na pergunta anterior.
from flask_restx import Resource, Namespace, reqparse, fields
from model import Model

# Criação de um namespace chamado classification_model com uma breve descrição.
# Isso é usado para organizar os endpoints da API.
classification_model = Namespace(
    "classification_model",
    "Endpiont para classifiicar os dígitos escritos a mão",
)

# Define um modelo de dados chamado modelo para a API. O modelo consiste em um 
# campo chamado "pixel_values", que é uma string que representa os valores de 
# pixels na imagem. É especificado que esse campo é obrigatório, tem um comprimento 
# máximo de 600 caracteres e possui uma descrição.
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

# Cria uma classe chamada predictionModel que herda de Resource. Essa classe representa 
# o endpoint da API para previsão de modelos.
@classification_model.route("")
class predictionModel(Resource):
    # Define um objeto atributos do tipo RequestParser para analisar os argumentos da 
    # solicitação. Ele adiciona um argumento chamado "pixel_values" que é uma string e 
    # é obrigatório.
    atributos = reqparse.RequestParser()
    atributos.add_argument("pixel_values", type=str, required=True)
    
    # Usa um decorador expect para definir que o método POST espera um modelo de dados 
    # conforme definido em modelo. O parâmetro validate=True indica que a validação
    #  deve ser realizada.
    @classification_model.expect(modelo, validate=True)
    def post(self):

        # Analisa os argumentos da solicitação usando o RequestParser definido 
        # anteriormente e armazena-os em dados.
        dados = predictionModel.atributos.parse_args()

        # Cria uma instância da classe Model (presumivelmente, a mesma classe de 
        # modelo discutida na primeira resposta).
        predict_model = Model()

        # Divide a string de valores de pixel em uma lista e converte cada valor em 
        # ponto flutuante.
        input_str = dados.pixel_values.split(",")

        input_dados = [float(str_value) for str_value in input_str]

        # Faz uma chamada ao método predict do modelo para realizar a previsão com 
        # base nos dados de entrada. Se a previsão for bem-sucedida, ela é retornada. 
        # Se ocorrer uma exceção, uma resposta de erro é retornada com o código de
        # status 500.
        try:
            prediction = predict_model.predict(input_dados)

            return prediction

        except Exception as e:
            return {"Err": str(e)}, 500
