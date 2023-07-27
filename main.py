from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
async def main_page():
        return  FileResponse('view/index.html')