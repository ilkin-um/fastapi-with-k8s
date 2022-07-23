from fastapi import HTTPException, status, Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.products.models import Product
from ecommerce.user.models import User
from .models import Cart, CartItems
from .schema import ShowCart


async def add_to_cart(
    product_id: int, current_user, database: Session = Depends(db.get_db)
):
    product_info = database.query(Product).get(product_id)
    if not product_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !"
        )

    if product_info.quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item Out of Stock !"
        )

    user_info = database.query(User).filter(User.email == current_user.email).first()

    cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    if not cart_info:
        new_cart = Cart(user_id=user_info.id)
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_items(new_cart.id, product_info.id, database)
    else:
        await add_items(cart_info.id, product_info.id, database)
    return {"status": "Item Added to Cart"}


async def add_items(
    cart_id: int, product_id: int, database: Session = Depends(db.get_db)
):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    database.add(cart_items)
    database.commit()
    database.refresh(cart_items)

    product_object = database.query(Product).filter(Product.id == product_id)
    current_quantity = product_object.first().quantity - 1
    product_object.update({"quantity": current_quantity})
    database.commit()
    return {"detail": "Object Updated"}


async def get_all_items(current_user, database) -> ShowCart:
    user_info = database.query(User).filter(User.email == current_user.email).first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    return cart


async def remove_cart_item(cart_item_id: int, current_user, database) -> None:
    user_info = database.query(User).filter(User.email == current_user.email).first()
    cart_id = database.query(Cart).filter(User.id == user_info.id).first()
    database.query(CartItems).filter(
        and_(CartItems.id == cart_item_id, CartItems.cart_id == cart_id.id)
    ).delete()
    database.commit()
    return
