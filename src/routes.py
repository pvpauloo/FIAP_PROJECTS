from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from .auth_user import UserUseCases
from .depends import token_verifier
from .schemas import User, TokenSchema
from .tools.filtro import filtro
from .tools.download_prepare_files import *
from .tools.load_data import load_data
from typing import Optional, List, Dict, Any
data = load_data()

user_router = APIRouter(prefix='/user')
data_router = APIRouter(prefix='/data', dependencies=[Depends(token_verifier)])

@user_router.post('/register')
def user_register(
    user: User
):
    uc = UserUseCases()
    uc.user_register(user=user)
    return JSONResponse(
        content={'msg': 'success'},
        status_code=status.HTTP_201_CREATED
    )

# rota com finalidade de rotarnar o token ao usuario mediante username e senha
@user_router.post('/login')
def user_register(
    request_form_user: OAuth2PasswordRequestForm = Depends()
):
    uc = UserUseCases()
    user = User(
        username=request_form_user.username,
        password=request_form_user.password
    )

    auth_data = uc.user_login(user=user)
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )

# GET producao
@data_router.get("/prepare_files")
def prepare_files():
    processar_dados(RELATIVE_DATA_PATH)

# GET producao
@data_router.get("/producao")
async def get_producao(query: Optional[str] = Query(None)):
    producao_data = data.copy()['producao']
    for i,_ in enumerate(producao_data):
        producao_data[i]["Ano"] = int(producao_data[i]["Ano"])
    if query:
        try:
            results = filtro(query,producao_data)
            return {"results": len(results), "data": results}
        except:
            pass
    results_count = len(producao_data)
    return {"results": results_count, "data": producao_data}

# GET processamento
@data_router.get("/processamento")
async def get_processamento(query: Optional[str] = Query(None)):
    processamento_data = data.copy()['processamento']
    for i,_ in enumerate(processamento_data):
        processamento_data[i]["Ano"] = int(processamento_data[i]["Ano"])
    if query:
        try:
            results = filtro(query,processamento_data)
            return {"results": len(results), "data": results}
        except:
            pass
    results_count = len(processamento_data)
    return {"results": results_count, "data": processamento_data}

# GET comercializacao
@data_router.get("/comercializacao")
async def get_comercializacao(query: Optional[str] = Query(None)):
    comercializacao_data = data.copy()['comercializacao']
    
    for i,_ in enumerate(comercializacao_data):
        comercializacao_data[i]["Ano"] = int(comercializacao_data[i]["Ano"])
    if query:
        try:
            results = filtro(query,comercializacao_data)
            return {"results": len(results), "data": results}
        except:
            pass
    results_count = len(comercializacao_data)
    return {"results": results_count, "data": comercializacao_data}

# GET importacao
@data_router.get("/importacao")
async def get_importacao(query: Optional[str] = Query(None)):
    importacao_data = data.copy()['importacao']
    for i,_ in enumerate(importacao_data):
        importacao_data[i]["Ano"] = int(float(importacao_data[i]["Ano"]))
    if query:
        try:
            results = filtro(query,importacao_data)
            return {"results": len(results), "data": results}
        except:
            pass
    results_count = len(importacao_data)
    return {"results": results_count, "data": importacao_data}

# GET exportacao
@data_router.get("/exportacao")
async def get_exportacao(query: Optional[str] = Query(None)):
    exportacao_data = data.copy()['exportacao']
    for i,_ in enumerate(exportacao_data):
        exportacao_data[i]["Ano"] = int(float(exportacao_data[i]["Ano"]))
    if query:
        try:
            results = filtro(query,exportacao_data)
            return {"results": len(results), "data": results}
        except:
            pass
    results_count = len(exportacao_data)
    return {"results": results_count, "data": exportacao_data}