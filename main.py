from fastapi import FastAPI
from ecommerce.config import settings
from ecommerce.user import router as user_router


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    return app


app = start_application()
app.include_router(user_router.router)
