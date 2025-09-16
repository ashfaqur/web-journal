import os
import logging
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sql import (
    query_last_days,
    query_counter,
    query_counter_cumulative,
    query_progress,
    query_tags,
)
from process import (
    process_counter_data,
    process_progress_data,
    process_day_points_data,
    DayPointsResult,
)
from habits import process_habits_data, HabitDataResult, HabitObj

journal_database_path_env: Optional[str] = os.getenv("JOURNAL_DATABASE_PATH")

journal_db = ""

if journal_database_path_env:
    journal_db = journal_database_path_env

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
)


def check_journal_database():
    if journal_database_path_env is None:
        logging.error("JOURNAL_DATABASE_PATH environment variable is not set.")
        raise HTTPException(
            status_code=500,
            detail="JOURNAL_DATABASE_PATH environment variable is not set.",
        )


app = FastAPI()

origins = ["*"]  # Allow all origins
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
    check_journal_database()
    if days < 1 or days > 1000:
        raise HTTPException(
            status_code=400, detail="The 'days' parameter must be between 1 and 1000."
        )
    print(f"Fetching last {days} days data")
    result: list[tuple[str, str, int]] = query_last_days(journal_db, days)
    items: list[DayPointsResult] = process_day_points_data(result)
    return items


@app.get("/count/{days}")
async def get_counters(days: int) -> dict[str, list[dict]]:
    check_journal_database()
    items = query_counter(journal_db, days)
    processed_counter_data = process_counter_data(items)
    return processed_counter_data


@app.get("/counter_total/{counter_name}/{days}")
async def get_counter_total(counter_name: str, days: int) -> list[tuple[str, str, int]]:
    check_journal_database()
    items = query_counter_cumulative(journal_db, counter_name, days)
    return items


@app.get("/progress")
async def get_progress_data() -> dict[str, list[tuple[str, int]]]:
    check_journal_database()
    items: list[tuple[str, str, int]] = query_progress(journal_db)
    processed_progress_data: dict[str, list[tuple[str, int]]] = process_progress_data(
        items
    )
    return processed_progress_data


@app.get("/habits/{days}")
async def get_habits_data(days: int) -> list[HabitObj]:
    check_journal_database()
    result: HabitDataResult = query_tags(journal_db, days)
    return process_habits_data(result, days)
