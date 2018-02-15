import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


class Items(object):
    def __init__(self, canvas):  # mqtt_client
        self.oval = canvas.create_oval(245, 245, 255, 255, fill='black')
        self.canvas = canvas
        self.destination = canvas.create_oval(0, 0, 0, 0, fill='blue')
        # self.mqtt_client = mqtt_client
        self.robot = canvas.create_oval(240, 240, 260, 260, fill='red')

    def move_to_destination(self, x, y, mqtt_client):
        self.canvas.coords(self.destination, x - 10, y - 10, x + 10,
                           y + 10)

        message = (x, 500 - y)

        mqtt_client.send_message('moveto', [message])


class MyDelegate(object):
    def __init__(self, root, items):
        self.root = root
        self.items = items

    def move_robot(self, data):
        print(data)
        x = data[0]
        y = 500 - data[1]

        self.items.canvas.coords(self.items.robot, x - 10, y - 10, x + 10,
                                 y + 10)
        self.root.update()

        # ???why not update

        # def add_item(self, items):
        #    self.items = items


def main():
    # frame creation
    root = tkinter.Tk()
    root.title = "MQTT Shared Circles"
    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()
    instructions = "Click the window to make the robot move"
    label = ttk.Label(main_frame, text=instructions)
    label.grid(columnspan=2)

    # Make a tkinter.Canvas on a Frame.
    canvas = tkinter.Canvas(main_frame, background="lightgray", width=500,
                            height=500)
    canvas.grid(row=2, column=1)

    # Make callbacks for mouse click events.
    canvas.bind("<Button-1>",
                lambda event: left_mouse_click(event, mqtt_client))

    robot_con = ttk.Button(main_frame, text='connect_robot')
    robot_con.grid(row=3, column=0)
    robot_con["command"] = lambda: robot_connection(items, mqtt_client)

    # Make callbacks for the two buttons.
    back_button = ttk.Button(main_frame, text="back_to_origion")
    back_button.grid(row=3, column=1)
    back_button["command"] = lambda: back(mqtt_client)

    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=3, column=2)
    quit_button["command"] = lambda: quit_program(mqtt_client)

    # Create an MQTT connection
    global items
    items = Items(canvas)
    my_delegate = MyDelegate(root, items)
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter event handlers
# Left mouse click
# ----------------------------------------------------------------------
def robot_connection(items, mqtt):
    mqtt.send_message('robotconnection')


def left_mouse_click(event, mqtt_client):
    """ Draws a circle onto the canvas (one way or another). """

    x = event.x
    y = event.y
    items.move_to_destination(x, y, mqtt_client)


def back(mqtt_client):
    """Clears the canvas contents"""
    items.move_to_destination(250, 250, mqtt_client)


def quit_program(mqtt_client):
    """For best practice you should close the connection.  Nothing really "bad" happens if you
       forget to close the connection though. Still it seems wise to close it then exit."""
    mqtt_client.send_message('shutdown')
    if mqtt_client:
        mqtt_client.close()
    exit()


main()
