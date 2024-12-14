import os
import json

from consts import *
from fastapi import FastAPI


def load_data():
    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname, RELATIVE_DATA_PATH)
    # print(data_path)

    data = {}

    # Load Comercializacao.json
    with open(os.path.join(data_path, 'Comercializacao.json'), 'r', encoding='utf-8') as fp:
        comercializacao_data = json.load(fp)
        data['comercializacao'] = comercializacao_data

    # Load Exportacao.json
    with open(os.path.join(data_path, 'Exportacao.json'), 'r', encoding='utf-8') as fp:
        exportacao_data = json.load(fp)
        data['exportacao'] = exportacao_data

    # Load Importacao.json
    with open(os.path.join(data_path, 'Importacao.json'), 'r', encoding='utf-8') as fp:
        importacao_data = json.load(fp)
        data['importacao'] = importacao_data

    # Load Processamento.json
    with open(os.path.join(data_path, 'Processamento.json'), 'r', encoding='utf-8') as fp:
        processamento_data = json.load(fp)
        data['processamento_data'] = processamento_data

    # Load Producao.json
    with open(os.path.join(data_path, 'Producao.json'), 'r', encoding='utf-8') as fp:
        producao_data = json.load(fp)
        data['producao'] = producao_data

    for k, entry in data.items(): 
        print(k, type(entry))
    
    return data
    
data = load_data()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# GET producao
@app.get("/producao")
async def get_producao():
    producao_data = data.copy()['producao']
    results_count = len(producao_data)

    return {"results": results_count, "data": producao_data}

# GET processamento
@app.get("/processamento")
async def get_processamento():
    return {"message": "Endpoint /processamento em andamento"}

# GET comercializacao
@app.get("/comercializacao")
async def get_comercializacao():
    return {"message": "Endpoint /comercializacao em andamento"}

# GET importacao
@app.get("/importacao")
async def get_importacao():
    return {"message": "Endpoint /importacao em andamento"}

# GET exportacao
@app.get("/exportacao")
async def get_exportacao():
    return {"message": "Endpoint /exportacao em andamento"}