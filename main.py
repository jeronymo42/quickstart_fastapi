from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
async def main_page():
    with open('index.html') as file:
        result = ''.join(file.readlines())
        return HTMLResponse(content=result, status_code=200)