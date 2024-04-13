"""Application settings."""
import os

from pydantic_settings import BaseSettings

APP_PATH = os.path.abspath(
    os.path.dirname(__file__),
)


class AppSettings(BaseSettings):
    """Application settings class."""

    bot_token: str = ''
    webapp_host: str = 'http://127.0.0.1:5000'


app_settings = AppSettings(
    _env_file=os.path.join(APP_PATH, '.env'),  # type: ignore
)
