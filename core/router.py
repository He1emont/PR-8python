from fastapi import FastAPI
from fa_learn_app.routers import product


def set_routers(app: FastAPI):
    app.include_router(product.router, prefix="", tags=['products'])
