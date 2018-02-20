"""
Song Trivia on the PC side!!!!
Author: Wes Derflinger
"""

import tkinter
from tkinter import ttk
import ev3dev.ev3 as ev3
import mqtt_remote_method_calls as com


class MyDelegate(object):

    def __init__(self):
        """Constructs a delegate specific to the PC!"""
        self.song_color = "Red"
        self.option_1_button = None
        self.option_2_button = None
        self.option_3_button = None
        self.option_4_button = None
        self.label = None

    def get_color(self, color):
        """Obtains the color the color sensor on the robot reads!"""
        self.song_color = color

    def set_gui_1(self, frame1, mqtt_client):
        """Sets first song options!"""
        self.label = ttk.Label(frame1, text='Song 1!')
        self.label.grid(row=0, column=1)

        self.option_1_button = ttk.Button(frame1, text='Guns N Roses')
        self.option_1_button.grid(row=1, column=1)
        self.option_1_button['command'] = lambda: print("Wrong! Guess Again!")

        self.option_2_button = ttk.Button(frame1, text='Metallica')
        self.option_2_button.grid(row=2, column=1)
        self.option_2_button['command'] = lambda: drive_color(mqtt_client, "Blue")

        self.option_3_button = ttk.Button(frame1, text='Justin Bieber')
        self.option_3_button.grid(row=3, column=1)
        self.option_3_button['command'] = lambda: print("Wrong! Guess Again!")

        self.option_4_button = ttk.Button(frame1, text='Megadeth')
        self.option_4_button.grid(row=4, column=1)
        self.option_4_button['command'] = lambda: print("Wrong! Guess Again!")

    def set_gui_2(self, frame1, mqtt_client):
        """Sets second song options!"""
        self.label = ttk.Label(frame1, text='Song 2!')
        self.label.grid(row=0, column=1)

        self.option_1_button = ttk.Button(frame1, text='Jason Aldean')
        self.option_1_button.grid(row=1, column=1)
        self.option_1_button['command'] = lambda: print("Wrong! Guess Again!")

        self.option_2_button = ttk.Button(frame1, text='Florida Georgia Line')
        self.option_2_button.grid(row=2, column=1)
        self.option_2_button['command'] = lambda: print("Wrong! Guess Again!")

        self.option_3_button = ttk.Button(frame1, text='Luke Bryan')
        self.option_3_button.grid(row=3, column=1)
        self.option_3_button['command'] = lambda: drive_color(mqtt_client, "Black")

        self.option_4_button = ttk.Button(frame1, text='George Straight')
        self.option_4_button.grid(row=4, column=1)
        self.option_4_button['command'] = lambda: print("Wrong! Guess Again!")

    def set_gui_3(self, frame1, mqtt_client):
        """Sets third song options!"""
        self.label = ttk.Label(frame1, text='Song 3!')
        self.label.grid(row=0, column=1)

        self.option_1_button = ttk.Button(frame1, text='Jimmy Eat World')
        self.option_1_button.grid(row=1, column=1)
        self.option_1_button['command'] = lambda: print("Wrong! Guess Again!")

        self.option_2_button = ttk.Button(frame1, text='Third Eye Blind')
        self.option_2_button.grid(row=2, column=1)
        self.option_2_button['command'] = lambda: quit_program(mqtt_client)

        self.option_3_button = ttk.Button(frame1, text='Blink-182')
        self.option_3_button.grid(row=3, column=1)
        self.option_3_button['command'] = lambda: print("Wrong! Guess Again!")

        self.option_4_button = ttk.Button(frame1, text='A Day to Remember')
        self.option_4_button.grid(row=4, column=1)
        self.option_4_button['command'] = lambda: print("Wrong! Guess Again!")


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Guess the Song Artist!")
    frame1 = ttk.Frame(root, padding=40)
    frame2 = ttk.Frame(root, padding=40)
    frame3 = ttk.Frame(root, padding=40)
    frame1.grid()
    frame2.grid()
    frame3.grid()

    drive_color(mqtt_client, "Red")
    my_delegate.set_gui_1(frame1, mqtt_client)
    my_delegate.set_gui_2(frame2, mqtt_client)
    my_delegate.set_gui_3(frame3, mqtt_client)

    root.mainloop()


def drive_color(mqtt_client, color):
    """Communicates to the robot which color it should drive to!"""
    if color == "Red":
        color = ev3.ColorSensor.COLOR_RED
        print("Correct!")
    elif color == "Blue":
        color = ev3.ColorSensor.COLOR_BLUE
        print("Correct!")
    elif color == "Black":
        color = ev3.ColorSensor.COLOR_BLACK
        print("Correct!")
    mqtt_client.send_message("drive_to_color", [color])


def quit_program(mqtt_client):
    """Quits the program!"""
    print("Correct! You Win!!")
    mqtt_client.send_message("shutdown")
    mqtt_client.close()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
