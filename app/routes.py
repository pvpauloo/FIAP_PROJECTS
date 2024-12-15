from fastapi import APIRouter
from app.auth_user import UserUseCases
from app.schemas import User

user_router = APIRouter(prefix='/user')

@user_router.post('/register')
def user_register():
    pass

# rota com finalidade de rotarnar o token ao usuario mediante username e senha
@user_router.post('/login')
def user_login():
    pass