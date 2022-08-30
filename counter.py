import time
from datetime import datetime as dt

from pynput.mouse import Listener
from tkinter import messagebox

# messagebox.showwarning('warn', 'sdf')
# messagebox.showerror("asdfs", "text")
# messagebox.showinfo("title", 'message')

start_time = dt.now().replace(microsecond=0)
glob_count = 0
day_count = 0
day_now = dt.now().day
today_showed = False


def on_click(x, y, button, pressed):
    if not pressed:
        return
    global glob_count
    glob_count += 1
    global day_count
    day_count += 1
    # print(f"Mouse clicked {x=} {y=} {button=} {pressed=} {count}")


listener = Listener(on_click=on_click)
listener.start()

try:
    while True:
        time.sleep(1)
        if day_now != dt.now().day:
            day_count = 0
            today_showed = False
            day_now = dt.now().day
        if day_count >= 500:
            messagebox.showinfo("Click counter", message=f"Поздравляю!\nСегодня ты кликнул уже {day_count} раз\n"
                                                         f"И {glob_count} раз начиная с {start_time.isoformat()}")
except KeyboardInterrupt:
    listener.stop()
