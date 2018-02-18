"""EV3 Part of Project"""

import robot_controller as robo
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import time


def main():
    print('Hello')
    ev3.Sound.speak('Hello').wait()
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)

    ev3_delegate = Ev3Delegate()
    mqqt_client = com.MqttClient(ev3_delegate)
    ev3_delegate.mqtt_client = mqqt_client
    mqqt_client.connect_to_pc()
    ev3_delegate.loop_forever()


class Ev3Delegate(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.mqtt_client = None

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

    def op_unthinkable(self):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        if self.robot.color_sensor.color == self.robot.color_sensor.COLOR_RED:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
            self.robot.stop_button()
            ev3.Sound.speak('Mission Failure').wait()
            self.mqtt_client.send_message('unthinkable_failure')

        elif self.robot.color_sensor.color == self.robot.color_sensor.COLOR_GREEN:
            ev3.Sound.speak('Object found.')

        elif self.robot.color_sensor.color == self.robot.color_sensor.COLOR_BLUE:
            ev3.Sound.speak('Drop off location found.')

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)


main()