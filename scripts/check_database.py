# checking the three tables where loaded succesfully in database

import sqlite3


def check_tables():
    """Display all tables available in the SQLite database."""
    conn = sqlite3.connect("bluestock_mf.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    tables = cursor.fetchall()

    print("Tables loaded successfully:")
    for table in tables:
        print(table[0])

    conn.close()


if __name__ == "__main__":
    check_tables()