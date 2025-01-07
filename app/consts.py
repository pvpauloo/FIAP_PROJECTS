
# diretorio onde estao armazeanados os dados ja tratados
RELATIVE_DATA_PATH = 'db/db_json/'

# config para criacao do token 
SECRET_KEY = '9a4a5717996f3284fbd1d627a5eb2c6a7e4240b938a3559bbf99ff0a9027409c'
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