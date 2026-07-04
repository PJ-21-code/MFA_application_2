import jwt
from app.core.config import settings
from datetime import datetime, timedelta, timezone

def security_access_tokens(subject: str) -> str:

    expiration= datetime.now(timezone.utc) + timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload= {
        "sub": subject,
        "exp": expiration
    }

    token= jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm= settings.JWT_ALGORITHM)

    return token