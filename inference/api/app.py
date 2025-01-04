from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from api.common.validation import (
    validation_exception_handler,
    pydantic_exception_handler,
)
from api.router import router as prediction_router
from prediction_model.model import prediction_model

from config.allowed_origins import ALLOWED_ORIGINS
from database.connection import db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await prediction_model.load_model_async()
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(prediction_router)

app.add_exception_handler(ValidationError, pydantic_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
