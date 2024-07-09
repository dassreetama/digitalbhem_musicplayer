import os
from tkinter import filedialog

def open_music_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    return file_path

def save_playlist(playlist, file_path):
    with open(file_path, 'w') as f:
        for music_file in playlist:
            f.write(music_file + '\n')

def load_playlist(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            playlist = [line.strip() for line in f.readlines()]
        return playlist
    else:
        return []
