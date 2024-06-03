import os
from dotenv import load_dotenv


def configure():
    """helper function  used to load environment variables from a .env file into the application's environment"""
    load_dotenv()


def get_env_var(var_name: str, default: str = None) -> str:
    """helper function to get environment variables with error handling."""
    value = os.getenv(var_name, default)
    if value is None:
        raise EnvironmentError(f"Environment variable {var_name} not set.")
    return value
