"""
main_functions.py

Core database functions for the anime tracker app. Each functions opens and closes its own connection.
"""

import sqlite3
import os

DB_PATH = os.path.join('db', 'anime.db')


def add_anime(row: dict):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    columns = list(row.keys())
    placeholders = [f":{col}" for col in columns]


    sql = f"""
    INSERT INTO anime ({', '.join(columns)})
    VALUES ({', '.join(placeholders)})
    """

    cursor.execute(sql, row)
    conn.commit()
    new_id = cursor.lastrowid

    conn.close()
    return new_id

def update_episodes_progress(anime_id: int, episodes_watched: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE anime SET episodes_watched = ? WHERE id = ?",
        (episodes_watched, anime_id)
    )

    conn.commit()
    rows_changed = cursor.rowcount
    conn.close()
    return rows_changed

def mark_completed(anime_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE anime SET status = 'Completed', episodes_watched = COALESCE(episodes, episodes_watched) WHERE id =?",
        (anime_id)
    )

    conn.commit()
    rows_changed = cursor.rowcount
    conn.close()
    return rows_changed

def delete_anime(anime_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM anime WHERE id = ?",
        (anime_id,)
    )

    conn.commit()
    rows_changed = cursor.rowcount
    conn.close()
    return rows_changed

def list_all():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM anime ORDER BY id")
    rows = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return rows