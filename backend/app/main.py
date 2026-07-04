from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field,EmailStr,AnyUrl
from typing import Annotated
from fastapi.responses import JSONResponse
import json

from app.api.auth import router as auth_router
app= FastAPI()
app.include_router(auth_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://127.0.0.1:5173","http://localhost:5174"], # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    email: EmailStr
    password: Annotated[str, Field(min_length=6, title='Enter your password', description='The password must be strong with minimum length of 6 characters')]

dummy_users_db = {
    "test@example.com": {
        "user_id": "1",
        "email": "test@example.com",
        "hashed_password": "fake_hashed_securepassword" 
    }
}

def verify_password(plain_password: str, hashed_password:str) -> bool:
    return f'fake_hashed_{plain_password}' == hashed_password

@app.post('/api/verify-user')
async def verify_user(credentials: LoginRequest):

    user= dummy_users_db.get(credentials.email)

    if not  user or not verify_password(credentials.password, user['hashed_password']):
        raise HTTPException(status_code=401, detail='invalid email or password')
    
    return {"message": "User verified", "session_id": f"session_for_{user['user_id']}"}