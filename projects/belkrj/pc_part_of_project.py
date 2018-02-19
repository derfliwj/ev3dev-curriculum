"""PC part of project"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import time
import os


def starting():

    starting_root = tkinter.Tk()
    starting_root.title('Cold War')

    starting_frame = ttk.Frame(starting_root, padding=10)
    starting_frame.grid()

    starting_title_label = ttk.Label(starting_frame, text='Cold War', relief='raised')
    starting_title_label.grid()

    starting_explian_label_l1 = ttk.Label(starting_frame, text='Hello Soldier.')
    starting_explian_label_l2 = ttk.Label(starting_frame, text='You will be doing a few undercover operations.')
    starting_explian_label_l3 = ttk.Label(starting_frame, text='Press the button to select an operation.')

    starting_explian_label_l1.grid()
    starting_explian_label_l2.grid()
    starting_explian_label_l3.grid()

    starting_continue_to_op_btn = ttk.Button(starting_frame, text='Continue')

    starting_continue_to_op_btn.grid()

    starting_continue_to_op_btn['command'] = lambda: operations_screen(starting_root)

    starting_music_btn = ttk.Button(starting_frame, text='Music')
    starting_music_btn.grid()

    starting_music_btn['command'] = lambda: os.system("start C:\g_eazy.wav")

    starting_root.mainloop()


def operations_screen(previous_screen_root):

    destroy_window(previous_screen_root)

    operations_screen_root = tkinter.Tk()
    operations_screen_root.title('Operations Screen')

    operations_screen_frame = ttk.Frame(operations_screen_root, padding=100)
    operations_screen_frame.grid()

    operations_screen_title_label = ttk.Label(operations_screen_frame, text='Operations:', relief='raised')
    operations_screen_title_label.grid()

    operations_screen_unthinkable_btn = ttk.Button(operations_screen_frame, text='Operation Unthinkable')
    operations_screen_unthinkable_btn.grid()

    operations_screen_unthinkable_btn['command'] = lambda: operation_unthinkable(operations_screen_root)

    operations_screen_root.mainloop()


def operation_unthinkable(previous_screen_root):

    destroy_window(previous_screen_root)

    unthinkable_root = tkinter.Tk()
    unthinkable_root.title('Operation: Unthinkable')

    unthinkable_frame = ttk.Frame(unthinkable_root, padding=10)
    unthinkable_frame.grid()

    unthinkable_title_label = ttk.Label(unthinkable_frame, text='Operation: Unthinkable', relief='raised')
    unthinkable_title_label.grid()

    unthinkable_detail_label_l1 = ttk.Label(unthinkable_frame, text='The year is 1945.')
    unthinkable_detail_label_l2 = ttk.Label(unthinkable_frame, text='The second great war has just ended.')
    unthinkable_detail_label_l3 = ttk.Label(unthinkable_frame, text='You have direct orders from Winston Churchill.')
    unthinkable_detail_label_l4 = ttk.Label(unthinkable_frame, text='He instructs you to...')
    unthinkable_detail_label_l5 = ttk.Label(unthinkable_frame, text='Pit U.S. and U.S.S.R. officials against each other'
                                                                    'by planting stolen items.')
    unthinkable_detail_label_l6 = ttk.Label(unthinkable_frame, text='Do you accept?')

    unthinkable_detail_label_l1.grid()
    unthinkable_detail_label_l2.grid()
    unthinkable_detail_label_l3.grid()
    unthinkable_detail_label_l4.grid()
    unthinkable_detail_label_l5.grid()
    unthinkable_detail_label_l6.grid()

    unthinkable_mission_accept_btn = ttk.Button(unthinkable_frame, text='I accept.')
    unthinkable_mission_accept_btn.grid()

    unthinkable_mission_accept_btn['command'] = lambda: unthinkable_accepted(unthinkable_root)

    unthinkable_root.mainloop()


def unthinkable_accepted(previous_screen_root):

    destroy_window(previous_screen_root)

    unthinkable_accepted_root = tkinter.Tk()
    unthinkable_accepted_root.title('Mission Time: Operation Unthinkable.')

    unthinkable_accepted_frame = ttk.Frame(unthinkable_accepted_root, padding=20)
    unthinkable_accepted_frame.grid()

    unthinkable_accepted_title_label = ttk.Label(unthinkable_accepted_frame, text='Operation Unthinkable:', relief='rai'
                                                                                                                   'se'
                                                                                                                   'd')

    unthinkable_accepted_title_label.grid()

    unthinkable_accepted_intel_title = ttk.Label(unthinkable_accepted_frame, text='Intel Incoming:')
    unthinkable_accepted_intel_title.grid()

    unthinkable_accepted_intel_l1 = ttk.Label(unthinkable_accepted_frame, text='Three items.')
    unthinkable_accepted_intel_l2 = ttk.Label(unthinkable_accepted_frame, text='Ten bad guys.')
    unthinkable_accepted_intel_l3 = ttk.Label(unthinkable_accepted_frame, text='Being caught means failure.')

    unthinkable_accepted_intel_l1.grid()
    unthinkable_accepted_intel_l2.grid()
    unthinkable_accepted_intel_l3.grid()

    unthinkable_accepted_begin_btn = ttk.Button(unthinkable_accepted_frame, text='Begin.')
    unthinkable_accepted_begin_btn.grid()

    unthinkable_accepted_begin_btn['command'] = lambda: unthinkable_begin()

    unthinkable_controls_btn = ttk.Button(unthinkable_accepted_frame, text='Controls')
    unthinkable_controls_btn.grid()

    unthinkable_controls_btn['command'] = lambda : robot_controls()

    unthinkable_accepted_root.mainloop()


def unthinkable_begin():
    pc_delegate = PcDelegate()
    mqtt_client = com.MqttClient(pc_delegate)
    mqtt_client.connect_to_ev3(lego_robot_number=22)
    mqtt_client.send_message('op_unthinkable')


def robot_controls():
    pc_delegate = PcDelegate()
    mqtt_client2 = com.MqttClient(pc_delegate)
    pc_delegate.mqtt_client2 = mqtt_client2
    mqtt_client2.connect_to_ev3(lego_robot_number=97)

    robot_control_root = tkinter.Tk()
    robot_control_root.title('Robot Control')

    main_frame = ttk.Frame(robot_control_root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "200")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "200")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: press_forward_button(mqtt_client2, left_speed_entry.get(),
                                                             right_speed_entry.get())
    robot_control_root.bind('<Up>', lambda event: press_forward_button(mqtt_client2, left_speed_entry.get(),
                                                                       right_speed_entry.get()))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: press_left_button(mqtt_client2, left_speed_entry.get(), right_speed_entry.get())
    robot_control_root.bind('<Left>', lambda event: press_left_button(mqtt_client2, left_speed_entry.get(),
                                                                      right_speed_entry.get()))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: press_stop_button(mqtt_client2)
    robot_control_root.bind('<space>', lambda event: press_stop_button(mqtt_client2))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: press_right_button(mqtt_client2, left_speed_entry.get(), right_speed_entry.get())
    robot_control_root.bind('<Right>', lambda event: press_right_button(mqtt_client2, left_speed_entry.get(),
                                                                        right_speed_entry.get()))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: press_back_button(mqtt_client2, left_speed_entry.get(), right_speed_entry.get())
    robot_control_root.bind('<Down>', lambda event: press_back_button(mqtt_client2, left_speed_entry.get(),
                                                                      right_speed_entry.get()))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client2)
    robot_control_root.bind('<u>', lambda event: send_up(mqtt_client2))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client2)
    robot_control_root.bind('<j>', lambda event: send_down(mqtt_client2))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client2, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client2, True))

    robot_control_root.mainloop()
    pc_delegate.loop_forever()


def press_forward_button(mqtt_client, left_speed, right_speed):
    print('Forward button pressed.')
    mqtt_client.send_message("forward_button", [left_speed, right_speed])


def press_left_button(mqtt_client, left_speed, right_speed):
    print('Left button pressed.')
    mqtt_client.send_message("left_button", [left_speed, right_speed])


def press_stop_button(mqtt_client):
    print('Stop button pressed.')
    mqtt_client.send_message("stop_button")


def press_right_button(mqtt_client, left_speed, right_speed):
    print('Right button pressed.')
    mqtt_client.send_message("right_button", [left_speed, right_speed])


def press_back_button(mqtt_client, left_speed, right_speed):
    print('Back button pressed')
    mqtt_client.send_message("reverse_button", [left_speed, right_speed])


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


class PcDelegate(object):
    def __init__(self):
        self.running = True

    def unthinkable_failure(self):
        unthinkable_failure_root = tkinter.Tk()
        unthinkable_failure_root.title('Failure')

        unthinkable_failure_frame = ttk.Frame(unthinkable_failure_root, padding=100)
        unthinkable_failure_frame.grid()

        unthinkable_failure_title_label = ttk.Label(unthinkable_failure_frame, text='Mission Failed!', relief='raised')
        unthinkable_failure_title_label.grid()

        unthinkable_failure_text_label_l1 = ttk.Label(unthinkable_failure_frame, text='You have been caught!')
        unthinkable_failure_text_label_l2 = ttk.Label(unthinkable_failure_frame, text='Better luck next time.')
        unthinkable_failure_text_label_l3 = ttk.Label(unthinkable_failure_frame, text='Click the button below to return'
                                                                                              ' to operations.')

        unthinkable_failure_text_label_l1.grid()
        unthinkable_failure_text_label_l2.grid()
        unthinkable_failure_text_label_l3.grid()

        unthinkable_failure_return_btn = ttk.Button(unthinkable_failure_frame, text='Return to homebase.')
        unthinkable_failure_return_btn.grid()

        unthinkable_failure_return_btn['command'] = lambda: starting()

        unthinkable_failure_root.mainloop()

    def unthinkable_passed(self):
        unthinkable_passed_root = tkinter.Tk()
        unthinkable_passed_root.title('Operation Passed!')

        unthinkable_passed_frame = ttk.Frame(unthinkable_passed_root, padding=100)
        unthinkable_passed_frame.grid()

        unthinkable_passed_title_label = ttk.Label(unthinkable_passed_frame, text='Mission Passed!', relief='raised')
        unthinkable_passed_title_label.grid()

        unthinkable_passed_text_label_l1 = ttk.Label(unthinkable_passed_frame, text='You completed the mission!')
        unthinkable_passed_text_label_l2 = ttk.Label(unthinkable_passed_frame, text='Good job!.')
        unthinkable_passed_text_label_l3 = ttk.Label(unthinkable_passed_frame,
                                                      text='Click the button below to return to operations.')

        unthinkable_passed_text_label_l1.grid()
        unthinkable_passed_text_label_l2.grid()
        unthinkable_passed_text_label_l3.grid()

        unthinkable_passed_return_btn = ttk.Button(unthinkable_passed_frame, text='Return to homebase.')
        unthinkable_passed_return_btn.grid()

        unthinkable_passed_return_btn['command'] = lambda: starting()

        unthinkable_passed_frame.mainloop()

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)


def destroy_window(root):
    root.destroy()


starting()
