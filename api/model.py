# Este código define uma classe chamada Model que 
# parece estar relacionada a um modelo de aprendizado 
# de máquina (ML).

class Model:
    def __init__(self) -> None:
        pass


    # Este método load_model é usado para carregar um modelo 
    # treinado a partir de um arquivo usando a biblioteca pickle. 
    # Ele abre o arquivo "modelo.pkl" no modo de leitura binária 
    # ("rb") e carrega o modelo treinado para o membro da classe 
    # self.trained_model.
    def load_model(self):
        import pickle

        with open("modelos_treinados/modelo.pkl", "rb") as f:
            self.trained_model = pickle.load(f)

    # O método predict é usado para fazer previsões com o modelo carregado. 
    # Ele aceita input_values, que são os valores de entrada para fazer a 
    # previsão. O parâmetro load_model é um valor booleano que determina se o 
    # modelo deve ser carregado antes de fazer a previsão. Se load_model for 
    # verdadeiro, o método chama self.load_model() para carregar o modelo.
    def predict(self, input_values, load_model=True):
        import numpy as np

        if load_model:
            self.load_model()
        
        # Prevendo

        input_values = np.array(input_values)

        input_values = input_values.reshape(1,-1)

        y_predict_site = self.trained_model.predict(input_values)

        # O resultado da previsão é retornado como um dicionário com uma única 
        # chave 'valor', que contém o valor da previsão convertido para um número 
        # inteiro. Além disso, um código de status HTTP 200 é retornado para indicar 
        # que a operação foi bem-sucedida.

        return {
            'valor': int(y_predict_site[0]),
        }, 200
