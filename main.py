from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
async def main_page():
        return  FileResponse('view/index.html')

@app.post('/calculate/')
async def calculate(num_1:int, num_2:int):
        return {"result":num_1 + num_2}
