"""
menu.py

A print based menu for the anime tracker app. Used to test main_functions.py.
"""

import main_functions as mf

def handle_add_anime():
    title = input("Enter the title of the anime: ").strip()
    title_japanese = input("Enter the Japanese title (leave blank if unknown): ").strip()
    type_ = input("Enter the type (TV, Movie, OVA, etc.): ").strip()
    episodes = int(input("Enter the number of episodes: "))
    studio = input("Enter the studio: ").strip()
    release_season = input("Enter the release season (Spring, Summer, Fall, Winter): ").strip()
    tags = input("Enter tags (comma-separated): ").strip()
    status = input("Enter the status (Completed, Dropped, On Hold, Watching, Plan to Watch, Unknown): ").strip()
    rating = float(input("Enter the rating (0-10): "))
    release_year = int(input("Enter the release year: "))
    end_year = int(input("Enter the end year (or leave blank for ongoing): ") or 0)
    description = input("Enter a description: ").strip()
    cover_image_path = input("Enter the cover image path: ").strip()
    content_warning = input("Enter any content warnings (or leave blank): ").strip()
    related_anime = input("Enter related anime (comma-separated): ").strip()
    voice_actors = input("Enter voice actors (comma-separated): ").strip()
    staff = input("Enter staff members (comma-separated): ").strip()

    row = {
        "title": title,
        "title_japanese": title_japanese if title_japanese else None,
        "type": type_,
        "episodes": episodes,
        "episodes_watched": 0,
        "studio": studio,
        "release_season": release_season,
        "tags": tags,
        "status": status,
        "rating": rating,
        "release_year": release_year,
        "end_year": end_year if end_year != 0 else None,
        "description": description,
        "cover_image_path": cover_image_path,
        "content_warning": content_warning if content_warning else None,
        "related_anime": related_anime if related_anime else None,
        "voice_actors": voice_actors if voice_actors else None,
        "staff": staff if staff else None
    }

    new_id = mf.add_anime(row)
    print(f"Anime added with ID: {new_id}")

def handle_episodes_progress():
    anime_id = int(input("Enter the anime ID to update episodes watched:").strip())
    episodes_watched = int(input("Enter the number of episodes watched:").strip())
    changed = mf.update_episodes_progress(anime_id, episodes_watched)
    if changed:
        print(f"Episodes watched updated for anime ID {anime_id}.")
    else:
        print(f"No anime found with id {anime_id}.")

def handle_mark_completed():
    anime_id = int(input("Enter the anime ID to mark as completed:").strip())
    changed = mf.mark_completed(anime_id)
    if changed:
        print(f"Anime ID {anime_id} marked as completed.")
    else:
        print(f"No anime found with id {anime_id}.")

def handle_delete_anime():
    anime_id = int(input("Enter the anime ID to delete:").strip())
    changed = mf.delete_anime(anime_id)
    if changed:
        print(f"Anime ID {anime_id} deleted.")
    else:
        print(f"No anime found with id {anime_id}.")

def print_anime_list():
    anime_list = mf.list_all()
    if not anime_list:
        print("No anime found in the database.")
        return

    print("\nCurrent Anime List:")
    for anime in anime_list:
        watched = anime['episodes_watched']
        total = anime['episodes'] if anime['episodes'] is not None else "?"
        rating = anime['rating'] if anime['rating'] is not None else "N/A"
        print(f"{anime['id']:<4}{anime['title']:<35}{anime['status']:<15}{f'{watched}/{total}':<10}{rating:<6}")

def main():

    actions = {
        "1": ("Add Anime", handle_add_anime),
        "2": ("Update Episodes Progress", handle_episodes_progress),
        "3": ("Mark as Completed", handle_mark_completed),
        "4": ("Delete Anime", handle_delete_anime),
        "5": ("Print Anime List", print_anime_list),
        "6": ("Exit", None)
    }

    while True:
        print("\n--------- Anime Tracker Menu ---------")
        for key, (description, _) in actions.items():
            print(f"{key}. {description}")

        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Exiting the menu. Goodbye!")
            break
        elif choice in actions:
            actions[choice][1]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()