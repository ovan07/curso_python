from fastapi import FastAPI
from controller import libros_controller

app = FastAPI()
app.include_router(libros_controller.router)