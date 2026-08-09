"""
insert_test_data.py

Insert a handful of rows into the database for testing purposes.
"""

import os
import sqlite3

DB_PATH = os.path.join("db", "anime.db")

sample_anime = [
    {
    "title": "The Boy and the Heron",
    "title_japanese": "君たちはどう生きるか",
    "type": "Movie",
    "episodes": 1,
    "episodes_watched": 0,
    "studio": "Studio Ghibli",
    "release_season": "Summer", 
    "tags": "Animation, Slice of Life",
    "status": "Unknown",
    "rating": 7.7,
    "release_year": 2023,
    "end_year": 2023,
    "description": "While the Second World War rages, the teenage Mahito, haunted by his mother’s tragic death, is relocated from Tokyo to the serene rural home of his new stepmother Natsuko, a woman who bears a striking resemblance to the boy’s mother. As he tries to adjust, this strange new world grows even stranger following the appearance of a persistent gray heron, who perplexes and bedevils Mahito, dubbing him the “long-awaited one.”",
    "cover_image_path": "images/The_Boy_and_the_heron.jpg", 
    "content_warning": "Rated PG-13",
    "related_anime": None,
    "voice_actors": None,
    "staff": None
},
{
    "title": "Naruto",
    "title_japanese": "ナルト",
    "type": "TV",
    "episodes": 220,
    "episodes_watched": 0,
    "studio": "Studio Pierrot",
    "release_season": "Fall",
    "tags": "Action, Adventure, Fantasy",
    "status": "Unknown",
    "rating": 8.0,
    "release_year": 2002,
    "end_year": 2007,
    "description": "Naruto Uzumaki, a hyperactive and knuckle-headed ninja, lives in Konohagakure, the Hidden Leaf village. Moments prior to his birth, a huge demon known as the Kyuubi, the Nine-tailed Fox, attacked Konohagakure and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the 4th Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto. Shunned because of the presence of the Kyuubi inside him, Naruto struggles to find his place in the village. He strives to become the Hokage of Konohagakure, and he meets many friends and foes along the way.",
    "cover_image_path": "images/Naruto.jpg",
    "content_warning": "Rated PG-13",
    "related_anime": None,
    "voice_actors": None,
    "staff": None
},
{
    "title": "ONE PIECE FAN LETTER",
    "title_japanese": None,
    "type": "Special",
    "episodes": 1,
    "episodes_watched": 0,
    "studio": "Toei Animation",
    "release_season": "Fall",
    "tags": "Action, Adventure, Fantasy",
    "status": "Unknown",
    "rating": 9.0,
    "release_year": 2024,
    "end_year": 2024,
    "description": "To commemorate the 25th anniversary of the ONE PIECE TV anime: an animated adaptation of the ONE PIECE novel: Mugiwara Stories. Two years after the Paramount War, the Straw Hats are about to reunite on the Sabaody Archipelago. At the same time, a girl who is head over heels for Nami is trying to hand a fan letter to her before the group leaves the island.",
    "cover_image_path": "images/ONE_PIECE_FAN_LETTER.jpg",
    "content_warning": "Rated PG-13",
    "related_anime": None,
    "voice_actors": None,
    "staff": None
}
]

INSERT_SQL = """
INSERT INTO anime(
    title, title_japanese, type, episodes, episodes_watched, studio, release_season, tags, status, rating, release_year, end_year, description, cover_image_path, content_warning, related_anime, voice_actors, staff
) VALUES (
    :title, :title_japanese, :type, :episodes, :episodes_watched, :studio, :release_season, :tags, :status, :rating, :release_year, :end_year, :description, :cover_image_path, :content_warning, :related_anime, :voice_actors, :staff
)
"""

def drop_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM anime")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'anime'")
    conn.commit()
    conn.close()

def main():

    drop_table()
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executemany(INSERT_SQL, sample_anime)
    conn.commit()
    print(f"Inserted {len(sample_anime)} rows into the anime table.")


    print("Current rows in the anime table:")
    cursor.execute("SELECT * FROM anime")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    main()