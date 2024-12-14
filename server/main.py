from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql import get_last_thirty_days

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
    items = get_last_thirty_days()
    print(items)
    return items
