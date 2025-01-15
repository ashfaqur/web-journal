import os
import asyncio
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql import get_last_thirty_days
from contextlib import asynccontextmanager
from journal_util import (
    get_journal_files,
    validate_journal_db_path_env,
    validate_journal_dir_env,
    update_journal_dir,
)
from journal_parser import parse_journal_files, insert_journal_data

journal_path_dir_env = os.getenv("JOURNAL_PATH")
journal_database_path_env = os.getenv("JOURNAL_DATABASE_PATH")

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
)


async def periodic_task():
    if not validate_journal_dir_env(journal_path_dir_env):
        return
    logging.info(f"Using journal directory {journal_path_dir_env}")
    if not validate_journal_db_path_env(journal_database_path_env):
        return
    logging.info(f"Using journal database {journal_database_path_env}")
    while True:
        update_journal_dir(journal_path_dir_env)
        journal_files = get_journal_files(journal_path_dir_env)
        if journal_files:
            logging.debug(journal_files)
            days = parse_journal_files(journal_files)
            insert_journal_data(days, journal_database_path_env)
        else:
            logging.debug("No journal files found")

        await asyncio.sleep(3600)  # in seconds


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
    items = get_last_thirty_days(journal_database_path_env)
    print(items)
    return items
