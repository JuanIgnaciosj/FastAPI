from fastapi import APIRouter, Query, Path
from models.product import Product

router = APIRouter()

products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 20,
        "stock": 10,
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 40,
        "stock": 20,
    }

]


@router.get('/products')  # RUTA POR DEFECTO
def get_products():
    return products


@router.get('/products/{id}')  # RUTA POR DEFECTO
def get_product(id: int = Path(gt=0)):
    return list(filter(lambda item: item['id'] == id, products))

# productos con un determinado valor o precio
# Parametro query es del tipo products/?stock=10&price=50
# asi es como se utilizan los parametros query


# Si contiene parametros query debe llevar una barra al final.
@router.get('/products/')
def get_products_by_stock_price(stock: int, price: float = Query(gt=0)):
    return list(filter(lambda item: item['stock'] == stock and item['price'] == price, products))

# Se crea un producto


@router.post('/products')
def get_create_product(product: Product):
    product.append(product)
    return product


@router.put('/products/{id}')
def update_product(id: int, product: Product):
    for index, item in enumarate(products):
        if item['id'] == id:
            products[index]['name'] == product.name
            products[index]['price'] == product.price
            products[index]['stock'] == product.stock
    return products


@router.delete('/products/{id}')
def delete_product(id: int):
    for item in products:
        if item['id'] == id:
            products.remove(item)
    return products
