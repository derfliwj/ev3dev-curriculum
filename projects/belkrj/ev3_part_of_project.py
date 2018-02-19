"""EV3 Part of Project"""

import robot_controller as robo
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import time


def main():
    print('Waiting for orders.')
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)

    ev3_delegate = Ev3Delegate()
    mqqt_client_op = com.MqttClient(ev3_delegate)
    ev3_delegate.mqtt_client1 = mqqt_client_op
    mqqt_client_op.connect_to_pc(lego_robot_number=22)
    ev3_delegate.loop_forever()


def restart():
    main()


class Ev3Delegate(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.running = True
        self.mqtt_client_op = None

    def op_unthinkable(self):

        control_delegate = ControlDelegate()
        mqtt_client2 = com.MqttClient(control_delegate)
        control_delegate.mqtt_client2 = mqtt_client2
        control_delegate.mqtt_client2.connect_to_pc(lego_robot_number=97)

        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        color_sensor = ev3.ColorSensor()
        touch_sensor = ev3.TouchSensor()

        while not touch_sensor.is_pressed:
            if color_sensor.color == ev3.ColorSensor.COLOR_RED:
                self.robot.shutdown()
                ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
                ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
                ev3.Sound.speak('Mission Failure').wait()
                control_delegate.mqtt_client2.send_message('unthinkable_failure')
                restart()
                break

            elif color_sensor.color == ev3.ColorSensor.COLOR_GREEN:
                ev3.Sound.speak('Object found.').wait()

            elif color_sensor.color == ev3.ColorSensor.COLOR_BLUE:
                ev3.Sound.speak('Drop off location found.').wait()

            elif color_sensor.color == ev3.ColorSensor.COLOR_BLACK:
                mqtt_client2.send_message('unthinkable_passed')

        restart()
        control_delegate.loop_forever()

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)


class ControlDelegate(object):
    def __init__(self):
        self.robot = robo.Snatch3r()
        self.running = True
        self.mqtt_client2 = None

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

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)


main()
