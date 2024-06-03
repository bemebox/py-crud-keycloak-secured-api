import requests
import logging
from fastapi import HTTPException, status
from configuration import configuration

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_token_validation_response(token: str) -> dict:
    """Fetch the token validation response from Keycloak."""
    client_id = configuration.get_env_var("KEYCLOAK_CLIENT_ID")
    client_secret = configuration.get_env_var("KEYCLOAK_CLIENT_SECRET")
    validate_token_url = configuration.get_env_var("KEYCLOAK_VALIDATE_TOKEN_URL")

    request_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "token": token,
        "grant_type": "token",
    }
    request_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        response = requests.post(
            validate_token_url, headers=request_headers, data=request_data
        )
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching token validation data: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_user_roles(payload: dict) -> list:
    """Extract roles from the token validation response payload."""
    return payload.get("realm_access", {}).get("roles", [])
