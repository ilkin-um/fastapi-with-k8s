from fastapi import FastAPI
from celery import Celery
from ecommerce.config import settings
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router
from ecommerce.cart import router as cart_router
from ecommerce.orders import router as order_router
from ecommerce.config import settings

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
app.include_router(order_router.router)


celery = Celery(
    __name__,
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",
    backend=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",

)


celery.conf.imports = [
    'ecommerce.orders.tasks'
]