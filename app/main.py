from fastapi import FastAPI
from tools.load_data import load_data

  
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
    processamento_data = data.copy()['processamento']
    results_count = len(processamento_data)

    return {"results": results_count, "data": processamento_data}

# GET comercializacao
@app.get("/comercializacao")
async def get_comercializacao():
    comercializacao_data = data.copy()['comercializacao']
    results_count = len(comercializacao_data)

    return {"results": results_count, "data": comercializacao_data}

# GET importacao
@app.get("/importacao")
async def get_importacao():
    importacao_data = data.copy()['importacao']
    results_count = len(importacao_data)

    return {"results": results_count, "data": importacao_data}

# GET exportacao
@app.get("/exportacao")
async def get_exportacao():
    exportacao_data = data.copy()['exportacao']
    results_count = len(exportacao_data)

    return {"results": results_count, "data": exportacao_data}