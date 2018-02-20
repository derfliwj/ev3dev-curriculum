"""
Song Trivia on the robot side!!!!
Author: Wes Derflinger
"""

import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time


class MyDelegate(object):

    def __init__(self):
        self.robot = robo.Snatch3r()
        self.mqtt_client = None
        self.running = True

    def loop_forever(self):
        """Allows the program to run forever!"""
        self.running = True
        while self.running:
            time.sleep(0.1)

    def shutdown(self):
        """Allows the program to shutdown after finishing!"""
        self.running = False

    def drive_to_color(self, color):
        """Uses robot controller to drive to the specific color then sends message of color to PC!"""
        self.robot.drive_to_color(color)
        if color == ev3.ColorSensor.COLOR_RED:
            color = "Red"
        elif color == ev3.ColorSensor.COLOR_BLUE:
            color = "Blue"
        elif color == ev3.ColorSensor.COLOR_BLACK:
            color = "Black"
        self.mqtt_client.send_message("get_color", [color])


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    my_delegate.mqtt_client = mqtt_client
    mqtt_client.connect_to_pc()
    my_delegate.loop_forever()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------


main()
