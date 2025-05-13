#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

sensor_motor = Motor(Port.A)
colour_sensor = ColorSensor(Port.S3)
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
colour_sensor = ColorSensor(Port.S3)
ultrasonic_sensor = UltrasonicSensor(Port.S2)
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2
block_grabbed = False
detect_distance = 300 #150mm
check_block_distance = 80 #5mm



# FOLLOW KDOTFUNNIES ON TWITTER FOR MORE KDOT MEMES

"""Used to test the movement of the colour sensor's motor, using run_angle to move the motor at 
a speed of 90 degrees per second for 90 degrees, to stop the motor from hitting the ground or the wheels.
It then moves it back to it's previous posiiton and corrects the movements."""

#sensor_motor.run_angle(90, 90)
#sensor_motor.run_angle(90, -90)

"""Tests the colour sensor, to detect the two good blocks (red or yellow), making one beep
unrecognised blocks or undetect makes two beeps."""


#if colour_sensor.color() == Color.RED or Color.YELLOW:
    #pick up here
    ev3.speaker.beep()

#else:
    #move back here and turn 90 degrees
    ev3.speaker.beep()
    wait(2000)
    ev3.speaker.beep()
    ev3.speaker.beep()




# while ultrasonic_sensor > 30:
    robot.straight(20)
    robot.turn(30)
    if ultrasonic_sensor > 30:
        break
    robot.turn(-60)
    if ultrasonic_sensor > 30:
        break
    robot.turn(30)
    if ultrasonic_sensor > 30:
        break




while True:
    #finding block
    counter = 60
    found_block = False
    while found_block == False:
        while counter > 0:
           ev3.screen.print("Finding block")
           ev3.screen.print(counter)

           counter -= 1
           robot.turn(3)
           ev3.screen.clear()

           if ultrasonic_sensor.distance() < detect_distance:
               found_block = True
               ev3.screen.print("Block found")
               break
        ev3.straight(10)

    wait(30)

    #go to block
    while ultrasonic_sensor.distance() > check_block_distance:
        ev3.screen.print("Going to block")
        ev3.screen.print(ultrasonic_sensor.distance())
        robot.straight(2.5) #move forward 2.5mm
        ev3.screen.clear()
    
    wait(30)

    #check block colour
    while True:
        sensor_motor.run_angle (90,-90)
        current_color = colour_sensor.color()

        wait(5)

        if current_color == Color.RED or Color.YELLOW:
            block_grabbed = True
            wait(30)
            ev3.straight(2.5)
            sensor_motor.run_angle (90,90)
            break
        else:
            ev3.screen.print("Bad block found")
            ev3.screen.print(current_color)
            ev3.screen.clear()
            ev3.straight(-10)
            ev3.turn(-90)
            ev3.straight(10)
            ev3.turn(90)
            ev3.straight(20)
            ev3.turn(10)
            ev3.straight(10)
            ev3.turn(-90)
            sensor_motor.run_angle (90,90)
            break

    if block_grabbed == True:
        while colour_sensor.color() == Color.WHITE:
            robot.straight(2.5)
    
    deviation = colour_sensor.reflection() - threshold
    turn_rate = 1.2 * deviation
    robot.drive(100, turn_rate)
    wait(10)


#end
ev3.screen.print("Finished")
