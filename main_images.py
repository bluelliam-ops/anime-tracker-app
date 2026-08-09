"""
main.py

The current main GUI made using CustomTiknter to run the anime-tracker app.
"""

import customtkinter as ctk
from PIL import Image
import tkinter as messagebox

import main_functions as mf

ctk.set_appearance_mode("light")

class AnimeTrackerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Anime Tracker")
        self.geometry("1000x800")

        self.selected_id = None
        self.selected_row_frame = None

        self.build_widgets()
        self.refresh_list()

    def build_widgets(self):

        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.pack(padx=20, pady=(20, 0), fill="both", expand=True)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(padx=20, pady=20, fill="x")

        ctk.CTkButton(button_frame, text="Add Anime", command=self.add_anime).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(button_frame, text="Update Episodes Progress", command=self.update_episodes_progress).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(button_frame, text="Mark Completed", command=self.mark_completed).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(button_frame, text="Delete Anime", command=self.delete_anime).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(button_frame, text="Refresh List", command=self.refresh_list).pack(side="left", padx=10, pady=10)

        self.theme_switch = ctk.CTkSwitch(
            button_frame,
            text="Dark Mode Off",
            command=self.toggle_theme,
            onvalue=1,
            offvalue=0,
        )
        self.theme_switch.pack(side="right", padx=10, pady=10)

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        self.selected_id = None
        self.selected_row_frame = None

        for anime in mf.list_all():
            self._add_row(anime)

    def _add_row(self, anime):
        watched = anime["episodes_watched"]
        total = anime["episodes"] if anime["episodes"] is not None else "?"
        rating = anime["rating"] if anime ["rating"] is not None else "?"

        row = ctk.CTkFrame(self.list_frame)
        row.pack(padx=3, pady=3, fill="x")

        title_label = ctk.CTkLabel(row, text=anime["title"], width=250, anchor="w")
        status_label = ctk.CTkLabel(row, text=anime["status"], width=120, anchor="w")
        progress_label = ctk.CTkLabel(row, text=f"{watched}/{total}", width=80, anchor="w")
        rating_label = ctk.CTkLabel(row, text=str(rating), width=60, anchor="w")

        title_label.pack(side="left", padx=5, pady=5)
        status_label.pack(side="left", padx=5)
        progress_label.pack(side="left", padx=5)
        rating_label.pack(side="left", padx=5)

        for widget in (row, title_label, status_label, progress_label, rating_label):
            widget.bind("<Button-1>", lambda event, a=anime, r=row: self._select_row(a, r))

    def _select_row(self, anime, row_frame):
        if self.selected_row_frame is not None:
            self.selected_row_frame.configure(fg_color="transparent")

        row_frame.configure(fg_color="#a3a3a3")
        self.selected_row_frame = row_frame
        self.selected_id = anime["id"]

    def _require_selection(self):
        if self.selected_id is None:
            messagebox.showwarning("No selection", "Click an anime in the list")
            return None
        return self.selected_id

    def add_anime(self):
        title_dialog = ctk.CTkInputDialog(text="Title:", title="Add Anime")
        title = title_dialog.get_input()
        if not title:
            return

        status_dialog = ctk.CTkInputDialog(text="Enter Status: (Completed, Dropped, On Hold, Watching, Plan to Watch, Unknown)", title = "Add Anime")
        status = status_dialog.get_input()
        if not status:
            return

        rating_dialog = ctk.CTkInputDialog(text="Rating:", title="Add Anime")
        rating = rating_dialog.get_input()
        if not status:
            return

        episodes_dialog = ctk.CTkInputDialog(text="Total episodes", title="Add Anime")
        episodes_str = episodes_dialog.get_input()

        row = {"title": title, "status": status, "rating": rating}
        if episodes_str:
            try:
                row["episodes"] = int(episodes_str)
            except ValueError:
                messagebox.showerror("Invalid input", "Episodes must be a number.")
                return

            mf.add_anime(row)
            self.refresh_list()

    def update_episodes_progress(self):
        anime_id = self._require_selection()
        if anime_id is None:
            return

        dialog = ctk.CTkInputDialog(text="Episodes watched:", title="Update Progress")
        watched_str = dialog.get_input()
        if not watched_str:
            return

        try:
            watched = int(watched_str)
        except ValueError:
            messagebox.showerror("Invalid input", "Episodes must be a number.")
            return

        mf.update_episodes_progress(anime_id, watched)
        self.refresh_list()

    def mark_completed(self):
        anime_id = self._require_selection()
        if anime_id is None:
            return

        mf.mark_completed(anime_id)
        self.refresh_list()

    def delete_anime(self):
        anime_id = self._require_selection()
        if anime_id is None:
            return

        mf.delete_anime(anime_id)
        self.refresh_list()

    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("dark")
            self.theme_switch.configure(text="Dark Mode On")
        else:
            ctk.set_appearance_mode("light")
            self.theme_switch.configure(text="Dark Mode Off")




def main():
    app = AnimeTrackerApp()
    app.mainloop()

if __name__ == "__main__":
    main()