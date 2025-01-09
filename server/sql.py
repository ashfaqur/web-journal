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


def add_multiple_journal_entries(conn: Connection, entries: list[tuple[str, str, int]]):
    cursor = conn.cursor()
    cursor.executemany(
        """
        INSERT OR REPLACE INTO journal (date, state, points)
        VALUES (?, ?, ?)
        """,
        entries,
    )
    conn.commit()
    cursor.close()


def add_journal_entry(conn: Connection, date: str, entry: int, points: int):

    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO journal (date, state, points)
            VALUES (?, ?,?)
            """,
            (date, entry, points),
        )
        conn.commit()
        print("Entry added successfully.")
    except conn.IntegrityError as e:
        print(f"Failed to add entry: {e}")
    finally:
        cursor.close()


def insert_journal_entrys(
    entries: list[
        tuple[
            str,
            str,
            int,
        ]
    ]
):
    try:
        db_path = "build/example_database.db"
        conn = connect_to_db(db_path)
        create_table(conn)
        add_multiple_journal_entries(conn, entries)
        close_connection(conn)
    except Exception as e:
        print(f"Failed to add entry: {e}")


def get_last_thirty_days() -> list[dict]:
    try:
        db_path = "build/example_database.db"
        conn = connect_to_db(db_path)
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


# # Example usage
# db_path = "build/example_database.db"
# conn = connect_to_db(db_path)
# create_table(conn)
# add_journal_entry(conn, "2024-11-29", State)
# close_connection(conn)
