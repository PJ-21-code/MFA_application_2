from fastapi import FastAPI, HTTPException, APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import time
import random 
import uuid
import json
from app.core.security import security_access_tokens

router= APIRouter()

redis_data_store= {}
class SessionRequest(BaseModel):
    session_id: str

class VerifyOtpRequest(BaseModel):
    session_id: str
    otp: str

def generate_6_digit_otp() -> str:
    return str(random.randint(100000,999999))

@router.post('/api/send-otp')
async def send_otp(request: SessionRequest):
    session_id= request.session_id
    otp_code= generate_6_digit_otp()
    current_time= time.time()

    redis_data_store[session_id]= {
        'otp': otp_code,
        'session_expire_at': current_time+60,
        'last_sent_at': current_time,
        'resend_count': 0
    }

    print(f"[DEVELOPMENT LOG] OTP for {session_id} is: {otp_code}")

    return {"message": "OTP sent successfully"}

@router.post('/api/resend-otp')
async def resend_otp(request: SessionRequest):
    session_id= request.session_id
    session_data= redis_data_store.get(session_id)

    if not session_data:
        raise HTTPException(status_code=404, detail='session not found or expired')
    
    current_time= time.time()
    
    time_since_last_sent = current_time - session_data["last_sent_at"]

    if time_since_last_sent<10:
        remaining_cooldown= int(10- time_since_last_sent)
        raise HTTPException(status_code= status.HTTP_429_TOO_MANY_REQUESTS, detail=  f'wait for {remaining_cooldown} seconds before resending')
    
    if session_data['resend_count'] >=2:
        raise HTTPException(status_code= status.HTTP_429_TOO_MANY_REQUESTS, detail='Maximum cound to resend otp reached')
    
    new_otp= generate_6_digit_otp()

    redis_data_store[session_id].update({
        'otp': new_otp,
        'session_expire_at': current_time+60,
        'last_sent_at': current_time,
        'resend_count': session_data['resend_count'] +1
    })

    print(f"[DEVELOPMENT LOG] OTP for {session_id} is: {new_otp}")

    return {"message": "OTP resent successfully"}

@router.post('/api/verify-otp')
async def verify_otp(request: VerifyOtpRequest):
    session_ID= request.session_id
    session_data= redis_data_store.get(session_ID)

    if not session_data:
        raise HTTPException(status_code=404, detail= 'session not found or expired')
    
    if time.time() > session_data['session_expire_at']:
        del redis_data_store[session_ID]
        raise HTTPException(status_code=400, detail='OTP has expired')
    
    if session_data['otp'] != request.otp:
        raise HTTPException(status_code= 401, detail='Invalid OTP!')
    
    token= security_access_tokens(subject=session_ID)
    

    del redis_data_store[session_ID]

    auth_code = f"code_{uuid.uuid4().hex}"

    return {
        'access_token': token,
        'token_type': "bearer",
        'message': 'Authorization successful'
    }


