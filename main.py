from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.models import User, UserAge, Feedback, UserCreate
from products_db import sample_products
from typing import Dict, List
app = FastAPI()

user: User = User(name="John Doe", id=1)

@app.get('/')
async def main_page():
        return  FileResponse('view/index.html')

@app.post('/calculate/')
async def calculate(num_1:int, num_2:int):
        return {"result":num_1 + num_2}

@app.get('/user')
def user_info() -> User:
        return user

@app.post('/user')
def user_age(user:UserAge):
        return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}

@app.post('/feedback')
def user_age(feedback:Feedback):
        return {"message": "Feedback received. Thank you, Alice!"}

@app.post('/create_user')
def create_user(item:UserCreate) -> UserCreate:
        return item

@app.get('/product/{product_id}')
def user_info(product_id: int) -> Dict | None:
        for product in sample_products:
                if product['product_id'] == product_id:
                        return product
                continue


@app.get('/products/search')
def user_info(keyword:str, category:str | None = None, limit: int | None = 10) -> List[Dict] | None:
        result = []
        for product in sample_products:
                if keyword in product['name']:
                        if category:
                                if product['category'] == category:
                                        result.append(product)
                                        continue
                        result.append(product)
                        if len(result) == limit:
                                break
        return result