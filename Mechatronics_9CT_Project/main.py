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

"""Used to test the movement of the colour sensor's motor, using run_angle to move the motor at 
a speed of 90 degrees per second for 90 degrees, to stop the motor from hitting the ground or the wheels.
It then moves it back to it's previous posiiton and corrects the movements."""

sensor_motor.run_angle(90, -90)
sensor_motor.run_angle(90, 90)

"""Tests the colour sensor, to detect the two good blocks (red or yellow), making one beep
unrecognised blocks or undetect makes two beeps."""


if colour_sensor.color() == Color.RED or Color.YELLOW:
    #pick up here
    ev3.speaker.beep()

else:
    #move back here and turn 90 degrees
    speaker.beep()
    speaker.beep()