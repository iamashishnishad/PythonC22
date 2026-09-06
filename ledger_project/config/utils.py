from typing import Any
from datetime import datetime, timedelta, timezone
import jwt
from rest_framework.exceptions import AuthenticationFailed


UTF_8 = "utf-8"
SECRET_KEY = "e0f2dddefac89066f3008b46071cd4c2032005b285b10158e93bd67c6981b054"
ALGORITHM = "HS256"


class JwtUtil:

    @staticmethod
    def create_access_token(user_id: int, role: str) -> str:
        now = datetime.now(timezone.utc)
        payload = {
            "user_id": user_id,
            "role": role,
            "exp": now + timedelta(minutes=30),
            "iat": now,  # creation_time
        }

        return jwt.encode(payload, SECRET_KEY, ALGORITHM)

    @staticmethod
    def verify_token(access_token: str) -> dict[str, Any]:
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired!")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid Token")

        return payload
