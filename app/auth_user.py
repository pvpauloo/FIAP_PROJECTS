from datetime import datetime, timedelta
from fastapi import status
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.schemas import User
from consts import SECRET_KEY, ALGORITHM

crypt_context = CryptContext(schemes=['sha256_crypt'])


class UserUseCases:
    
    # Metodo sem uso por enquanto
    def user_register(self, user: User):
        username = user.username
        password=crypt_context.hash(user.password) # senha em hash

        # to-do: onde e como salvar user/pass.

    def user_login(self, user: User, expires_in: int = 30):
        # to-do: logica determinando se o user e senha estao corretos. Depende da solução adotada em user_register
        
        exp = datetime.now() + timedelta(minutes=expires_in) # definindo tempo de duração do token. Por enquanto sem validação. 

        # payload necessario para criacao do token
        payload = {
            'sub': user.username,
            'exp': exp
        }

        # criacao do token
        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {
            'access_token': access_token,
            'exp': exp.isoformat()
        }
