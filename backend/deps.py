from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from auth import decode_token
from database import users_collection
from models import user_model

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)

    if not payload:
         raise HTTPException(status_code=401 , detail="Token invalid or expired")

    user = users_collection.find_one({"email" : payload["sub"]})

    if not user:
        raise HTTPException(status_code=404 , detail="User not found")

    return user_model(user)
