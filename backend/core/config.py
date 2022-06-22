from decouple import config


class Settings:

    PROJECT_NAME: str = "Ecommerce - FastAPI Version"
    PROJECT_DESCRIPTION: str = "This is private docs"
    PROJECT_VERSION: str = "0.1.0"


settings = Settings()
