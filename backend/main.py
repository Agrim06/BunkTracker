from fastapi import FastAPI, HTTPException , Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime
from database import users_collection
from schemas import UserRegister, UserLogin, TokenResponse, UserResponse
from auth import hash_password, verify_password, create_access_token, decode_token
from models import user_model

app = FastAPI(title="BunkTracker API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)

    if not payload:
         raise HTTPException(status_code=401 , detail="Token invalid or expired")

    user = users_collection.find_one({"email" : payload["sub"]})

    if not user:
        raise HTTPException(status_code=404 , detail="User not found")

    return user_model(user)


@app.post("/register")
def register(user : UserRegister):
    if users_collection.find_one({"email" : user.email}):
        raise HTTPException(status_code=401 , detail="Email already registered!")

    new_user = {
        "name" : user.name,
        "email" : user.email,
        "password" : hash_password(user.password),
        "min_attendance" : user.min_attendance,
        "created_at" : datetime.utcnow()
    }

    users_collection.insert_one(new_user)
    return { "message" : "User Registered Successfully"}    


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = users_collection.find_one({"email": form_data.username})

    if not db_user or not verify_password(form_data.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user["email"]})
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/me", response_model=UserResponse)
def get_profile(current_user: dict = Depends(get_current_user)):
    return current_user