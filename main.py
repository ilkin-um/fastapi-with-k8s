from fastapi import FastAPI
from core.config import settings


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    return app


app = start_application()
