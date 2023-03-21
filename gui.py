from tkinter import *
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.time_label = Label(self.root, font=('Helvetica', 80))
        self.time_label.pack(padx=50, pady=50)
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

root = Tk()
app = DigitalClock(root)
root.mainloop()
