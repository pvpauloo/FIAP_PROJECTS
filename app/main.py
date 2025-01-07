from fastapi import FastAPI, Request, HTTPException, Depends, Response
from tools.load_data import load_data
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from tools.download_prepare_files import *
from schemas import User
from consts import *
import json
import os
from pathlib import Path

data = load_data()

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "app/static"),
    name="static",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


authenticated_users = {}

def get_user(username, password):
    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname, RELATIVE_DATA_PATH)
    with open(os.path.join(data_path, 'Users.json'), 'r', encoding='utf-8') as fp:
        users = json.load(fp)
    user = [x for x in users if x["username"] == username]
    print(username)
    print(password)
    if user:
        if user[0]["password"] == password:
            return user[0]
    else:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos.")

def authenticate_user(request: Request):
    token = request.cookies.get("auth_token")
    print(f"token: {token}")
    if not token or token not in authenticated_users:
        raise HTTPException(status_code=403, detail="Usuário não autenticado.")
    return authenticated_users[token]

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get_token")
async def get_token(request: Request, user: dict = Depends(authenticate_user)):
    return templates.TemplateResponse("generate.html", {"request": request})

@app.post("/validate_user")
async def validate_user(user: User, response: Response):
    validated_user = get_user(user.username, user.password)
    token = f"token_{validated_user['username']}"  # Cria um token simples
    authenticated_users[token] = validated_user  # Salva o usuário autenticado
    response.set_cookie(key="auth_token", value=token,httponly=True)  # Armazena o token no cookie
    return {"message": "Usuário autenticado com sucesso.", "username": validated_user["username"]}

# GET producao
@app.get("/prepare_files")
def prepare_files():
    processar_dados(RELATIVE_DATA_PATH)

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
