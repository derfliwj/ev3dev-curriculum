import ev3dev.ev3 as ev3
import robot_controller as robo
import mqtt_remote_method_calls as com
import math


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True
        self.robot_state = 0  # 0 is stop, 1 is looking for path, 2 is blocking
        self.destination_x = 250
        self.destination_y = 250
        self.angle = 0
        self.x = 250
        self.y = 250
        self.robot_state = 0

    def change_robot_state(self, number):
        self.robot_state = number


class MyDelegate(object):
    def robotconnection(self):
        ev3.Sound.speak("Robot Online")

    def moveto(self, data):
        dc.destination_x = data[0]
        dc.destination_y = data[1]
        dc.change_robot_state(1)
        # print(data)

    def shutdown(self):
        dc.running = False
        print('shutdown')


def robot_command(dc, robot, mqtt_client, command):
    angle = dc.angle
    if command == 'left':
        robot.drive_degree(4, 400)
        # the difference of turning degree is
        # caused by the frequently start and stop of the robot
        dc.angle = dc.angle + 5
    elif command == 'right':
        robot.drive_degree(-4, 400)
        # the difference of turning degree is
        # caused by the frequently start and stop of the robot
        dc.angle = dc.angle - 5
    elif command == 'forward':
        robot.drive_inches(2, 400)
        dc.x = dc.x + math.cos(angle * 3.14 / 180) * 10
        dc.y = dc.y + math.sin(angle * 3.14 / 180) * 10
        # print(dc.x, dc.y)
    message = [dc.x, dc.y]
    mqtt_client.send_message('move_robot', [message])


def obs_dectection(dc, robot, mqtt_client):
    if robot.ir_sensor.proximity < 50:
        message = [dc.x + math.cos(dc.angle * 3.14 / 180) * 50, dc.y +
                   math.sin(dc.angle * 3.14 / 180) * 50]
        mqtt_client.send_message('obstacle', [message])
        # avoid the obsticles by turn left 90 degree, forward 8 inch,
        # then right 90 degree
        for k in range(15):
            robot_command(dc, robot, mqtt_client, 'left')
        for k in range(4):
            robot_command(dc, robot, mqtt_client, 'forward')
        for k in range(15):
            robot_command(dc, robot, mqtt_client, 'right')
        obs_dectection(dc, robot, mqtt_client)


def check_emergency_stop(dc, robot, mqtt_client):
    if robot.touch_sensor.is_pressed:
        dc.robot_state = 0


def robot_run(robot, mqtt_client):
    while dc.running == True:
        # print(dc.robot_state)
        if dc.robot_state == 1:
            angle = dc.angle
            x = dc.x / 5
            y = dc.y / 5
            des_x = dc.destination_x / 5
            des_y = dc.destination_y / 5
            deltax = des_x - x
            deltay = des_y - y
            des_angle = math.atan2(deltay, deltax) * 360 / (2 * 3.14)
            # print(des_angle, angle)
            check_emergency_stop(dc, robot, mqtt_client)
            obs_dectection(dc, robot, mqtt_client)
            if abs(des_angle - angle) > 5:
                if des_angle > angle:
                    robot_command(dc, robot, mqtt_client, 'left')
                else:
                    robot_command(dc, robot, mqtt_client, 'right')
            else:
                distance = math.sqrt(deltax * deltax + deltay * deltay)
                # print(distance)
                # print(angle)
                if distance > 2:
                    robot_command(dc, robot, mqtt_client, 'forward')
                    # print(distance)
                else:
                    dc.change_robot_state(0)

    robot.stop()


print("--------------------------------------------")
print("Path finder")
print("--------------------------------------------")
print("Press the touch sensor profome emergency stop")

dc = DataContainer()
robot = robo.Snatch3r()
my_delegate = MyDelegate()
mqtt_client = com.MqttClient(my_delegate)
mqtt_client.connect_to_pc()

robot_run(robot, mqtt_client)
