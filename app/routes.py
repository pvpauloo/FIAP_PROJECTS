from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from auth_user import UserUseCases
from schemas import User

user_router = APIRouter(prefix='/user')

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
def user_login():
    pass