import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql import get_last_thirty_days

journal_database_path_env = os.getenv("JOURNAL_DATABASE_PATH")

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
)


app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/items")
async def root():
    return {"message": "Hello World"}


@app.get("/last30days")
async def get_last_30_days():
    items = get_last_thirty_days(journal_database_path_env)
    return items
