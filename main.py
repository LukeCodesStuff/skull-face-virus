from pynput import mouse
import tkinter as tk
import threading
from PIL import Image, ImageTk
from playsound3 import playsound
import sys
import time

frozen = False

# ------------------ Mouse freeze logic ------------------
def freeze_loop():
    x, y = controller.position  # get current mouse coordinates
    while frozen:
        controller.position = (x, y)  # keep the mouse at the same spot
        time.sleep(0.01)

def freeze():
    global frozen
    frozen = True
    t = threading.Thread(target=freeze_loop)
    t.start()

def unfreeze():
    global frozen
    frozen = False

# ------------------ Overlay logic ------------------
def start_overlay():
    duration_ms = 3000  # overlay duration
    skull_offset_y = 200  # pixels below center

    # Freeze the mouse
    freeze()

    # Initialize Tkinter window
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.75)  # semi-transparent
    root.configure(bg="gray")

    # Exit function
    def exit_app(event=None):
        unfreeze()  # make sure mouse is not frozen
        root.destroy()
        sys.exit()

    root.bind("<Escape>", exit_app)
    root.after(duration_ms, exit_app)  # auto-close after 3 seconds
    root.after(duration_ms, unfreeze)  # unfreeze after overlay

    # Play music (non-blocking)
    playsound(r"funk1.mp3", block=False)

    # Load skull image
    img = Image.open(r"skullface1.png")
    img = img.resize((400, 400))
    skull = ImageTk.PhotoImage(img)

    # Screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width // 2
    y = screen_height // 2 + skull_offset_y

    label = tk.Label(root, image=skull, bg="gray")
    label.place(x=x, y=y, anchor="center")

    root.mainloop()

# ------------------ Wait for click ------------------
controller = mouse.Controller()  # create controller to read/freeze mouse

# print("Waiting for mouse click...")

with mouse.Events() as events:   # blocks until a mouse event
    for event in events:
        if isinstance(event, mouse.Events.Click):
            start_overlay()       # run overlay on click
            break                 # exit loop after first click