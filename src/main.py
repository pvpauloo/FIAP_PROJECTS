from fastapi import FastAPI, Request, HTTPException, Depends, Response,Query
from routes import user_router, data_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
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

@app.get("/", include_in_schema=False)
async def root(request: Request):
    return RedirectResponse(url="/docs")





