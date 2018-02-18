"""
Author: Wes Derflinger
"""

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    root = tkinter.Tk()
    root.title("Song Trivia")
    frame1 = ttk.Frame(root,  padding=40)
    frame1.grid()
    option_1_button = ttk.Button(frame1, text='Option 1')
    option_1_button.grid()
    option_2_button = ttk.Button(frame1, text='Option 2')
    option_2_button.grid()
    option_3_button = ttk.Button(frame1, text='Option 3')
    option_3_button.grid()
    option_4_button = ttk.Button(frame1, text='Option 4')
    option_4_button.grid()
    root.mainloop()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
