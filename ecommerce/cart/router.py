from os import stat
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ecommerce import db
from ecommerce.user.schema import User
from . import services, schema

router = APIRouter(tags=["cart"], prefix="/cart")


@router.get("/add", status_code=status.HTTP_201_CREATED)
async def add_product(product_id: int, database: Session = Depends(db.get_db)):
    result = await services.add_to_cart(product_id, database)
