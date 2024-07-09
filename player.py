import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.paused = False
        self.stopped = True
        self.current_music = None

    def play(self, music_file):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            if self.stopped or self.current_music != music_file:
                pygame.mixer.music.load(music_file)
                self.stopped = False
                self.current_music = music_file
            pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.stopped = True

    def get_busy(self):
        return pygame.mixer.music.get_busy()
