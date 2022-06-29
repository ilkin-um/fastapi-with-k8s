from decouple import config


class Settings:
    PROJECT_NAME: str = "JobSearch"
    PROJECT_DESCRIPTION: str = "A job platform"
    PROJECT_VERSION: str = "0.1.0"
    DB_NAME: str = config("DB_NAME")
    DB_USER: str = config("DB_USER")
    DB_HOST: str = config("DB_HOST")
    DB_PORT: str = config("DB_PORT")
    DB_PASSWORD: str = config("DB_PASSWORD")
    TEST_DB_NAME: str = config("DB_NAME")
    REDIS_HOST: str = config("DB_NAME")
    REDIS_PORT: str = config("DB_NAME")
    REDIS_DB: str = config("DB_NAME")


settings = Settings()
