class Model:
    def __init__(self) -> None:
        pass


    def load_model(self):
        import pickle

        with open("modelos_treinados/modelo.pkl", "rb") as f:
            self.trained_model = pickle.load(f)


    def predict(self, input_values, load_model=True):
        import numpy as np

        if load_model:
            self.load_model()
        
        # Prevendo

        input_values = np.array(input_values)

        input_values = input_values.reshape(1,-1)

        y_predict_site = self.trained_model.predict(input_values)

        return {
            'valor': int(y_predict_site[0]),
        }, 200
