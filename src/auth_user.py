import os
import json

from datetime import datetime, timedelta
from fastapi import status
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from schemas import User
from consts import SECRET_KEY, ALGORITHM, RELATIVE_DATA_PATH

crypt_context = CryptContext(schemes=['sha256_crypt'])

# referencia para o path com os usuarios salvos
dirname = os.path.dirname(__file__)
data_path = os.path.join(dirname, RELATIVE_DATA_PATH)

class UserUseCases:
    
    # Metodo sem uso por enquanto
    def user_register(self, user: User):
        username = user.username
        password=crypt_context.hash(user.password) 
        if user:
            if username!="" and password!="":
                # to-do: onde e como salvar user/pass.
                with open(os.path.join(data_path, 'users_hashed.json'), 'r', encoding='utf-8') as fp:
                    users_db = json.load(fp)
                    if not username in users_db:
                        users_db[username] = {'password': password}
                    else:
                        raise HTTPException(status_code=401, detail="Usuário já cadastrado.",headers={"Error": "Usuário já cadastrado."})
                with open(os.path.join(data_path, 'users_hashed.json'), 'w', encoding='utf-8') as fp:
                    json.dump(users_db, fp)
            else:
                raise HTTPException(status_code=401, detail="Usuário ou senha inválidos.")
        

    def user_login(self, user: User, expires_in: int = 86400):
        # to-do: logica determinando se o user e senha estao corretos. Depende da solução adotada em user_register
        
        # carregando usuarios salvos
        with open(os.path.join(data_path, 'users_hashed.json'), 'r', encoding='utf-8') as fp:
            users_db = json.load(fp)

            if users_db.get(user.username) is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Invalid username or password'
                )

            if not crypt_context.verify(user.password, users_db[user.username]['password']):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Invalid username or password'
                )

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
    
    def renew_token(self,access_token:str, expires_in: int = 86400):
        if self.verify_token(access_token):
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            exp = datetime.now() + timedelta(minutes=expires_in)

            payload = {
                'sub': data['sub'],
                'exp': exp
            }


            access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

            return {
                'access_token': access_token,
                'exp': exp.isoformat()
            }
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid access token'
        )
    
    def verify_token(self, access_token):
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token 1 {} {}'.format(access_token, e)
            )
        
        # carregando usuarios salvos
        with open(os.path.join(data_path, 'users_hashed.json'), 'r', encoding='utf-8') as fp:
            users_db = json.load(fp)
        if users_db.get(data['sub']) is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token 2'
            )
        return True