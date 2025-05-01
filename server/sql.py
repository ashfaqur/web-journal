import sqlite3
from datetime import datetime
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


def get_last_thirty_days(journal_database_path_env: str) -> list[dict]:
    try:
        conn = connect_to_db(journal_database_path_env)
        create_table(conn)
        cursor = conn.cursor()
        # get todays date in format YYYY-MM-DD
        date = datetime.now().strftime("%Y-%m-%d")
        # make query for last 30 days given todays date
        cursor.execute(
            """
            SELECT date, state, points
            FROM journal
            WHERE date <= ?
            ORDER BY date DESC
            LIMIT 30
            """,
            (date,),
        )
        rows = cursor.fetchall()
        cursor.close()
        close_connection(conn)
        rows = rows[::-1]  # Reverse the list
        items: list[dict] = []
        for row in rows:
            date_str = datetime.strptime(row[0], "%Y-%m-%d").strftime("%d/%m")
            items.append({"date": date_str, "state": row[1], "points": row[2]})
        return items
    except Exception as e:
        print(f"Failed to add entry: {e}")
    return []

