from fastapi import FastAPI
from ecommerce.config import settings
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router
from ecommerce.cart import router as cart_router


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )
    return app


app = start_application()
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
