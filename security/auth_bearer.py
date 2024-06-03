import logging
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from security import keycloak_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False
        payload = keycloak_client.fetch_token_validation_response(jwtoken)
        roles = keycloak_client.get_user_roles(payload)

        if "write_role" in roles:
            isTokenValid = True
        else:
            if payload.get("active", {}) == False:
                logger.warning("Token expired.")
            else:
                logger.warning("User lacks the 'write_role' role.")

        return isTokenValid
