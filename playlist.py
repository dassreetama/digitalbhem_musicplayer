class PlaylistManager:
    def __init__(self):
        self.playlist = []

    def add_to_playlist(self, music_file):
        self.playlist.append(music_file)

    def remove_from_playlist(self, index):
        if 0 <= index < len(self.playlist):
            del self.playlist[index]

    def clear_playlist(self):
        self.playlist = []

    def get_playlist(self):
        return self.playlist

    def save_playlist(self, file_path):
        with open(file_path, 'w') as f:
            for music_file in self.playlist:
                f.write(music_file + '\n')

    def load_playlist(self, file_path):
        with open(file_path, 'r') as f:
            self.playlist = [line.strip() for line in f.readlines()]
