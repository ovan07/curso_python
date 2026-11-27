from fastapi import FastAPI
from controller import ejemplares_controller

app = FastAPI()
app.include_router(ejemplares_controller.router)