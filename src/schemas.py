import re
from pydantic import BaseModel, field_validator
from .consts import *

class User(BaseModel):
    username: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    
