"""
query_practice.py

A file to practice queries with the anime tracker database. This file is not part of the main application and is only used for testing and learning purposes.
"""

import sqlite3
import os

DB_PATH = os.path.join('db', 'anime.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


def run_query(query):
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def sql_head(table_name):

    table_head_query = """SELECT * FROM {} LIMIT 5;""".format(table_name)

    cursor.execute(table_head_query)

    return cursor.fetchall()


run_query("""SELECT * FROM anime""")

sql_head("anime")

run_query(
    """SELECT * FROM anime WHERE rating >= 8.0"""
)

run_query(
    """SELECT * FROM anime WHERE episodes <= 1"""
)

run_query(
    """SELECT * FROM anime ORDER BY rating DESC"""
)

run_query(
    """SELECT * FROM anime WHERE release_season = 'Fall' """
)


conn.close()