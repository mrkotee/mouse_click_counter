import os
import subprocess
import time
from datetime import datetime as dt

from pynput.mouse import Listener
# from tkinter import messagebox


# messagebox.showwarning('warn', 'sdf')
# messagebox.showerror("asdfs", "text")
# messagebox.showinfo("title", 'message')


class ClickCounter:

    def __init__(self):
        self.start_time = dt.now().replace(microsecond=0)
        self.glob_count = 0
        self.day_count = 0
        self.day_now = dt.now().day
        self.today_showed = False

    def on_click(self, x, y, button, pressed):
        if not pressed:
            return
        self.glob_count += 1
        self.day_count += 1
        # print(f"Mouse clicked {x=} {y=} {button=} {pressed=} {count}")

    def run(self):
        try:
            self.listener = Listener(on_click=self.on_click)
            self.listener.start()
            while True:
                time.sleep(1)
                if self.day_now != dt.now().day:
                    self.day_count = 0
                    self.today_showed = False
                    self.day_now = dt.now().day
                if self.day_count >= 3 and not self.today_showed:
                    message = f"Поздравляю!\nСегодня ты кликнул уже {self.day_count} раз\n"\
                            f"И {self.glob_count} раз начиная с {self.start_time.isoformat()}"
                    for msg in message.split("\n")[::-1]:
                        # subprocess.Popen(['notify-send', msg])
                        os.system(f"""notify-send "Счетчик кликов" "{msg}" """)
                        time.sleep(0.5)
                    self.today_showed = True
                    # messagebox.showinfo("Click counter",
                    #                     message=message)
        except KeyboardInterrupt:
            self.listener.stop()
