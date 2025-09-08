import sqlite3
from datetime import datetime, timedelta
from sqlite3 import Connection


def connect_to_db(file_path) -> Connection:
    conn = sqlite3.connect(file_path)
    print(f"Database created at {file_path}")
    return conn


def close_connection(conn: Connection):
    if conn:
        conn.close()
        print("Database connection closed.")


def create_table(conn: Connection):
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS journal (
        date TEXT PRIMARY KEY,
        state TEXT,
        points INTEGER
    )
    """
    )
    conn.commit()
    cursor.close()


def query_progress(journal_db_path: str) -> list[tuple[str, str, int, int]]:
    """Fetch progress data."""
    try:
        conn = connect_to_db(journal_db_path)
        create_table(conn)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT name, date, progress, daily
            FROM progress
            ORDER BY date ASC
            """,
        )
        items: list[tuple[str, str, int, int]] = cursor.fetchall()

        cursor.close()
        close_connection(conn)
        return items
    except Exception as e:
        print(f"SQL Query Failure: {e}")
    return []


def query_counter(journal_db_path: str, days: int) -> list[tuple[str, str, int]]:
    """Fetch counter data over the last given days."""
    try:
        conn = connect_to_db(journal_db_path)
        create_table(conn)
        cursor = conn.cursor()
        # get todays date in format YYYY-MM-DD
        date = datetime.now().strftime("%Y-%m-%d")
        # get the date "days" ago
        days_ago = datetime.now() - timedelta(days=days)
        days_ago_str = days_ago.strftime("%Y-%m-%d")

        # make query between todays date and days ago
        cursor.execute(
            """
            SELECT date, name, count
            FROM counter
            WHERE date <= ? AND date >= ?
            ORDER BY date DESC
            LIMIT ?
            """,
            (
                date,
                days_ago_str,
                days,
            ),
        )
        rows: list[tuple[str, str, int]] = cursor.fetchall()
        cursor.close()
        close_connection(conn)
        # Reverse the list to get the oldest first
        rows = rows[::-1]
        return rows
    except Exception as e:
        print(f"SQL Query Failure: {e}")
    return []


def query_counter_cumulative(
    journal_db_path: str, counter_name: str, days: int
) -> list[tuple[str, str, int]]:
    """Fetch cumulative counter data for a specific counter name over the last given days."""
    try:
        conn = connect_to_db(journal_db_path)
        create_table(conn)
        cursor = conn.cursor()
        # get todays date in format YYYY-MM-DD
        date = datetime.now().strftime("%Y-%m-%d")
        # get the date "days" ago
        days_ago = datetime.now() - timedelta(days=days)
        days_ago_str = days_ago.strftime("%Y-%m-%d")

        # make query between todays date and days ago
        cursor.execute(
            """
            SELECT date, name, cumulative
            FROM counter
            WHERE date <= ? AND date >= ? AND name = ?
            ORDER BY date DESC
            LIMIT ?
            """,
            (
                date,
                days_ago_str,
                counter_name,
                days,
            ),
        )
        rows: list[tuple[str, str, int]] = cursor.fetchall()
        cursor.close()
        close_connection(conn)
        # Reverse the list to get the oldest first
        rows = rows[::-1]
        return rows
    except Exception as e:
        print(f"SQL Query Failure: {e}")
    return []


def query_last_days(journal_db_path: str, days: int) -> list[dict]:
    try:
        conn = connect_to_db(journal_db_path)
        create_table(conn)
        cursor = conn.cursor()
        # get todays date in format YYYY-MM-DD
        date = datetime.now().strftime("%Y-%m-%d")
        # make query for last x days given todays date
        cursor.execute(
            """
            SELECT date, state, points
            FROM journal
            WHERE date <= ?
            ORDER BY date DESC
            LIMIT ?
            """,
            (
                date,
                days,
            ),
        )
        rows: list[tuple[str, str, str]] = cursor.fetchall()
        cursor.close()
        close_connection(conn)
        rows = rows[::-1]  # Reverse the list
        items: list[dict] = []
        for row in rows:
            date_str = datetime.strptime(row[0], "%Y-%m-%d").strftime("%d/%m")
            items.append({"date": date_str, "state": row[1], "points": row[2]})
        return items
    except Exception as e:
        print(f"SQL Query Failure: {e}")
    return []
