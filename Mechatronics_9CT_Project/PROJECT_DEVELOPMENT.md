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

## Part II - Pseudocode and Flowcharts 

### Pseudocode

**Main Loop**
```
BEGIN
   WHILE block_counter > 2
      block_search
      block_check
      block_return
   ENDWHILE
END
```
**block_search**
```
BEGIN
counter1 = 30
counter2 = 60
   WHILE block_found = False and block_grabbed = False
      while counter1 > 0
        Turn 1 degree right
        READ ultrasonic_sensor
        IF ultrasonic_sensor > detect distance:
           block_found = True 
           counter1 = 0
           counter2 = 0
        ELSE:
           counter1 =- 1
      while counter2 > 0 
        Turn 1 degree left
        READ ultrasonic_sensor
        IF ultrasonic_sensor > detect distance:
           block_found = True 
           counter1 = 0
           counter2 = 0
        ELSE:
           counter2 =- 1
      Turn 30 degrees right
      Move forward 10 centimeters
END
```
**block_check**
```
BEGIN
   WHILE block_found = True and block_grabbed = False
      WHILE ultrasonic_sensor > check_distance
        Move forward 2.5 centimeters
        READ ultrasonic_sensor
    Move colour sensor to foward position
    IF colour_sensor = red or yellow
       Move foward to contact
       Colour sensor to down position
       block_grabbed = True
       block_found = False
    ELSE
       Move back distance
       Turn left 90 degrees
       Move forward distance
       Turn right 90 degrees
       Move forward distance x 2
       Turn right 90 degrees
       Move forward distance
       Turn left 90 degrees
       block_found = False
   ENDWHILE
END
```
### Flowcharts



## Part III - Development and Testing

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Block Detection| The Ultrasonic sensor detects an object within 10cm|The robot moves forward to identify the object|

This test case was relatively easy to accomplish, using this simple section of code. No extra development was required, due to the simplistic nature of the case. This case was absolutely successful, with only mininmal testing required to ensure it worked. The only possible improvement could be somehow increasing the speed, though this would come at the cost of possibly hitting a negative block.

```python
if block_found == True and block_grabbed == False:
    while ultrasonicsensor.distance() > check_block_distance:
        robot.straight(2.5) #robot moves forward slowly to detect distance
```

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Block Classification|The colour sensor detects the colour of a block|The robot either picks up or avoids the block|

This test case was slightly harder to code, as it required the construction of the physical sensor motor. Though after this was complete, it was simply a need to code a few if statements to create the checking. The physical motor may not be the most efficient way to check the colour for both the ground and blocks, but aside from using a second sensor, it was the msot obvious to my group at the time, as we all used it. The current_colour mode of the mode of the sensor took some getting used to, as we had only previously used the reflection version.
```py
if block_found == True and block_grabbed == False:
    while ultrasonic_sensor.distance() > check_block_distance:
        robot.straight(2.5) #robot moves forward slowly to detect distance
    robot_motor.run_angle (-90,90) #moves the colour detector to forward
    if current_color == Color.RED or Color.YELLOW:
        wait(30) #moves the robot forward so that the block is being pushed
        robot.straight(2.5)
        sensor_motor.run_angle (90,90) #moves the colour detector back to down
        block_found = False
        block_grabbed = True
    else:
        ev3.screen.print("Bad block found")
        ev3.screen.print(current_color)
        ev3.screen.clear()
        robot.straight(-10) #Moves the robot 10 ahead of the bad block
        robot.turn(-90)
        robot.straight(10)
        robot.turn(90)
        robot.straight(20)
        robot.turn(10)
        robot.straight(10)
        robot.turn(-90)
        sensor_motor.run_angle (90,90)
        block_found = False
```
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Block Avoidance|A negative block is detected by the classification|The robot moves away from the block in a set path|

This case was possibly the easiest, and was so simple it could be included in the code snippet for the previous case. The only issues that were encountered were to do with the distances the robot had to move. To ensure there was no unnecessary bumping, the distances had to be perfected. This hardcoding likely isn't optimal, and a simple 90 degree turn may have been possible, but it was included in order to ensure that the robot did not accidentally end in a loop of constantly detecting and checking the same block.

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Block Movement|A positive block is detected by the classification|The robot uses it's grabber to pickup the block.|

This case was actually abandoned soon into the hardware stage of development, as the idea of having another motor placed at the front of the robot, alongside the sensor motor would have been too much. Rather, it was replaced with a pushing mechanism, where the two forward sensors (the pressure and colour) would inadvertantly contain a small section of containment, enough for the small turns the robot would undertake. Another motor probably could have been included, but the weight on the front way already getting heavy, and to risk having the front dragging, making all movement measurements somewhat invalid made no sense. Some element of risk is still involved, as the smaller grapplers the sensor make up are more likely to miss the block, but this is considered an accceptable chance.

Also included are two other programs that were made to test the colour sensor's colour testing mode and the sensor movement mechanism.

The test program used to test the movement of the sensor movement mechanism's various iterations.
```python
"""Used to test the movement of the colour sensor's motor, using run_angle to move the motor at 
a speed of 90 degrees per second for 90 degrees, to stop the motor from hitting the ground or the wheels.
It then moves it back to it's previous position."""

sensor_motor.run_angle(90, 90)
sensor_motor.run_angle(90, -90) 
```

The test program used to test the color sensor's color sensing ability.

```py
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

## Part IV - Evaluation

### Peer Evaluation - Fraser Maple 
*When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project*

**3/5**

*Explain the reason for this score in detail:*

I think Fraser did well with the time we were all given. Though his code wasn't necessarily as influental towards the final group code was as Oscar's, he still wrote a full program, of which elements were used in my final code. He also put plenty of effort into the theory components and the ideation stage of the design.

*When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?*

**3/5**

*Explain the reason for this score in detail:*

Again, though Fraser's code was less vital for the group's efforts than Oscar's and mine, it still contributed greatly to what was required, and the theory and ideation aspects included can't be missed.

*When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?*

**4/5**

*Explain the reason for this score in detail:*

Honestly, I didn't see much of the testing of his final test case, and as far as I'm sure, it wasn't tested very thoroughly at all, but this is mostly due to the various technical issues we and the class experienced in attempting to test our robots. Having read through the code on occasion, it seemed solid, and with testing could well have been successful.

*When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?*

**4/5**

*Explain the reason for this score in detail:*

I think, in total, given the various issues and problems the group was faced with both individually and as a whole, Fraser fared well in the totality of the project, and through this, came out with what would have been a successful piece of code. 

### Peer Evaluation - Oscar Dodd
*When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project*

**5/5**

*Explain the reason for this score in detail:*

Oscar put in plenty of effort in the project, withot a doubt. I think it likely outpaces mine, and his discussions during the ideation stage were vital. I've borrowed various pieces of his code for my final piece of code, and he's done the same with mine.

*When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?*

**5/5**

*Explain the reason for this score in detail:*

Oscar's contributions, both in the hardware department, and in the coding sections, were very clear to me. He did the majority of the engineering work for the sensor motor, and this section was, as an example, used by all of the team.

*When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?*

**4/5**

*Explain the reason for this score in detail:*

Oscar's code I believe was very similar to mine in the end, having borrowed heavily from eachother. His does, I believe, lack the organisation of functions, all being executed in a while True loop. Otherwise, having read through and watched tests, I believe the code would have been extremely successful with extra testing.

*When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?*

**5/5**

*Explain the reason for this score in detail:*

From the theory to the actual coding and testing, Oscar was useful to all the members of the team, both as someone to bounce ideas and code off of, to working on his own code. His performance was, in my opinion, vital to the success of my code, at least.

### Personal Evaluation

I feel my final test comparative to my functional criteria was obviously poor. A bug caused it to immedately malfunction and and having detected a block, do a full 30 degree turn to the right, before driving straight forwards, likely attempting to find a block that did not exist. It's possible this 30 degree turn was caused by the while loop the searching program existed in, though the changing of the block_found value to True should have broken the loop regardless. Besides this failure, should the rest of the code have gone to plan, I believe I will have accomplished all my functional criteria, besides the abandoned grabber.

Again, due to the undue bug that was fixed too late on the friday of the test, the accomplishment of any tests were impossible, but besides this loss, mainly due to technical issues preceeding the final development of the code, I believe the code should have accomplished the majority of it's non-functional requirements. Though again, this includes a section on the abandoned grabber. Otherwise, movement and avoidance without undue delay would likely have been accomplished, without any unneeded movement included in the code.

Despite the fact my group was beset with a number of challenges and bugs, having read through all fo our codes, I believe that with additional time for bugfixing, all of our codes should have been able to complete our goal, without any issues in the execution. Despite having our codes beset by bugs, we did manage to, at the very least, construct working hardware for our robot, and with the time to impliment our ideas, they should all have worked.

I feel as if I managed my time when working somewhat well, though there were obviously challenges, especially with the nature of the robots, cables and the various other challenges, I feel my development timeline was not perfect, but was manageable, and I did a good job managing the time I did have for testing and coding in class.

My code is, essentially, a team collaboration, with sections borrowed from both Oscar and Fraser, and I feel our team worked well together. We didn't have many disagreements, and they were settled easily when they did arise. Our group work on the hardware of the robot, especially the colour motor, was 100% a group effort, in both designing and engineering the piece. 

Beyond bugfixing, a number of improvement could be made to the final product. First and foremost, if a smaller frame for the robot was available, it could be of great use to the group, as it would allow the movement of the robot around the various blocks could be made much more efficient. In addition, with more time, I believe that the addition of a more specialised grabber may have been possible, of possibly a spear design, with sufficient counterwight at the back of the robot, could have improvement the reliability of the block movement phase of the program.

