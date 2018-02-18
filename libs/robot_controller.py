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
import math


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):
        """construct a left motor and a right motor"""

        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_D)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor()
        self.color_sensor = ev3.ColorSensor()
        self.ir_sensor = ev3.InfraredSensor()
        self.pixy = ev3.Sensor(driver_name="pixy-lego")

        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected
        assert self.touch_sensor
        assert self.color_sensor
        assert self.ir_sensor
        assert self.pixy

    def drive_inches(self, inch, speed):
        """Drives robot a distance at a given speed."""
        position = inch * 90
        self.left_motor.run_to_rel_pos(position_sp=position,
                                       speed_sp=speed)
        self.right_motor.run_to_rel_pos(position_sp=position,
                                        speed_sp=speed)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def drive_forward(self, left_speed, right_speed):
        """Drives forward continuously at a given speed"""
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def turn_left(self, speed):
        self.left_motor.run_forever(speed_sp=-speed)
        self.right_motor.run_forever(speed_sp=speed)

    def turn_right(self, speed):
        self.left_motor.run_forever(speed_sp=speed)
        self.right_motor.run_forever(speed_sp=-speed)

    def stop(self):
        """Stops robot"""
        self.right_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.left_motor.stop(stop_action=ev3.Motor.STOP_ACTION_BRAKE)

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

    def left_button(self, left_speed, right_speed):
        """moves robot left at set speed"""
        self.right_motor.run_forever(speed_sp=int(right_speed))

    def stop_button(self):
        """stops robot"""
        self.left_motor.stop()
        self.right_motor.stop()

    def right_button(self, left_speed, right_speed):
        """moves robot right at set speed"""
        self.left_motor.run_forever(speed_sp=int(left_speed))

    def reverse_button(self, left_speed, right_speed):
        """moves robot in reverse at set speed"""
        self.left_motor.run_forever(speed_sp=-int(left_speed))
        self.right_motor.run_forever(speed_sp=-int(right_speed))

    def seek_beacon(self):
        """Finds and stops in front of beacon."""
        beacon_seeker = ev3.BeaconSeeker(channel=2)
        assert beacon_seeker
        forward_speed = 200
        turn_speed = 100

        while not self.touch_sensor.is_pressed:
            current_heading = beacon_seeker.heading
            current_distance = beacon_seeker.distance
            if current_distance == -128:
                print("IR Remote not found. Distance is -128")
                self.drive_forward(turn_speed, -turn_speed)
            else:
                if math.fabs(beacon_seeker.heading) < 2:
                    print("On the right heading. Distance: ", current_distance)
                    if beacon_seeker.distance == 1:
                        self.drive_inches(4, turn_speed)
                        self.stop()
                        return True
                    else:
                        self.drive_forward(forward_speed, forward_speed)
                if (math.fabs(beacon_seeker.heading) > 2) & (math.fabs(beacon_seeker.heading) < 10):
                    if beacon_seeker.heading < 0:
                        print("Adjusting heading: ", current_heading)
                        self.drive_forward(-turn_speed, turn_speed)
                    elif beacon_seeker.heading > 0:
                        print("Adjusting heading: ", current_heading)
                        self.drive_forward(turn_speed, -turn_speed)
                if math.fabs(beacon_seeker.heading) > 10:
                    self.drive_forward(turn_speed, -turn_speed)
                    print("Heading is too far off to fix: ", current_heading)
            time.sleep(0.2)
        print("Abandon ship!")
        self.stop()
        return False
