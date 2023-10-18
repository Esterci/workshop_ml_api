class Binarizador:
    def __init__(self) -> None:
        self.location_dict = {
        'Previdenciários': '00000000',
        'Marumbi': '00000001',
        'Nova Benfica': '00000010',
        'Parque Jardim Burnier': '00000011',
        'Santa Maria': '00000100',
        'Nossa Senhora das Graças': '00000101',
        'São Geraldo': '00000110',
        'Parque Guarani': '00000111',
        'Santa Candida': '00001000',
        'Parque Independência': '00001001',
        'Jardim do Sol': '00001010',
        'Aracy': '00001011',
        'Centenário': '00001100',
        'Sao Tarcisio': '00001101',
        'São Bernardo': '00001110',
        'Santa Cecília': '00001111',
        'Encosta do Sol': '00010000',
        'Filgueiras': '00010001',
        'Linhares': '00010010',
        'Parque Independencia III': '00010011',
        'Bosque dos Pinheiros': '00010100',
        'Jardim Esperança': '00010101',
        'Residencial Renascença': '00010110',
        'Grajaú': '00010111',
        'Jardim de Alah': '00011000',
        'Bonfim': '00011001',
        'Industrial': '00011010',
        'Santos Anjos': '00011011',
        'Cidade Nova': '00011100',
        'Santo Antônio': '00011101',
        'Carlos Chagas': '00011110',
        'Terras Altas': '00011111',
        'Mundo Novo': '00100000',
        'Monte Castelo': '00100001',
        'Cerâmica': '00100010',
        'Martelos': '00100011',
        'Barbosa Lage': '00100100',
        'Nossa Senhora de Lourdes': '00100101',
        'Eldorado': '00100110',
        'Esplanada': '00100111',
        'Caicaras': '00101000',
        'Bom Jardim': '00101001',
        'Vivendas da Serra': '00101010',
        'Vitorino Braga': '00101011',
        'Cidade do Sol': '00101100',
        'Nossa Senhora Aparecida': '00101101',
        'Nossa Senhora de Fátima': '00101110',
        'Jardim das Laranjeiras': '00101111',
        'Fontesville': '00110000',
        'Vila Furtado de Menezes': '00110001',
        'Nova Califórnia': '00110010',
        'Recanto da Mata': '00110011',
        'Loteamento Morada do Serro': '00110100',
        'Paineiras': '00110101',
        'Jardim Lermitage': '00110110',
        'Borboleta': '00110111',
        'Bairu': '00111000',
        'Jardim dos Alfineiros': '00111001',
        'Santa Efigênia': '00111010',
        'Mansões do Bom Pastor': '00111011',
        'Residência': '00111100',
        'Lourdes': '00111101',
        'Democrata': '00111110',
        'Boa Vista': '00111111',
        'Serra D água': '01000000',
        'Bandeirantes': '01000001',
        'Dom Bosco': '01000010',
        'Progresso': '01000011',
        'Vale do Ipê': '01000100',
        'Jardim Glória': '01000101',
        'Ipiranga': '01000110',
        'Jardim Santa Isabel': '01000111',
        'Tiguera': '01001000',
        'Barao do Retiro': '01001001',
        'Retiro': '01001010',
        'Marilândia': '01001011',
        'Granbery': '01001100',
        'Santa Luzia': '01001101',
        'Santa Catarina': '01001110',
        'Morro da Glória': '01001111',
        'Parque Jardim da Serra': '01010000',
        'São Mateus': '01010001',
        'Barreira do Triunfo': '01010010',
        'Santos Dumont': '01010011',
        'Passos': '01010100',
        'Cascatinha': '01010101',
        'Terras do Comendador': '01010110',
        'Valadares': '01010111',
        'Teixeiras': '01011000',
        'Vivendas do Retiro': '01011001',
        'Aeroporto': '01011010',
        'Santa Teresa': '01011011',
        'Vina Del Mar': '01011100',
        'Santa Helena': '01011101',
        'Alto dos Passos': '01011110',
        'Costa Carvalho': '01011111',
        'Santa Terezinha': '01100000',
        'Spina Ville II': '01100001',
        'Parque Guaruá': '01100010',
        'Humaita': '01100011',
        'Graminha': '01100100',
        'Jóquei Clube': '01100101',
        'Bom Pastor': '01100110',
        'Benfica': '01100111',
        'Caete': '01101000',
        'Grama': '01101001',
        'Vila Ideal': '01101010',
        'Novo Horizonte': '01101011',
        'Manoel Honório': '01101100',
        'Centro': '01101101',
        'Parque das Palmeiras': '01101110',
        'Nova Era': '01101111',
        'Ladeira': '01110000',
        'Fábrica': '01110001',
        'Alto dos Pinheiros': '01110010',
        'Recanto dos Lagos': '01110011',
        'Mariano Procópio': '01110100',
        'Cidade Jardim': '01110101',
        'Poço Rico': '01110110',
        'Quintas das Avenidas': '01110111',
        'Vila Ozanan': '01111000',
        'São Pedro': '01111001',
        'Bosque do Imperador': '01111010',
        'Cruzeiro do Sul': '01111011',
        'Portal da Torre': '01111100',
        'Bom Clima': '01111101',
        'Chales do Imperador': '01111110',
        'Francisco Bernardino': '01111111',
        'Jardim Natal': '10000000',
        'Granjas Betania': '10000001',
        'Milho Branco': '10000010',
        'Torreoes': '10000011',
        'Residencial Alvim': '10000100',
        'Estrela Sul': '10000101',
        'Spina Ville': '10000110',
        'Parque Imperial': '10000111',
        'Parque Guadalajara': '10001000',
        'Jk': '10001001',
        'Alphaville': '10001010',
        'Igrejinha': '10001011',
        'Santa Cruz': '10001100',
        'Salvaterra': '10001101',
        'Distrito Industrial': '10001110',
        'Granjas Santo Antonio': '10001111'
    }

    def transform(self,df):
        for i in range(8):
            df[f'b{7-i}'] = 0
        
        def binarize_row(row):
            bairro = row['Bairro']
            bairro_code = self.location_dict.get(bairro, '1' * 8)
            for i, digit in enumerate(bairro_code):
                df.at[row.name, f'b{7-i}'] = int(digit)

        df.apply(binarize_row, axis=1)
        df = df.drop(columns="Bairro")
        return df


class Model:
    def __init__(self, tipo) -> None:
        self.tipo = tipo


    def load_model(self):
        import pickle

        with open("modelos_treinados/modelo_{}.pkl".format(self.tipo), "rb") as f:
            self.trained_model = pickle.load(f)


    def load_scaler(self):
        import pickle

        with open("scalers_treinados/scaler_{}.pkl".format(self.tipo), "rb") as f:
            self.scaler = pickle.load(f)


    def load_tipos(self):
        import pickle

        with open("tipos_disponiveis/tipos.pkl".format(self.tipo), "rb") as f:
            self.bairros, self.tipos_conhecidos = pickle.load(f)


    def predict(self, input_df, load_model=True):

        if load_model:
            self.load_scaler()
            self.load_model()
        
        self.load_tipos()

        # if self.tipo not in self.tipos_conhecidos or input_df.Bairro not in self.bairros:
        #     return {"message": "Tipo de imóvel ou bairro desconhecido."}, 400

        # Binarizando

        self.binarizador = Binarizador()

        input_df = self.binarizador.transform(input_df)

        # Normalizando

        input_df = self.scaler.transform(input_df)

        # Prevendo

        y_predict_site = self.trained_model.predict(input_df)

        # Definindo os intervalos do resultado baseado no valor do preço (<= 1000 = 0.30, <= 2000 = 0.25, <= 5000 = 0.20, <= 10000 <= 0.15, > 10000 = 0.10)
        if y_predict_site <= 1000:
            predict_error = 0.30
        elif y_predict_site <= 2000:
            predict_error = 0.25
        elif y_predict_site <= 5000:
            predict_error = 0.20
        elif y_predict_site <= 10000:
            predict_error = 0.15
        else:
            predict_error = 0.10

        erro = predict_error*y_predict_site[0]

        return {
            'valor': f"{int(y_predict_site[0])},00",
            'valor_min': f"{int(y_predict_site[0]-erro)},00",
            'valor_max': f"{int(y_predict_site[0]+erro)},00",
        }, 200
