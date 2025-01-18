from fastapi import FastAPI, Request, HTTPException, Depends, Response,Query
from routes import user_router, data_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from depends import token_verifier
from schemas import User, TokenSchema
from consts import *
import json
import os
import sys
from pathlib import Path

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

app.include_router(user_router)
app.include_router(data_router)

authenticated_users = {}

def get_user(username, password):
    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname, RELATIVE_DATA_PATH)
    with open(os.path.join(data_path, 'Users.json'), 'r', encoding='utf-8') as fp:
        users = json.load(fp)
    user = [x for x in users if x["username"] == username]
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
async def get_token(request: Request, token: str = Query(...)):
    user = token_verifier(token)
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido.")
    return templates.TemplateResponse("generate.html", {"request": request})

@app.post("/validate_user")
async def validate_user(user: User, response: Response):
    validated_user = get_user(user.username, user.password)
    token = f"token_{validated_user['username']}"  # Cria um token simples
    authenticated_users[token] = validated_user  # Salva o usuário autenticado
    response.set_cookie(key="auth_token", value=token,httponly=True)  # Armazena o token no cookie
    return {"message": "Usuário autenticado com sucesso.", "username": validated_user["username"]}




