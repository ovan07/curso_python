from fastapi import FastAPI
from controller import formacion_controller

app = FastAPI()
app.include_router(formacion_controller.router)