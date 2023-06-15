from fastapi import FastAPI
from app.products import produtsList

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/products/")
async def get_products():
    return {
        "products": produtsList
           }


@app.get("/products/{word}")
async def get_products_bay_word(word: str):
    return {
         # filtra produtsList y retorna los que contengan la palabra word en alguna parte del titulo  o la descripcion
        "products": [product for product in produtsList if word in product["title"] or word in product["description"]]

        
    }


