
# diretorio onde estao armazeanados os dados ja tratados
RELATIVE_DATA_PATH = 'db/db_json/'

# config para criacao do token 
SECRET_KEY = '0ea52afffae599466c8751da48f2f41b011b5a23b4ca44561311d827e944406f'
ALGORITHM = 'HS256'

baseURL= "http://vitibrasil.cnpuv.embrapa.br/download/"

#Rotas para os conjuntos de dados
path = {
    "Producao": "Producao.csv",
    "Processamento": ["ProcessaViniferas.csv", "ProcessaAmericanas.csv", "ProcessaMesa.csv", "ProcessaSemclass.csv"],
    "Comercializacao": "Comercio.csv",
    "Importacao": ["ImpVinhos.csv", "ImpEspumantes.csv", "ImpFrescas.csv", "ImpPassas.csv", "ImpSuco.csv"],
    "Exportacao": ["ExpVinho.csv", "ExpEspumantes.csv", "ExpUva.csv", "ExpSuco.csv"]
}