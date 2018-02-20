"""
Author: Wes Derflinger
"""

import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3


class MyDelegate(object):

    def __init__(self):
        self.robot = robo.Snatch3r()
        self.mqtt_client = None

    def loop_forever_1(self):
        self.robot.loop_forever()

    def drive_to_color(self, color):
        self.robot.drive_to_color(color)
        if color == ev3.ColorSensor.COLOR_RED:
            color = "Red"
        elif color == ev3.ColorSensor.COLOR_BLUE:
            color = "Blue"
        elif color == ev3.ColorSensor.COLOR_GREEN:
            color = "Green"
        self.mqtt_client.send_message("get_color", [color])


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    my_delegate.mqtt_client = mqtt_client

    mqtt_client.connect_to_pc()

    my_delegate.loop_forever_1()
