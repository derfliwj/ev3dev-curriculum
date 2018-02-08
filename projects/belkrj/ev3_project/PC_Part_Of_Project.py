"""Bobby Belks Project PC Part"""
import time

import math

import mqtt_remote_method_calls as com

import tkinter
from tkinter import ttk

import robot_controller as robo


def main():
    start_root = tkinter.Tk()
    start_root.title('The Cold War Simulation')

    main_frame = ttk.Frame(start_root, padding=20)
    main_frame.grid()

    intro_label = ttk.Label(main_frame, text='The year in 1945.')
    intro_label.grid()

    intro_label_detail_l1 = ttk.Label(main_frame, text='The war to end all wars has just ended.')
    intro_label_detail_l1.grid()

    intro_label_detail_l2 = ttk.Label(main_frame, text='However a more devious war is upon the world.')
    intro_label_detail_l2.grid()

    intro_label_detail_l3 = ttk.Label(main_frame, text='The war would be known as The Cold War')
    intro_label_detail_l3.grid()

    intro_label_detail_l4 = ttk.Label(main_frame, text='You will assume the role as a lead on 3 operations that occured.')
    intro_label_detail_l4.grid()

    intro_label_detail_l5 = ttk.Label(main_frame, text='Complete all 3 without failure.')
    intro_label_detail_l5.grid()


    begin_btn = ttk.Button(main_frame, text='Shall we begin?')
    begin_btn.grid()

    begin_btn['command'] = lambda: background()

    start_root.mainloop()


def background():

    background_root = tkinter.Tk()
    background_root.title('Choose your mission.')

    background_frame = ttk.Frame(background_root, padding=100)
    background_frame.grid()

    background_info = ttk.Label(background_frame, text='Operations:', relief='raised')
    background_info.grid(row=0, column=0)

    operation_kitty_btn = ttk.Button(background_frame, text='Operation Kitty')
    operation_kitty_btn.grid(row=2, column=0)
    operation_kitty_btn['command'] = lambda: details_operation_kitty()

    operation_unthinkable_btn = ttk.Button(background_frame, text='Operation Unthinkable')
    operation_unthinkable_btn.grid(row=1, column=0)
    operation_unthinkable_btn['command'] = lambda: details_operation_unthinkable()

    operation_savior_btn = ttk.Button(background_frame, text='Operation Savior')
    operation_savior_btn.grid(row=3, column=0)
    operation_savior_btn['command'] = lambda: details_operation_savior()

    background_root.mainloop()


def details_operation_kitty():

    kitty_root = tkinter.Tk()
    kitty_root.title('Operation Kitty:')

    kitty_frame = ttk.Frame(kitty_root, padding=100)
    kitty_frame.grid()

    kitty_label = ttk.Label(kitty_frame, text='Details:', relief='raised')
    kitty_label.grid(row=0, column=0)

    kitty_detail_label_l1 = ttk.Label(kitty_frame, text='The year is 1961.')
    kitty_detail_label_l2 = ttk.Label(kitty_frame, text='Operation Kitty has gotten the green light.')
    kitty_detail_label_l3 = ttk.Label(kitty_frame, text='The mission is...')
    kitty_detail_label_l4 = ttk.Label(kitty_frame, text='Locate Communists in Washington D.C.')
    kitty_detail_label_l5 = ttk.Label(kitty_frame, text='Simple enough.')
    kitty_detail_label_l6 = ttk.Label(kitty_frame, text='However, you are a cat.')
    kitty_detail_label_l7 = ttk.Label(kitty_frame, text='You have been assembled into a cyborg cat.')
    kitty_detail_label_l8 = ttk.Label(kitty_frame, text='Years of training and surgeries.')
    kitty_detail_label_l9 = ttk.Label(kitty_frame, text='Your tail is now a transmitter.')
    kitty_detail_label_l10 = ttk.Label(kitty_frame, text='Listening devices have been implanted in your ears.')
    kitty_detail_label_l11 = ttk.Label(kitty_frame, text='Cameras for your eyes.')
    kitty_detail_label_l12 = ttk.Label(kitty_frame, text='Cost over 15 million dollars for this mission.')
    kitty_detail_label_l13 = ttk.Label(kitty_frame, text='Do you accept?')

    kitty_detail_label_l1.grid()
    kitty_detail_label_l2.grid()
    kitty_detail_label_l3.grid()
    kitty_detail_label_l4.grid()
    kitty_detail_label_l5.grid()
    kitty_detail_label_l6.grid()
    kitty_detail_label_l7.grid()
    kitty_detail_label_l8.grid()
    kitty_detail_label_l9.grid()
    kitty_detail_label_l10.grid()
    kitty_detail_label_l11.grid()
    kitty_detail_label_l12.grid()
    kitty_detail_label_l13.grid()

    kitty_accept_btn = ttk.Button(kitty_frame, text='I accept.')
    kitty_accept_btn.grid()

    kitty_accept_btn['command'] = lambda: kitty_accepted()
    time.sleep(.1)

    kitty_root.mainloop()


def kitty_accepted():

    kitty_on_mission_root = tkinter.Tk()
    kitty_on_mission_root.title('Operation Kitty: Mission Time')

    kitty_on_mission_frame = ttk.Frame(kitty_on_mission_root, padding=100)
    kitty_on_mission_frame.grid()

    control_button_access = ttk.Button(kitty_on_mission_frame, text='Click here to access controls.')
    control_button_access.grid()

    kitty_objectives = ttk.Label(kitty_on_mission_frame, text='Objectives:', relief='raised')
    kitty_objectives.grid()

    kitty_objectives_l1 = ttk.Label(kitty_on_mission_frame, text='Find enemies and escort them to jail.')
    kitty_objectives_l1.grid()

    kitty_on_mission_intel_l1 = ttk.Label(kitty_on_mission_frame, text='Intel coming in.', relief='raised')
    kitty_on_mission_intel_l1.grid()

    kitty_on_mission_intel_l2 = ttk.Label(kitty_on_mission_frame, text='1.We know of 3 enemies.')
    kitty_on_mission_intel_l3 = ttk.Label(kitty_on_mission_frame, text='2.Your special fitted cameras should tell once a possible target is insight.')
    kitty_on_mission_intel_l4 = ttk.Label(kitty_on_mission_frame, text='3.Some are using disguises!')
    kitty_on_mission_intel_l2.grid()
    kitty_on_mission_intel_l3.grid()
    kitty_on_mission_intel_l4.grid()

    control_button_access['command'] = lambda: mission_accepted_robot_controller()

    kitty_on_mission_root.mainloop()


def mission_accepted_robot_controller():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    controller_root = tkinter.Tk()
    controller_root.title('Mission Control')

    main_frame = ttk.Frame(controller_root, padding=25, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: press_forward_button(mqtt_client, left_speed_entry.get(),
                                                             right_speed_entry.get())
    controller_root.bind('<Up>', lambda event: press_forward_button(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: press_left_button(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    controller_root.bind('<Left>', lambda event: press_left_button(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: press_stop_button(mqtt_client)
    controller_root.bind('<space>', lambda event: press_stop_button(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: press_right_button(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    controller_root.bind('<Right>', lambda event: press_right_button(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: press_back_button(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    controller_root.bind('<Down>', lambda event: press_back_button(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    controller_root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    controller_root.bind('<j>', lambda event: send_down(mqtt_client))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    controller_root.mainloop()


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


def details_operation_unthinkable():

    unthinkable_root = tkinter.Tk()
    unthinkable_root.title('Operation Unthinkable:')

    unthinkable_frame = ttk.Frame(unthinkable_root, padding=100)
    unthinkable_frame.grid()

    unthinkable_label = ttk.Label(unthinkable_frame, text='Details:')
    unthinkable_label.grid()

    unthinkable_detials_label_l1 = ttk.Label(unthinkable_frame, text='The year is 1945.')
    unthinkable_detials_label_l2 = ttk.Label(unthinkable_frame, text='You are designated by Winston Churchhill to join BAFJP.')
    unthinkable_detials_label_l3 = ttk.Label(unthinkable_frame, text='British Armed Forces Joint Planning.')
    unthinkable_detials_label_l4 = ttk.Label(unthinkable_frame, text='Your mission from BAFJP.')
    unthinkable_detials_label_l5 = ttk.Label(unthinkable_frame, text='Elaborate and execute a plan to pit the U.S. and USSR against eachother.')
    unthinkable_detials_label_l6 = ttk.Label(unthinkable_frame, text='Do you accept?')

    unthinkable_detials_label_l1.grid(row=1, column=0)
    unthinkable_detials_label_l2.grid()
    unthinkable_detials_label_l3.grid()
    unthinkable_detials_label_l4.grid()
    unthinkable_detials_label_l5.grid()
    unthinkable_detials_label_l6.grid()

    unthinkable_accept_btn = ttk.Button(unthinkable_frame, text='I accept.')
    unthinkable_accept_btn.grid()

    unthinkable_accept_btn['command'] = lambda: unthinkable_accepted()

    unthinkable_root.mainloop()

def unthinkable_accepted():
    unthinkable_on_mission_root = tkinter.Tk()
    unthinkable_on_mission_root.title('Operation Unthinkable: Mission Time')

    unthinkable_on_mission_frame = ttk.Frame(unthinkable_on_mission_root, padding=100)
    unthinkable_on_mission_frame.grid()

    control_button_access = ttk.Button(unthinkable_on_mission_frame, text='Click here to access controls.')
    control_button_access.grid()

    unthinkable_objectives = ttk.Label(unthinkable_on_mission_frame, text='Objectives:', relief='raised')
    unthinkable_objectives.grid()

    unthinkable_objectives_l1 = ttk.Label(unthinkable_on_mission_frame, text='Plant the evidence to create distrust between U.S. officials and USSR officials.')
    unthinkable_objectives_l1.grid()

    unthinkable_on_mission_intel_l1 = ttk.Label(unthinkable_on_mission_frame, text='Intel coming in.', relief='raised')
    unthinkable_on_mission_intel_l1.grid()

    unthinkable_on_mission_intel_l2 = ttk.Label(unthinkable_on_mission_frame, text='1.We know of 3 items to steal.')
    unthinkable_on_mission_intel_l3 = ttk.Label(unthinkable_on_mission_frame,
                                          text='2.We know where to plant them.')
    unthinkable_on_mission_intel_l4 = ttk.Label(unthinkable_on_mission_frame, text='3.Do not get caught.')
    unthinkable_on_mission_intel_l2.grid()
    unthinkable_on_mission_intel_l3.grid()
    unthinkable_on_mission_intel_l4.grid()

    control_button_access['command'] = lambda: mission_accepted_robot_controller()

    unthinkable_on_mission_frame.mainloop()


def details_operation_savior():
    savior_root = tkinter.Tk()
    savior_root.title('Operation Savior:')

    savior_frame = ttk.Frame(savior_root, padding=100)
    savior_frame.grid()

    savior_label = ttk.Label(savior_frame, text='Details:')
    savior_label.grid()

    savior_details_label_l1 = ttk.Label(savior_frame, text='The year is 1973.')
    savior_details_label_l2 = ttk.Label(savior_frame, text='The Cold War is in full swing.')
    savior_details_label_l3 = ttk.Label(savior_frame, text='The U.S. CIA has some hard intel of a devious plot.')
    savior_details_label_l4 = ttk.Label(savior_frame, text='USSR is close to developing a mindcontrol device.')
    savior_details_label_l5 = ttk.Label(savior_frame, text='This is extremely hazardous ')
    savior_details_label_l6 = ttk.Label(savior_frame, text='This could change everything.')
    savior_details_label_l7 = ttk.Label(savior_frame, text='The U.S. and all of the public is in considerable danger.')
    savior_details_label_l8 = ttk.Label(savior_frame, text='They plan to move the device to a nearby facility.')
    savior_details_label_l9 = ttk.Label(savior_frame, text='This is where you come in.')
    savior_details_label_l10 = ttk.Label(savior_frame, text='It will not be easy.')
    savior_details_label_l11 = ttk.Label(savior_frame, text='The world is at stake.')
    savior_details_label_l12 = ttk.Label(savior_frame, text='Do you accept?')

    savior_details_label_l1.grid()
    savior_details_label_l2.grid()
    savior_details_label_l3.grid()
    savior_details_label_l4.grid()
    savior_details_label_l5.grid()
    savior_details_label_l6.grid()
    savior_details_label_l7.grid()
    savior_details_label_l8.grid()
    savior_details_label_l9.grid()
    savior_details_label_l10.grid()
    savior_details_label_l11.grid()
    savior_details_label_l12.grid()

    savior_accept_btn = ttk.Button(savior_frame, text='I accept.')
    savior_accept_btn.grid()

    savior_accept_btn['command'] = lambda: savior_accepted()

    savior_root.mainloop()


def savior_accepted():
    savior_on_mission_root = tkinter.Tk()
    savior_on_mission_root.title('Operation Savior: Mission Time')

    savior_on_mission_frame = ttk.Frame(savior_on_mission_root, padding=100)
    savior_on_mission_frame.grid()

    control_button_access = ttk.Button(savior_on_mission_frame, text='Click here to access controls.')
    control_button_access.grid()

    savior_objectives = ttk.Label(savior_on_mission_frame, text='Objectives:', relief='raised')
    savior_objectives.grid()

    savior_objectives_l1 = ttk.Label(savior_on_mission_frame,
                                          text='Steal mind control device.')
    savior_objectives_l1.grid()

    savior_on_mission_intel_l1 = ttk.Label(savior_on_mission_frame, text='Intel coming in.', relief='raised')
    savior_on_mission_intel_l1.grid()

    savior_on_mission_intel_l2 = ttk.Label(savior_on_mission_frame, text='1.Many numerous guards around.')
    savior_on_mission_intel_l3 = ttk.Label(savior_on_mission_frame,
                                                text='2.We found out they have 3 in total.')
    savior_on_mission_intel_l4 = ttk.Label(savior_on_mission_frame, text='3.Being caught is failure.')

    savior_on_mission_intel_l2.grid()
    savior_on_mission_intel_l3.grid()
    savior_on_mission_intel_l4.grid()

    control_button_access['command'] = lambda: mission_accepted_robot_controller()

    savior_on_mission_root.mainloop()

main()