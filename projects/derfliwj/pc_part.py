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
    option_1_label = ttk.Label(frame1, text='A.')
    option_1_button = ttk.Button(frame1, )
    option_1_label.grid(row=0, column=0)
    option_2_label = ttk.Label(frame1, text='B.')
    option_2_label.grid(row=1, column=0)
    option_3_label = ttk.Label(frame1, text='C.')
    option_3_label.grid(row=2, column=0)
    option_4_label = ttk.Label(frame1, text='D.')
    option_4_label.grid(row=3, column=0)
    root.mainloop()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
