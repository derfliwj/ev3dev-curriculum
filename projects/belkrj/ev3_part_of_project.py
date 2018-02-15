"""EV3 Part of Project"""

import robot_controller as robo
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


class Ev3Delegate(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.mqtt_client = com.MqttClient(Ev3Delegate)

    def forward_button(self, left, right):
        self.robot.forward_button(left, right)

    def left_button(self, left, right):
        self.robot.left_button(left, right)

    def stop_button(self):
        self.robot.stop_button()

    def right_button(self, left, right):
        self.robot.right_button(left, right)

    def reverse_button(self, left, right):
        self.robot.reverse_button(left, right)

    def arm_up(self):
        self.robot.arm_up()

    def arm_down(self):
        self.robot.arm_down()

    def shutdown(self):
        self.robot.shutdown()

    def operation_unthinkable(self, count):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        ev3.Sound.speak('Green light on operation unthinkable').wait()

        if self.robot.color_sensor.color is self.robot.color_sensor.COLOR_RED:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
            ev3.Sound.speak('Mission Failure').wait()
            self.mqtt_client.send_message('unthinkable_failure')

        if self.robot.color_sensor.color is self.robot.color_sensor.COLOR_GREEN:
            ev3.Sound.speak('Object found.')

        if self.robot.color_sensor.color is self.robot.color_sensor.COLOR_BLUE:
            ev3.Sound.speak('Drop off location found.')
            count = count + 1

        if count == 3:
            self.mqtt_client.send_message('unthinkable_passed')



