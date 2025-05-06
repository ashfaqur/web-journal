import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sql import query_last_days

journal_database_path_env = os.getenv("JOURNAL_DATABASE_PATH")

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
)


app = FastAPI()

origins = [
    "*"  # Allow all origins
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def root():
    return {"Health": "OK"}

@app.get("/lastdays/{days}")
async def get_last_days(days: int):
    if days < 1 or days > 1000:
        raise HTTPException(
            status_code=400, 
            detail="The 'days' parameter must be between 1 and 1000."
        )
    print(f"Fetching last {days} days data")
    items = query_last_days(journal_database_path_env, days)
    return items