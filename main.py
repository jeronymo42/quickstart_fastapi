from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.models import User, UserAge, Feedback, UserCreate
from products_db import sample_products
from typing import Dict, List
from usersdb import testUsers

app = FastAPI()

user: User = User(name="John Doe", id=1)


@app.get('/')
async def main_page():
    return FileResponse('view/index.html')


@app.post('/calculate/')
async def calculate(num_1: int, num_2: int):
    return {"result": num_1 + num_2}


@app.get('/user')
def user_info() -> User:
    return user


@app.post('/user')
def user_age(user: UserAge):
    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}


@app.post('/feedback')
def feedback(feedback: Feedback):
    return {"message": "Feedback received. Thank you, Alice!"}


@app.post('/create_user')
def create_user(item: UserCreate) -> UserCreate:
    return item


@app.get('/product/{product_id}')
def product_info(product_id: int) -> List:
    return list(filter(lambda x: x['product_id'] == product_id,
                sample_products))


@app.get('/products/search')
def product_search(keyword: str, category: str | None = None,
                   limit: int | None = 10) -> List[Dict] | None:
    if not category:
        base_result = list(filter(lambda x: keyword.lower() in
                                  x['name'].lower(), sample_products))
        return list(filter(lambda x: category.lower() ==
                           x['category'].lower(), base_result))[:limit]
    return list(filter(lambda x: keyword.lower() in
                       x['name'].lower(), sample_products))[:limit]


@app.post('/login')
def login_func(name: str, password: str):
    return
