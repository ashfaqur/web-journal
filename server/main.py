import os
import asyncio
from journal_util import get_journal_files, validate_journal_db_path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql import get_last_thirty_days
from contextlib import asynccontextmanager


journal_path_dir = os.getenv("JOURNAL_PATH")
journal_database_path = os.getenv("JOURNAL_DATABASE_PATH")


async def periodic_task():
    while True:
        print("Running periodic task...")
        # Add the code you want to execute every 60 minutes
        if journal_path_dir and validate_journal_db_path(journal_database_path):
            journal_files = get_journal_files(journal_path_dir)
            print(journal_files)

        await asyncio.sleep(10)  # in seconds


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the periodic task
    print("Starting periodic task...")
    task = asyncio.create_task(periodic_task())
    try:
        yield  # Allow the application to run
    finally:
        task.cancel()  # Cancel the periodic task when the application stops
        await task  # Ensure cleanup of the task


app = FastAPI(lifespan=lifespan)

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
