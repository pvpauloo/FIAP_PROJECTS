from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from auth_user import UserUseCases
from depends import token_verifier
from schemas import User

from tools.download_prepare_files import *
from tools.load_data import load_data

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
async def get_producao():
    producao_data = data.copy()['producao']
    results_count = len(producao_data)
    return {"results": results_count, "data": producao_data}

# GET processamento
@data_router.get("/processamento")
async def get_processamento():
    processamento_data = data.copy()['processamento']
    results_count = len(processamento_data)
    return {"results": results_count, "data": processamento_data}

# GET comercializacao
@data_router.get("/comercializacao")
async def get_comercializacao():
    comercializacao_data = data.copy()['comercializacao']
    results_count = len(comercializacao_data)
    return {"results": results_count, "data": comercializacao_data}

# GET importacao
@data_router.get("/importacao")
async def get_importacao():
    importacao_data = data.copy()['importacao']
    results_count = len(importacao_data)
    return {"results": results_count, "data": importacao_data}

# GET exportacao
@data_router.get("/exportacao")
async def get_exportacao():
    exportacao_data = data.copy()['exportacao']
    results_count = len(exportacao_data)
    return {"results": results_count, "data": exportacao_data}