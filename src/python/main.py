from fastapi import FastAPI

from src.python.controller import ImageController

app = FastAPI()
app.include_router(ImageController.router)
