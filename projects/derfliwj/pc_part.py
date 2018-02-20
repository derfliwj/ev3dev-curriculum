"""
Author: Wes Derflinger
"""

import tkinter
from tkinter import ttk
import ev3dev.ev3 as ev3
import mqtt_remote_method_calls as com


class MyDelegate(object):

    def __init__(self):
        self.song_color = "Red"

    def get_color(self, color):
        self.song_color = color


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Guess the Artist!")
    frame1 = ttk.Frame(root,  padding=40)
    frame1.grid()

    option_1_label = ttk.Label(frame1, text='A.')
    option_1_label.grid(row=0, column=0)

    option_2_label = ttk.Label(frame1, text='B.')
    option_2_label.grid(row=1, column=0)

    option_3_label = ttk.Label(frame1, text='C.')
    option_3_label.grid(row=2, column=0)

    option_4_label = ttk.Label(frame1, text='D.')
    option_4_label.grid(row=3, column=0)

    if my_delegate.song_color == "Red":
        drive_color(mqtt_client, "Red")

        option_1_button = ttk.Button(frame1, text='Guns N Roses')
        option_1_button.grid(row=0, column=1)
        option_1_button['command'] = lambda: print("Wrong! Guess Again!")

        option_2_button = ttk.Button(frame1, text='Metallica')
        option_2_button.grid(row=1, column=1)
        option_2_button['command'] = lambda: print("Correct!")
        option_2_button['command'] = lambda: drive_color(mqtt_client, "Blue")

        option_3_button = ttk.Button(frame1, text='Justin Bieber')
        option_3_button.grid(row=2, column=1)
        option_3_button['command'] = lambda: print("Wrong! Guess Again!")

        option_4_button = ttk.Button(frame1, text='Megadeth')
        option_4_button.grid(row=3, column=1)
        option_4_button['command'] = lambda: print("Wrong! Guess Again!")

    elif my_delegate.song_color == "Blue":
        option_1_button = ttk.Button(frame1, text='Jason Aldean')
        option_1_button.grid(row=0, column=1)
        option_1_button['command'] = lambda: print("Wrong! Guess Again!")

        option_2_button = ttk.Button(frame1, text='Florida Georgia Line')
        option_2_button.grid(row=1, column=1)
        option_2_button['command'] = lambda: print("Wrong! Guess Again!")

        option_3_button = ttk.Button(frame1, text='Luke Bryan')
        option_3_button.grid(row=2, column=1)
        option_3_button['command'] = lambda: print("Correct!")
        option_3_button['command'] = lambda: drive_color(mqtt_client, "Green")

        option_4_button = ttk.Button(frame1, text='George Straight')
        option_4_button.grid(row=3, column=1)
        option_4_button['command'] = lambda: print("Wrong! Guess Again!")

    elif my_delegate.song_color == "Green":
        option_1_button = ttk.Button(frame1, text='Jimmy Eat World')
        option_1_button.grid(row=0, column=1)
        option_1_button['command'] = lambda: print("Wrong! Guess Again!")

        option_2_button = ttk.Button(frame1, text='Third Eye Blind')
        option_2_button.grid(row=1, column=1)
        option_2_button['command'] = lambda: print("Correct!")
        option_2_button['command'] = lambda: print("You Win")

        option_3_button = ttk.Button(frame1, text='Blink-182')
        option_3_button.grid(row=2, column=1)
        option_3_button['command'] = lambda: print("Wrong! Guess Again!")

        option_4_button = ttk.Button(frame1, text='A Day to Remember')
        option_4_button.grid(row=3, column=1)
        option_4_button['command'] = lambda: print("Wrong! Guess Again!")

    root.mainloop()


def drive_color(mqtt_client, color):
    if color == "Red":
        color = ev3.ColorSensor.COLOR_RED
    elif color == "Blue":
        color = ev3.ColorSensor.COLOR_BLUE
    elif color == "Green":
        color = ev3.ColorSensor.COLOR_GREEN
    mqtt_client.send_message("drive_to_color", [color])


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
