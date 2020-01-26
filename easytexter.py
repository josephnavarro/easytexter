#! usr/bin/env python3
import subprocess
import tkinter
import os
from tkinter import Tk, Label, Text, Button, Frame


WIDTH = 560
HEIGHT = 135
COLOR = "#ccc"
TITLE = "EasyTexter"
BUTTON_LABEL = "Send"


def callback(root) -> None:
    """
    Callback function for text entry.
    """
    string = escapify(root.text_entry.get(1.0, tkinter.END))
    cwd = os.getcwd()
    adbpath = os.path.join(cwd, "adb.exe")
    cmd = "{} shell input text \"{}\"".format(adbpath, string)
    subprocess.call("{} -d".format(adbpath), shell=True)
    subprocess.call(cmd, shell=True)
    root.text_entry.delete(1.0, tkinter.END)


def init_button(root) -> None:
    """
    Initializes button for master GUI window.
    """
    root.button = Button(
        root.frame,
        bg=COLOR,
        text=BUTTON_LABEL,
        command=lambda: callback(root)
        )
    root.button.place(relx=0.5, rely=0.95, anchor=tkinter.S)


def init_entry(root) -> None:
    """
    Initializes entry forms for master GUI window.
    """
    root.text_entry = Text(root.frame, width=76, height=6)
    root.text_entry.place(x=12, y=12, anchor=tkinter.NW)


def init_frame(root) -> None:
    """
    Initializes frame bounds for master GUI window.
    """
    root.frame = Frame(bg=COLOR, width=WIDTH, height=HEIGHT)
    root.frame.pack()


def init_window() -> Tk:
    """
    Initializes master GUI window.
    """
    root = Tk()
    root.resizable(False, False)
    root.title(TITLE)

    return root


def escapify(string) -> str:
    """
    Replaces all spaces in a string with '%s'.
    """
    return '%s'.join(string.replace("'", "\\'").replace("\"", "\\\"").replace("$", "\\$").split())


def main():
    """
    Main method.
    """
    root = init_window()
    init_frame(root)
    init_entry(root)
    init_button(root)

    root.mainloop()



if __name__ == "__main__":
    main()
