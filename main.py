import tkinter as tk
from gui import MusicPlayerApp

def main():
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
