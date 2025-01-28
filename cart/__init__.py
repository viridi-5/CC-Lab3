import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    items = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        # Assuming contents is a comma-separated string of product IDs
        evaluated_contents = contents.split(',')  # Convert the string to a list of product IDs

        for product_id in evaluated_contents:
            temp_product = products.get_product(int(product_id))  # Convert to int if product ID is numeric
            items.append(temp_product)

    return items


    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


