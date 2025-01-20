from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from .auth_user import UserUseCases


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


def token_verifier(
    token = Depends(oauth_scheme)
):
    uc = UserUseCases()
    uc.verify_token(access_token=token)
    return True