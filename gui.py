import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from player import MusicPlayer
from playlist import PlaylistManager
import file_manager

class MusicPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("800x600")

        self.player = MusicPlayer()
        self.playlist_manager = PlaylistManager()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Menu Bar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open File", command=self.open_music_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Controls Frame
        controls_frame = tk.Frame(self.master, padx=20, pady=10)
        controls_frame.pack(side=tk.TOP, fill=tk.X)

        self.play_button = tk.Button(controls_frame, text="Play", command=self.play_music)
        self.play_button.grid(row=0, column=0, padx=10)

        self.pause_button = tk.Button(controls_frame, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.grid(row=0, column=1, padx=10)

        self.stop_button = tk.Button(controls_frame, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=2, padx=10)

        # Playlist Frame
        playlist_frame = tk.Frame(self.master)
        playlist_frame.pack(fill=tk.BOTH, expand=True)

        self.playlist_listbox = tk.Listbox(playlist_frame, selectmode=tk.SINGLE, bg="#121212", fg="#FFFFFF",
                                           selectbackground="#1ED760", selectforeground="#FFFFFF", height=20,
                                           font=("Helvetica", 12))
        self.playlist_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=10)

        scrollbar = ttk.Scrollbar(playlist_frame, orient="vertical", command=self.playlist_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.playlist_listbox.config(yscrollcommand=scrollbar.set)

        # Bind double click on playlist item to play_music function
        self.playlist_listbox.bind('<Double-1>', lambda event: self.play_selected())

    def play_music(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            music_file = self.playlist_manager.get_playlist()[index]
            self.fade_out_widgets()  # Start fade out animation
            self.master.after(500, lambda: self.player.play(music_file))  # Delay play by 500ms for animation
            self.master.after(1000, self.fade_in_widgets)  # Start fade in animation after 1 second
            self.update_buttons_state()

    def fade_out_widgets(self):
        for button in [self.play_button, self.pause_button, self.stop_button]:
            button.config(state=tk.DISABLED)

    def fade_in_widgets(self):
        for button in [self.play_button, self.pause_button, self.stop_button]:
            button.config(state=tk.NORMAL)

    def pause_music(self):
        self.player.pause()
        self.update_buttons_state()

    def stop_music(self):
        self.player.stop()
        self.update_buttons_state()

    def open_music_file(self):
        file_path = file_manager.open_music_file()
        if file_path:
            self.playlist_manager.add_to_playlist(file_path)
            self.playlist_listbox.insert(tk.END, os.path.basename(file_path))

    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.playlist_manager.remove_from_playlist(index)
            self.playlist_listbox.delete(index)

    def play_selected(self):
        self.play_music()

    def update_buttons_state(self):
        if self.player.get_busy():
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
        else:
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)