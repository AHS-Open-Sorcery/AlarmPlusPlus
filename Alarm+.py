
import tkinter as tk
from tkinter import messagebox, Button, Label
import cv2


window = None
instrument = None
timer = -1
FRAME_UPDATE_MS = 10
SCREEN_WIDTH, SCREEN_HEIGHT = 0, 0


def center_window(width, height):
    global window
    coords = center_coords(width, height)
    window.geometry("%dx%d%+d%+d" % (width, height, coords[0], coords[1]))


def center_coords(width, height):
    global SCREEN_HEIGHT, SCREEN_WIDTH
    return ((SCREEN_WIDTH - width) // 2, (SCREEN_HEIGHT - height) // 2)


def close_popup():
    global window
    window.destroy()
    window.update()


def popup_message(message):
    global window
    window = tk.Toplevel()
    window.title("TITLE HERE")
    label = tk.Label(window, text=message)
    label.pack()
    b = Button(window, text="Close", command=close_popup)
    b.pack()


def create_alarm():
    pass


def init_tk():
    submit = Button(root, text="Create Alarm", command=create_alarm)
    submit.pack()


    pass


width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.title("AirGuitar")
coords = center_coords(width, height)
root.geometry("%dx%d%+d%+d" % (width, height, coords[0], coords[1]))
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

root.mainloop()

