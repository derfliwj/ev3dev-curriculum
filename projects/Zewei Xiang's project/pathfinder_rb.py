import ev3dev.ev3 as ev3
import robot_controller as robo
import mqtt_remote_method_calls as com
import math
import time


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
        print(data)

    def shutdown(self):
        DataContainer.running = False


def robot_run(robot, mqtt_client):
    while dc.running:
        # print(dc.robot_state)
        if dc.robot_state == 1:
            angle = dc.angle
            x = dc.x / 10
            y = dc.y / 10
            des_x = dc.destination_x / 10
            des_y = dc.destination_y / 10
            deltax = des_x - x
            deltay = des_y - y
            des_angle = math.atan2(deltay, deltax) * 360 / (2 * 3.14)
            print(des_angle, angle)
            if abs(des_angle - angle) > 5:
                if des_angle > angle:
                    robot.drive_degree(+5, 400)
                    dc.angle = dc.angle + 5
                else:
                    robot.drive_degree(-5, 400)
                    dc.angle = dc.angle - 5
            else:
                distance = math.sqrt(deltax * deltax + deltay * deltay)
                print(distance)
                print(angle)
                if distance > 2:
                    robot.drive_inches(2, 400)
                    dc.x = dc.x + math.cos(angle * 3.14 / 180) * 20
                    dc.y = dc.y + math.sin(angle * 3.14 / 180) * 20
                    print(dc.x, dc.y, distance)
                else:
                    dc.change_robot_state(0)
            message = [dc.x, dc.y]
            mqtt_client.send_message('move_robot', [message])
    robot.stop()


print("--------------------------------------------")
print(" Beep at hands")
print("--------------------------------------------")
print("Press the touch sensor to exit this program.")

dc = DataContainer()
robot = robo.Snatch3r()
my_delegate = MyDelegate()
mqtt_client = com.MqttClient(my_delegate)
mqtt_client.connect_to_pc()

print('init finish')
robot_run(robot, mqtt_client)
