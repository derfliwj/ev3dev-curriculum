import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import math


# the items class store all the information about the canvas and all the
# point on it. It only have one method, which move the point to a new location
class Items(object):
    def __init__(self, canvas):  # mqtt_client
        self.oval = canvas.create_oval(245, 245, 255, 255, fill='black')
        self.canvas = canvas
        self.destination = canvas.create_oval(0, 0, 0, 0, fill='blue')
        self.robot = canvas.create_oval(240, 240, 260, 260, fill='red')
        self.direction = canvas.create_oval(258, 248, 262, 252, fill='black')

    def move_to_destination(self, x, y, mqtt_client):
        self.canvas.coords(self.destination, x - 10, y - 10, x + 10,
                           y + 10)
        # in the canvas, down is the positive y direction, so that a 500 - y
        #  is need to flip the positive direction
        message = (x, 500 - y)

        mqtt_client.send_message('moveto', [message])


class MyDelegate(object): 
    def __init__(self, root, items):
        self.root = root
        self.items = items

    def move_robot(self, data):
        # the move _robot method gather the robot location send by the robot
        #  and display it on the canvas. Due to the canvas downard positive
        # direction, a 500 - y is needed to flip the direction
        x = data[0]
        y = 500 - data[1]
        angle = data[2]
        dir_x = x + math.cos(-(angle * 3.14 / 180)) * 10
        dir_y = y + math.sin(-(angle * 3.14 / 180)) * 10
        self.items.canvas.coords(self.items.robot, x - 10, y - 10, x + 10,
                                 y + 10)
        self.items.canvas.coords(self.items.direction, dir_x - 2, dir_y - 2,
                                 dir_x + 2,
                                 dir_y + 2)

        self.root.update()

    def obstacle(self, data):
        # the obstacle method gather the obstacle location send by the robot
        #  and display it on canvas, it create a yellow circle to indicate
        # the obstacle
        x = data[0]
        y = 500 - data[1]
        self.items.canvas.create_oval(x - 10, y - 10, x + 10, y + 10,
                                      fill='yellow')


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

    robot_con = ttk.Button(main_frame, text='check_connection')
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
    """ Draws a circle onto the canvas  """
    # this function get the x,y input on the canvas and send it to the robot
    x = event.x
    y = event.y
    items.move_to_destination(x, y, mqtt_client)


def back(mqtt_client):
    """make the robot go back to the origion"""
    items.move_to_destination(250, 250, mqtt_client)


def quit_program(mqtt_client):
    # this function send the "shutdown" message to the robot and disconnect
    # from mqtt
    mqtt_client.send_message('shutdown')
    if mqtt_client:
        mqtt_client.close()
    exit()


main()
