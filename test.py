import tkinter as tk
import time

class ScreenSaver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='black')
        self.time_label = tk.Label(self, font=('Helvetica', 100), fg='gray', bg='black')
        self.time_label.pack(expand=True, fill='both')
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.after(1000, self.update_time)

if __name__ == '__main__':
    screensaver = ScreenSaver()
    screensaver.attributes('-fullscreen', True)
    screensaver.bind("<Escape>", lambda event: screensaver.destroy())
    screensaver.mainloop()