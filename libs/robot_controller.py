"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):
        """construct a left motor and a right motor"""

        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_D)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor()
        self.color_sensor = ev3.ColorSensor()

        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected
        assert self.touch_sensor
        assert self.color_sensor

    def drive_inches(self, inch, speed):
        """Drives robot a distance at a given speed."""
        position = inch * 90
        self.left_motor.run_to_rel_pos(position_sp=position,
                                       speed_sp=speed)
        self.right_motor.run_to_rel_pos(position_sp=position,
                                        speed_sp=speed)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def drive_degree(self, degree, speed):
        """Turns Robot a distance at a given speed."""
        position = 2 * 3.14 * 3 * degree / 360
        position = position * 90
        if position > 0:
            self.left_motor.run_to_rel_pos(position_sp=-position,
                                           speed_sp=speed)
            self.right_motor.run_to_rel_pos(position_sp=position,
                                            speed_sp=speed)
            self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

        elif position < 0:
            position = 0 - position
            self.left_motor.run_to_rel_pos(position_sp=position,
                                           speed_sp=speed)
            self.right_motor.run_to_rel_pos(position_sp=-position,
                                            speed_sp=speed)
            self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def arm_calibration(self):
        """Calibrates the arm"""
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        ev3.Sound.beep().wait()
        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

        self.arm_motor.position = 0

    def arm_up(self):
        """Moves the Snatch3r arm to the up position."""
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        ev3.Sound.beep().wait()

    def arm_down(self):
        """Moves the Snatch3r arm to the down position."""
        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def loop_forever(self):
        """keeps snatch3r recieving mqtt messagess until shutdown is activated"""
        self.running = True
        while self.running:
            time.sleep(0.1)

    def shutdown(self):
        """shutdowns everything on ev3"""
        self.running = False
        ev3.Leds.all_off()
        self.left_motor.stop()
        self.right_motor.stop()

    def forward_button(self, left_speed, right_speed):
        """moves robot forward at set speeds"""
        self.left_motor.run_forever(speed_sp=int(left_speed))
        self.right_motor.run_forever(speed_sp=int(right_speed))

    def left_button(self, right_speed):
        """moves robot left at set speed"""
        self.right_motor.run_forever(speed_sp=int(right_speed))

    def stop_button(self):
        """stops robot"""
        print("real stop")
        self.left_motor.stop()
        self.right_motor.stop()


    def right_button(self, left_speed):
        """moves robot right at set speed"""
        self.left_motor.run_forever(speed_sp=int(left_speed))

    def reverse_button(self, left_speed, right_speed):
        """moves robot in reverse at set speed"""
        self.left_motor.run_forever(speed_sp=-int(left_speed))
        self.right_motor.run_forever(speed_sp=-int(right_speed))