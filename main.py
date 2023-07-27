from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.models import User, UserAge
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