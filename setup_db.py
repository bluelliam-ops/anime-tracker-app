"""
setup.py file for the project.

Creates the db and 'anime' table for the app.
"""

import sqlite3
import os

DB_PATH = os.path.join('db', 'anime.db')

os.makedirs('db', exist_ok=True)

SCHEMA = """
CREATE TABLE IF NOT EXISTS anime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    title_japanese TEXT,
    type TEXT,
    episodes INTEGER,
    episodes_watched INTEGER NOT NULL DEFAULT 0,
    studio TEXT,
    release_season TEXT,
    tags TEXT,
    status TEXT NOT NULL DEFAULT 'Unknown'
        CHECK (status IN ('Completed', 'Dropped', 'On Hold', 'Watching', 'Plan to Watch', 'Unknown')),
    rating REAL
        CHECK (rating >= 0 AND rating <= 10),
    release_year INTEGER,
    end_year INTEGER,
    description TEXT,
    cover_image_path TEXT,
    content_warning TEXT,
    related_anime TEXT,
    voice_actors TEXT,
    staff TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
);
"""

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(SCHEMA)
    conn.commit()
    conn.close()
    print(f"Database created at {DB_PATH}")

if __name__ == "__main__":
    main()