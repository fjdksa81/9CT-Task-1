# 9CT200 Assessment 1 - Mechantronics

## By Charles McDonagh

## Part I - Requirements Outline

### Purpose

I need to design and code a program for an EV3 robot to navigate a map and move two blocks to a zone. It must do this without either leaving the map, or touching two obsticles around the map. It must include at least two sensors, either a colour, ultrasonic or pressure sensor, or all three.

### Key Actions 

- Use a pressure sensor to detect the attachment of a block
- Use a colour sensor to detect the colour of a block
- Take a set path to avoid obsticles 
- Use an ultrasonic sensor to detect the range of objects.

### Functional Requirements 
- **Block Detection** - The robot must use a ultrasonic sensor to detect the location of block.
- **Block Classification** - The robot must classify encountered blocks in terms of colour.
- **Block Avoidance** - The robot must take a special path to avoid enemy blocks.
- **Block Movement** - The robot must use a pressure sensor and an engineered system to pickup and move blocks.

### Use Cases

1. **Block Detection** - Scenario: The robot detects a block 10 centimeters from it.

   - Inputs: The ultrasonic sensor detects an object at the  10 cm mark.

   - Action: The robot more further forward to within the range of the colour sensor.

   - Expected Outcome: The robot allows for the colour sensor to classify the colour.

4. **Block Classifictation** - Scenario: The robot has moved itself to classify an object that needs to be picked up.

   - Inputs: The colour sensor detects the positive object.

   - Action: The robot uses it's grabber to pick up the object.

   - Expected Outcome: The robot gains control of the positive object.

8. **Block Avoidance** - Scenario: The robot detects a negative block

   - Inputs: The colour detection of a negative block.

   - Action: The robot takes a set path around the block to place itself ~ 10 centimeters forward of it's starting positions.

   - Expected Outcome: The robot is on the opposite side of the block without colliding with it.

12. **Block Movement** - Scenario: The robot has picked up a positive block but does not know whether it is completely picked up

    - Inputs: The pressure sensor on the grabber.

    - Action: The robot uses the pressure sensor to detect if the block is fully inserted/grabbed.

    - Expected Outcome: The robot confirms that the block will not move after pickup.
### Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Block Detection| The Ultrasonic sensor detects an object within 10cm|The robot moves forward to identify the object|
|Block Classification|The colour sensor detects the colour of a block|The robot either picks up or avoids the block|
|Block Avoidance|A negative block is detected by the classification|The robot moves away from the block in a set path|
|Block Movement|A positive block is detected by the classification|The robot uses it's grabber to pickup the block.|

### Non-Functional Requirements
- The robot should find it's path without extra movement un-needed.
- The robot should move around dangerous blocks without undue delay.
- The robot should aim to grab and pickup the block without a large number of undue tries.

## Part III - Development and Testing


The test program used to test the movement of the sensor movement mechanism's various iterations.
```python
 #!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

sensor_motor = Motor(Port.A)

"""Used to test the movement of the colour sensor's motor, using run_angle to move the motor at 
a speed of 90 degrees per second for 90 degrees, to stop the motor from hitting the ground or the wheels.
It then moves it back to it's previous position."""

sensor_motor.run_angle(90, 90)
sensor_motor.run_angle(90, -90) 
```

The test program used to test the color sensor's color sensing ability.

```
"""Tests the colour sensor, to detect the two good blocks (red or yellow), making one beep
unrecognised blocks or undetect makes two beeps."""


if colour_sensor.color() == Color.RED or Color.YELLOW:
    #pick up here
    speaker.beep()
else:
    #move back here and turn 90 degrees
    speaker.beep()
    speaker.beep()
```
