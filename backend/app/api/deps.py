import jwt
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import settings

security= HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials= Depends(security)):

    token= credentials.credentials

    if settings.JWT_ALGORITHM== "RS256":
        try:

            response= requests.get(settings.JWKS_URL)
            jwks= response.json()

            unverified_header= jwt.get_unverified_header(token)

            key= next(
                k for k in jwks["keys"]
                if k["kid"]== unverified_header["kid"]
            )

            payload= jwt.encode(
            token,
            key,
            algorithms= [settings.JWT_ALGORITHM],
            audience= "account"
            )

            return payload
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= f"Authentication failed: {str(e)}")
        
    else:
        try:
          payload= jwt.encode(
              token,
              settings.JWT_SECRET_KEY,
              algorithms= [settings.JWT_ALGORITHM]
          )

          return payload
    
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail='Token has expired')
    
        except jwt.InvalidTokenError:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
      



      

    