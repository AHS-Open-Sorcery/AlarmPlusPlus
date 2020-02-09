
import tkinter as tk
from tkinter import messagebox, Button, Label
import cv2
from PIL import Image, ImageTk
import enum

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


def choose_instrument(chosen):
    global instrument, timer, window, FRAME_UPDATE_MS
    instrument = chosen
    close_popup()
    window = tk.Toplevel()
    center_window(250, 50)
    window.title(chosen.name)
    label = Label(window, text="You have selected " + chosen.name)
    label.pack()
    timer = 1000 / FRAME_UPDATE_MS


def instrument_select():
    global window
    window = tk.Toplevel()
    center_window(800, 600)

    window.title("Instrument Select")
    for data in Instrument:
        b = Button(window, text=data.name)
        b['command'] = lambda a=data: choose_instrument(a)
        b.pack()


def show_frame():
    global timer, FRAME_UPDATE_MS

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(FRAME_UPDATE_MS, show_frame)
    if timer >= 0:
        timer -= 1
    if timer == 0:
        close_popup()


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

b = Button(root, text="Instrument", command=instrument_select)
b.pack()
show_frame()
root.mainloop()

